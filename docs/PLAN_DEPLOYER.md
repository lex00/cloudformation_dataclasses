# Plan: CloudFormation Stack Manager (Deployer)

## Goal

Add a `cfn-stack` CLI and programmatic API to deploy and manage CloudFormation stacks with:
- Interactive deployments with changeset preview and approval
- Drift-aware change detection
- Real-time event streaming
- Recovery operations for failed/stuck stacks
- S3 template staging for large templates
- Integration with existing Template and DeploymentContext classes

---

## Design Questions

### Should `Template.deploy()` exist?

**Proposed Answer: Yes, with optional `Deployer` injection**

```python
# Simple case - uses context for AWS config
template = Template.from_registry(context=ctx)
result = template.deploy()  # Derives stack name, region from ctx

# Explicit deployer for more control
deployer = Deployer(profile="prod", region="us-east-1")
result = template.deploy(deployer=deployer, stack_name="my-stack")

# Or use deployer directly
result = deployer.deploy(template, stack_name="my-stack")
```

### Stack Name Derivation

When `stack_name` is not provided, derive from context:

```python
def derive_stack_name(template: Template) -> str:
    """Derive stack name from template's context."""
    # Look for context in resources
    for resource in template.resources:
        if resource.context:
            ctx = resource.context
            # Pattern: {project_name}-{component}-{stage}
            parts = [p for p in [ctx.project_name, ctx.component, ctx.stage] if p]
            if parts:
                return "-".join(parts)

    # Fallback: use template description or raise
    if template.description:
        return template.description.replace(" ", "-")[:64]

    raise ValueError("Cannot derive stack name. Provide stack_name or use DeploymentContext.")
```

### Region Derivation

```python
def get_region(template: Template, explicit_region: str | None) -> str:
    """Get region from explicit param, context, or environment."""
    if explicit_region:
        return explicit_region

    # Check context
    for resource in template.resources:
        if resource.context and resource.context.region:
            return resource.context.region

    # Fall back to boto3 default (env var, config file, etc.)
    return None  # Let boto3 determine
```

---

## API Design

### Programmatic API

```python
from cloudformation_dataclasses import Template, Deployer
from cloudformation_dataclasses.stack_manager import DeployResult, StackStatus

# Option 1: Template.deploy() - simple, integrated
template = Template.from_registry(context=ctx)
result = template.deploy(
    stack_name="my-stack",        # Optional if derivable from context
    profile="prod",               # Optional AWS profile
    region="us-east-1",           # Optional, uses context.region
    parameters={"Env": "prod"},   # Optional parameter overrides
    tags={"Team": "Platform"},    # Optional additional tags
    capabilities=["CAPABILITY_IAM"],
    wait=True,                    # Wait for completion (default)
    detect_drift=False,           # Run drift detection first
    auto_approve=False,           # Skip confirmation (for CI/CD)
)

# Result object
result.stack_name      # "my-stack"
result.stack_id        # "arn:aws:cloudformation:..."
result.status          # StackStatus.UPDATE_COMPLETE
result.outputs         # {"VpcId": "vpc-123", ...}
result.changes         # List of changes made
result.events          # List of stack events

# Option 2: Deployer class - more control, reusable
deployer = Deployer(
    profile="prod",
    region="us-east-1",
    s3_bucket="my-staging-bucket",  # For large templates
)

result = deployer.deploy(template, stack_name="my-stack")
result = deployer.delete("my-stack")
result = deployer.diff(template, stack_name="my-stack")
status = deployer.status("my-stack")
events = deployer.events("my-stack", follow=True)
```

### CLI Commands

```bash
# Deploy from Python module
cfn-stack deploy my_stack.main --stack-name MyStack

# Deploy with auto-derived stack name (from context)
cfn-stack deploy my_stack.main

# Deploy from file
cfn-stack deploy ./template.json --stack-name MyStack

# Other commands
cfn-stack delete MyStack
cfn-stack status MyStack
cfn-stack events MyStack --follow
cfn-stack diff my_stack.main --stack-name MyStack --detect-drift
cfn-stack continue-rollback MyStack
cfn-stack cancel MyStack
```

---

## Context Integration

### DeploymentContext as Stack Configuration

The existing `DeploymentContext` already captures deployment-relevant information:

```python
@cloudformation_dataclass
class MyContext:
    context: DeploymentContext
    project_name = "acme"           # → Stack name prefix
    component = "api"               # → Stack name component
    stage = "prod"                  # → Stack name suffix
    deployment_group = "blue"       # → For blue/green
    region = "us-east-1"           # → AWS region for deployment
```

**Stack name derivation**: `{project_name}-{component}-{stage}` → `acme-api-prod`

**Blue/green**: With `deployment_group`, stack name becomes `acme-api-prod-blue`

### Extended Context for Deployment Settings

Option A: Add deployment fields to DeploymentContext:

```python
@dataclass
class DeploymentContext:
    # Existing fields...
    project_name: str
    component: str
    stage: str
    region: str

    # New optional deployment fields
    aws_profile: Optional[str] = None
    s3_staging_bucket: Optional[str] = None
    capabilities: list[str] = field(default_factory=lambda: ["CAPABILITY_IAM"])
    auto_approve: bool = False  # For CI/CD
```

Option B: Keep DeploymentContext focused on naming, use Deployer for AWS config:

```python
# DeploymentContext stays focused on naming/tagging
# Deployer handles AWS-specific config
deployer = Deployer.from_context(ctx, profile="prod")
```

**Recommendation**: Option B - keeps concerns separated

---

## Template.deploy() Implementation

```python
# In template.py

@dataclass
class Template:
    # ... existing fields ...

    def deploy(
        self,
        stack_name: str | None = None,
        *,
        profile: str | None = None,
        region: str | None = None,
        parameters: dict[str, str] | None = None,
        tags: dict[str, str] | None = None,
        capabilities: list[str] | None = None,
        wait: bool = True,
        detect_drift: bool = False,
        auto_approve: bool = False,
        s3_bucket: str | None = None,
        timeout_minutes: int = 30,
        deployer: "Deployer | None" = None,
    ) -> "DeployResult":
        """
        Deploy this template as a CloudFormation stack.

        Args:
            stack_name: Stack name (derived from context if not provided)
            profile: AWS profile name
            region: AWS region (uses context.region if not provided)
            parameters: Parameter overrides
            tags: Additional tags (merged with context tags)
            capabilities: CloudFormation capabilities
            wait: Wait for deployment to complete
            detect_drift: Run drift detection before deployment
            auto_approve: Skip confirmation prompts
            s3_bucket: S3 bucket for template staging (large templates)
            timeout_minutes: Deployment timeout
            deployer: Pre-configured Deployer instance

        Returns:
            DeployResult with status, outputs, and events

        Example:
            >>> template = Template.from_registry(context=ctx)
            >>> result = template.deploy()
            >>> print(result.status)
            StackStatus.CREATE_COMPLETE
        """
        from cloudformation_dataclasses.stack_manager import Deployer

        # Use provided deployer or create one
        if deployer is None:
            # Derive region from context if not provided
            effective_region = region or self._get_context_region()
            deployer = Deployer(
                profile=profile,
                region=effective_region,
                s3_bucket=s3_bucket,
            )

        # Derive stack name if not provided
        if stack_name is None:
            stack_name = self._derive_stack_name()

        return deployer.deploy(
            template=self,
            stack_name=stack_name,
            parameters=parameters,
            tags=tags,
            capabilities=capabilities,
            wait=wait,
            detect_drift=detect_drift,
            auto_approve=auto_approve,
            timeout_minutes=timeout_minutes,
        )

    def _get_context_region(self) -> str | None:
        """Extract region from first resource with context."""
        for resource in self.resources:
            if resource.context and resource.context.region:
                return resource.context.region
        return None

    def _derive_stack_name(self) -> str:
        """Derive stack name from context."""
        for resource in self.resources:
            if resource.context:
                ctx = resource.context
                parts = [p for p in [ctx.project_name, ctx.component, ctx.stage] if p]
                if ctx.deployment_group:
                    parts.append(ctx.deployment_group)
                if parts:
                    return "-".join(parts)

        if self.description:
            # Sanitize description for stack name
            name = "".join(c if c.isalnum() or c == "-" else "-" for c in self.description)
            return name[:64]

        raise ValueError(
            "Cannot derive stack name. Provide stack_name parameter or use DeploymentContext "
            "with project_name/component/stage."
        )

    def delete(
        self,
        stack_name: str | None = None,
        *,
        wait: bool = True,
        deployer: "Deployer | None" = None,
        **kwargs,
    ) -> "DeployResult":
        """Delete the stack. See deploy() for parameter docs."""
        from cloudformation_dataclasses.stack_manager import Deployer

        if deployer is None:
            deployer = Deployer(**kwargs)

        if stack_name is None:
            stack_name = self._derive_stack_name()

        return deployer.delete(stack_name, wait=wait)

    def diff(
        self,
        stack_name: str | None = None,
        *,
        detect_drift: bool = False,
        deployer: "Deployer | None" = None,
        **kwargs,
    ) -> "DiffResult":
        """Show what would change without deploying."""
        from cloudformation_dataclasses.stack_manager import Deployer

        if deployer is None:
            deployer = Deployer(**kwargs)

        if stack_name is None:
            stack_name = self._derive_stack_name()

        return deployer.diff(self, stack_name, detect_drift=detect_drift)
```

---

## Module Structure

```
src/cloudformation_dataclasses/
├── core/
│   ├── template.py           # Add deploy(), delete(), diff() methods
│   └── ...
└── stack_manager/            # New package
    ├── __init__.py           # Public API: Deployer, DeployResult, StackStatus
    ├── deployer.py           # Deployer class (~300 lines)
    ├── client.py             # Boto3 wrapper with graceful import (~50 lines)
    ├── states.py             # Stack state machine (~100 lines)
    ├── operations.py         # Create/Update/Delete with waiters (~250 lines)
    ├── changesets.py         # Changeset creation + diff (~150 lines)
    ├── drift.py              # Drift detection (~80 lines)
    ├── events.py             # Event streaming (~100 lines)
    ├── staging.py            # S3 template staging (~80 lines)
    ├── terminal.py           # Colors + formatting (~100 lines)
    ├── results.py            # DeployResult, DiffResult dataclasses (~50 lines)
    ├── exceptions.py         # Exception classes (~50 lines)
    └── cli.py                # argparse CLI (~200 lines)
```

---

## Result Objects

```python
# results.py

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any

class StackStatus(Enum):
    CREATE_COMPLETE = "CREATE_COMPLETE"
    CREATE_FAILED = "CREATE_FAILED"
    CREATE_IN_PROGRESS = "CREATE_IN_PROGRESS"
    UPDATE_COMPLETE = "UPDATE_COMPLETE"
    UPDATE_FAILED = "UPDATE_FAILED"
    UPDATE_IN_PROGRESS = "UPDATE_IN_PROGRESS"
    UPDATE_ROLLBACK_COMPLETE = "UPDATE_ROLLBACK_COMPLETE"
    UPDATE_ROLLBACK_FAILED = "UPDATE_ROLLBACK_FAILED"
    DELETE_COMPLETE = "DELETE_COMPLETE"
    DELETE_FAILED = "DELETE_FAILED"
    DELETE_IN_PROGRESS = "DELETE_IN_PROGRESS"
    ROLLBACK_COMPLETE = "ROLLBACK_COMPLETE"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    # ... etc

@dataclass
class StackEvent:
    timestamp: datetime
    logical_id: str
    resource_type: str
    status: str
    reason: str | None = None

@dataclass
class ResourceChange:
    action: str  # Add, Modify, Remove
    logical_id: str
    resource_type: str
    replacement: str | None  # True, False, Conditional
    details: list[dict[str, Any]] = field(default_factory=list)

@dataclass
class DeployResult:
    """Result of a deploy/delete operation."""
    stack_name: str
    stack_id: str | None = None
    status: StackStatus = StackStatus.CREATE_IN_PROGRESS
    outputs: dict[str, str] = field(default_factory=dict)
    changes: list[ResourceChange] = field(default_factory=list)
    events: list[StackEvent] = field(default_factory=list)

    @property
    def success(self) -> bool:
        return self.status in {
            StackStatus.CREATE_COMPLETE,
            StackStatus.UPDATE_COMPLETE,
            StackStatus.DELETE_COMPLETE,
        }

    @property
    def failed(self) -> bool:
        return "FAILED" in self.status.value

@dataclass
class DiffResult:
    """Result of a diff operation."""
    stack_name: str
    stack_exists: bool
    changes: list[ResourceChange] = field(default_factory=list)
    drift: list[dict[str, Any]] = field(default_factory=list)

    @property
    def has_changes(self) -> bool:
        return len(self.changes) > 0

    @property
    def has_drift(self) -> bool:
        return len(self.drift) > 0
```

---

## Deployer Class

```python
# deployer.py

from dataclasses import dataclass, field
from typing import Any

@dataclass
class Deployer:
    """
    CloudFormation stack deployer.

    Manages stack lifecycle: create, update, delete, diff.
    Handles large templates via S3 staging.

    Example:
        >>> deployer = Deployer(profile="prod", region="us-east-1")
        >>> result = deployer.deploy(template, stack_name="my-stack")
        >>> print(result.status)
    """

    profile: str | None = None
    region: str | None = None
    s3_bucket: str | None = None
    s3_prefix: str = "cfn-templates"
    default_capabilities: list[str] = field(
        default_factory=lambda: ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
    )

    _cf_client: Any = field(default=None, repr=False)
    _s3_client: Any = field(default=None, repr=False)

    @property
    def cf_client(self):
        if self._cf_client is None:
            from .client import get_cloudformation_client
            self._cf_client = get_cloudformation_client(self.profile, self.region)
        return self._cf_client

    @property
    def s3_client(self):
        if self._s3_client is None:
            from .client import get_s3_client
            self._s3_client = get_s3_client(self.profile, self.region)
        return self._s3_client

    def deploy(
        self,
        template: "Template",
        stack_name: str,
        *,
        parameters: dict[str, str] | None = None,
        tags: dict[str, str] | None = None,
        capabilities: list[str] | None = None,
        wait: bool = True,
        detect_drift: bool = False,
        auto_approve: bool = False,
        timeout_minutes: int = 30,
    ) -> DeployResult:
        """Deploy template as CloudFormation stack."""
        from .operations import StackOperations
        from .changesets import ChangesetManager
        from .drift import DriftDetector
        from .staging import TemplateStager
        from .events import EventStreamer

        # Stage template if too large
        template_body = template.to_json()
        stager = TemplateStager(self.s3_client, self.s3_bucket, self.s3_prefix)
        template_param = stager.stage_if_needed(template_body, stack_name)

        ops = StackOperations(self.cf_client)

        # Check if stack exists
        stack_exists = ops.stack_exists(stack_name)

        # Drift detection (if requested and stack exists)
        if detect_drift and stack_exists:
            detector = DriftDetector(self.cf_client)
            drift_result = detector.detect(stack_name)
            if drift_result.has_drift and not auto_approve:
                self._print_drift(drift_result)
                if not self._confirm("Continue despite drift?"):
                    raise UserCancelledError("Deployment cancelled due to drift")

        # Create changeset
        changeset_mgr = ChangesetManager(self.cf_client)
        changeset = changeset_mgr.create(
            stack_name=stack_name,
            template_param=template_param,
            parameters=parameters,
            tags=tags,
            capabilities=capabilities or self.default_capabilities,
            is_update=stack_exists,
        )

        # Show diff and confirm
        if not auto_approve:
            self._print_changeset(changeset)
            if not self._confirm("Deploy these changes?"):
                changeset_mgr.delete(stack_name, changeset.name)
                raise UserCancelledError("Deployment cancelled")

        # Execute changeset
        changeset_mgr.execute(stack_name, changeset.name)

        if not wait:
            return DeployResult(
                stack_name=stack_name,
                status=StackStatus.UPDATE_IN_PROGRESS if stack_exists else StackStatus.CREATE_IN_PROGRESS,
            )

        # Stream events while waiting
        streamer = EventStreamer(self.cf_client)
        events = []
        for event in streamer.stream(stack_name):
            events.append(event)
            self._print_event(event)

        # Get final status
        stack = ops.describe_stack(stack_name)

        return DeployResult(
            stack_name=stack_name,
            stack_id=stack["StackId"],
            status=StackStatus(stack["StackStatus"]),
            outputs={o["OutputKey"]: o["OutputValue"] for o in stack.get("Outputs", [])},
            changes=changeset.changes,
            events=events,
        )

    def delete(self, stack_name: str, *, wait: bool = True) -> DeployResult:
        """Delete a CloudFormation stack."""
        # ... implementation

    def diff(
        self,
        template: "Template",
        stack_name: str,
        *,
        detect_drift: bool = False,
    ) -> DiffResult:
        """Show what would change without deploying."""
        # ... implementation

    def status(self, stack_name: str) -> StackStatus:
        """Get current stack status."""
        # ... implementation

    def events(self, stack_name: str, *, follow: bool = False) -> list[StackEvent]:
        """Get stack events."""
        # ... implementation
```

---

## S3 Template Staging

```python
# staging.py

TEMPLATE_BODY_LIMIT = 51_200  # 50KB

class TemplateStager:
    def __init__(self, s3_client, bucket: str | None, prefix: str):
        self.s3 = s3_client
        self.bucket = bucket
        self.prefix = prefix

    def stage_if_needed(self, template_body: str, stack_name: str) -> dict:
        """Return {"TemplateBody": ...} or {"TemplateURL": ...}."""
        if len(template_body.encode()) <= TEMPLATE_BODY_LIMIT:
            return {"TemplateBody": template_body}

        if self.bucket is None:
            self.bucket = self._get_or_create_bucket()

        key = f"{self.prefix}/{stack_name}/{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        self.s3.put_object(Bucket=self.bucket, Key=key, Body=template_body)

        return {"TemplateURL": f"https://{self.bucket}.s3.amazonaws.com/{key}"}
```

---

## Dependencies

### Runtime Dependencies

The `[stack]` optional extra adds **boto3** and its transitive dependencies:

| Package | Purpose | Size |
|---------|---------|------|
| `boto3` | AWS SDK for Python | ~1 MB |
| `botocore` | Low-level AWS interface (boto3 dep) | ~80 MB |
| `s3transfer` | S3 transfer utilities (boto3 dep) | ~200 KB |
| `jmespath` | JSON query language (boto3 dep) | ~50 KB |
| `python-dateutil` | Date parsing (botocore dep) | ~300 KB |
| `urllib3` | HTTP client (botocore dep) | ~300 KB |

**Total install size**: ~80-100 MB (dominated by botocore's service definitions)

**Note**: This is an **optional** dependency. Users who only generate templates don't need boto3 - it's only required for `cfn-stack` CLI and `Template.deploy()`.

### pyproject.toml Changes

```toml
[project.optional-dependencies]
yaml = ["pyyaml>=6.0"]
importer = ["pyyaml>=6.0"]
stack = ["boto3>=1.34.0"]  # New - for cfn-stack CLI and Template.deploy()

[project.scripts]
cfn-dataclasses-import = "cloudformation_dataclasses.importer.cli:main"
cfn-dataclasses-init = "cloudformation_dataclasses.skeleton.cli:main"
cfn-stack = "cloudformation_dataclasses.stack_manager.cli:main"  # New
```

### Dev Dependencies (for testing)

```toml
[dependency-groups]
dev = [
    # ... existing dev deps ...
    "boto3>=1.34.0",     # For stack manager tests
    "moto[cloudformation,s3]>=5.0.0",  # AWS mocking
]
```

---

## Testing Strategy

### Test Dependencies

| Package | Purpose | Size |
|---------|---------|------|
| `moto` | AWS service mocking | ~10 MB |

**Moto** is the recommended library for testing boto3 code:
- Pure Python, runs in-process (no Docker required)
- Supports `@mock_aws` decorator for all services
- Supports CloudFormation stack operations, changesets, drift detection
- Active development, good CloudFormation support

**Alternatives considered**:
- **LocalStack**: More complete but requires Docker, heavier weight
- **botocore Stubber**: Lower-level, requires manual response setup
- **pytest-localstack**: Docker-based, slower startup

### Mocking Strategy

```python
# tests/stack_manager/conftest.py
import pytest
from moto import mock_aws

@pytest.fixture
def aws_credentials():
    """Mock AWS credentials for moto."""
    import os
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

@pytest.fixture
def cf_client(aws_credentials):
    """Mocked CloudFormation client."""
    with mock_aws():
        import boto3
        yield boto3.client("cloudformation", region_name="us-east-1")

@pytest.fixture
def s3_client(aws_credentials):
    """Mocked S3 client."""
    with mock_aws():
        import boto3
        yield boto3.client("s3", region_name="us-east-1")
```

### Test Structure

```
tests/stack_manager/
├── conftest.py           # Shared fixtures (mock clients)
├── test_states.py        # State machine logic (no AWS mocking needed)
├── test_results.py       # Result dataclasses (no AWS mocking needed)
├── test_terminal.py      # Color output formatting (no AWS mocking needed)
├── test_cli.py           # CLI argument parsing (no AWS mocking needed)
├── test_staging.py       # S3 staging (moto mocked)
├── test_operations.py    # Stack create/update/delete (moto mocked)
├── test_changesets.py    # Changeset creation + diff (moto mocked)
├── test_drift.py         # Drift detection (moto mocked)
├── test_events.py        # Event streaming (moto mocked)
├── test_deployer.py      # Deployer integration (moto mocked)
└── test_template_deploy.py  # Template.deploy() integration (moto mocked)
```

### Example Test Cases

```python
# test_operations.py
from moto import mock_aws
import boto3
import pytest

@mock_aws
def test_create_stack():
    """Test stack creation."""
    cf = boto3.client("cloudformation", region_name="us-east-1")

    from cloudformation_dataclasses.stack_manager.operations import StackOperations
    ops = StackOperations(cf)

    template = '{"AWSTemplateFormatVersion": "2010-09-09", "Resources": {}}'
    result = ops.create_stack("test-stack", template)

    assert result["StackId"].startswith("arn:aws:cloudformation:")

@mock_aws
def test_stack_exists():
    """Test stack existence check."""
    cf = boto3.client("cloudformation", region_name="us-east-1")

    from cloudformation_dataclasses.stack_manager.operations import StackOperations
    ops = StackOperations(cf)

    assert ops.stack_exists("nonexistent-stack") is False

    # Create a stack
    cf.create_stack(
        StackName="my-stack",
        TemplateBody='{"AWSTemplateFormatVersion": "2010-09-09", "Resources": {}}',
    )

    assert ops.stack_exists("my-stack") is True

@mock_aws
def test_stack_in_progress_detection():
    """Test detection of in-progress stack states."""
    cf = boto3.client("cloudformation", region_name="us-east-1")

    from cloudformation_dataclasses.stack_manager.states import is_in_progress

    # Create stack (will be CREATE_COMPLETE in moto, but we can check the logic)
    cf.create_stack(
        StackName="my-stack",
        TemplateBody='{"AWSTemplateFormatVersion": "2010-09-09", "Resources": {}}',
    )

    stack = cf.describe_stacks(StackName="my-stack")["Stacks"][0]
    assert is_in_progress(stack["StackStatus"]) is False
```

```python
# test_staging.py
from moto import mock_aws
import boto3
import pytest

@mock_aws
def test_small_template_not_staged():
    """Templates under 50KB should use TemplateBody."""
    s3 = boto3.client("s3", region_name="us-east-1")

    from cloudformation_dataclasses.stack_manager.staging import TemplateStager

    stager = TemplateStager(s3, bucket="my-bucket", prefix="templates")

    small_template = '{"AWSTemplateFormatVersion": "2010-09-09"}'
    result = stager.stage_if_needed(small_template, "my-stack")

    assert "TemplateBody" in result
    assert result["TemplateBody"] == small_template

@mock_aws
def test_large_template_staged_to_s3():
    """Templates over 50KB should be staged to S3."""
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="my-bucket")

    from cloudformation_dataclasses.stack_manager.staging import TemplateStager

    stager = TemplateStager(s3, bucket="my-bucket", prefix="templates")

    # Create a template larger than 50KB
    large_template = '{"AWSTemplateFormatVersion": "2010-09-09", "Data": "' + "x" * 60000 + '"}'
    result = stager.stage_if_needed(large_template, "my-stack")

    assert "TemplateURL" in result
    assert "my-bucket" in result["TemplateURL"]
```

```python
# test_template_deploy.py
from moto import mock_aws
import boto3
import pytest

@mock_aws
def test_template_deploy_creates_stack():
    """Test Template.deploy() creates a CloudFormation stack."""
    from cloudformation_dataclasses import Template
    from cloudformation_dataclasses.aws.s3 import Bucket

    # Build a simple template
    bucket = Bucket(bucket_name="test-bucket")
    bucket.logical_id = "TestBucket"
    template = Template(resources=[bucket], description="Test stack")

    # Deploy it
    result = template.deploy(
        stack_name="test-stack",
        region="us-east-1",
        auto_approve=True,  # Skip confirmation
    )

    assert result.success
    assert result.stack_name == "test-stack"
    assert result.status.value == "CREATE_COMPLETE"
```

### Unit Tests (No AWS Mocking)

Some modules can be tested without moto:

```python
# test_states.py
def test_stable_states():
    from cloudformation_dataclasses.stack_manager.states import STABLE_STATES, is_stable

    assert is_stable("CREATE_COMPLETE")
    assert is_stable("UPDATE_COMPLETE")
    assert not is_stable("CREATE_IN_PROGRESS")
    assert not is_stable("DELETE_FAILED")

def test_failed_states():
    from cloudformation_dataclasses.stack_manager.states import FAILED_STATES, is_failed

    assert is_failed("CREATE_FAILED")
    assert is_failed("UPDATE_ROLLBACK_FAILED")
    assert not is_failed("CREATE_COMPLETE")

def test_valid_operations():
    from cloudformation_dataclasses.stack_manager.states import get_valid_operations

    ops = get_valid_operations("CREATE_COMPLETE")
    assert "update" in ops
    assert "delete" in ops

    ops = get_valid_operations("ROLLBACK_COMPLETE")
    assert "update" not in ops
    assert "delete" in ops
```

```python
# test_cli.py
def test_deploy_command_parsing():
    from cloudformation_dataclasses.stack_manager.cli import create_parser

    parser = create_parser()
    args = parser.parse_args(["deploy", "my_stack.main", "--stack-name", "MyStack"])

    assert args.command == "deploy"
    assert args.template == "my_stack.main"
    assert args.stack_name == "MyStack"

def test_delete_command_parsing():
    from cloudformation_dataclasses.stack_manager.cli import create_parser

    parser = create_parser()
    args = parser.parse_args(["delete", "MyStack", "--yes"])

    assert args.command == "delete"
    assert args.stack_name == "MyStack"
    assert args.yes is True
```

### Moto Limitations

Be aware of moto's limitations for CloudFormation:
- Changesets are supported but behavior may differ slightly from real AWS
- Drift detection is mocked but may not reflect real-world accuracy
- Some newer CloudFormation features may have incomplete support

For critical deployment workflows, consider integration tests against a real AWS sandbox account.

---

## Implementation Order

1. **Phase 1**: Core infrastructure
   - `exceptions.py`, `client.py`, `states.py`, `results.py`

2. **Phase 2**: Stack operations
   - `operations.py`, `events.py`, `staging.py`

3. **Phase 3**: Changesets + drift
   - `changesets.py`, `drift.py`

4. **Phase 4**: Deployer + Template integration
   - `deployer.py`, update `template.py` with deploy/delete/diff methods

5. **Phase 5**: CLI + terminal
   - `cli.py`, `terminal.py`, pyproject.toml updates

6. **Phase 6**: Tests + docs
   - Unit tests (moto mocked), documentation

---

## Example Usage

### Minimal (Context-Driven)

```python
# my_stack/stack/main.py
from .. import *

@cloudformation_dataclass
class MyContext:
    context: DeploymentContext
    project_name = "acme"
    component = "api"
    stage = "prod"
    region = "us-east-1"

ctx = MyContext()

@cloudformation_dataclass
class MyBucket:
    resource: Bucket
    context = ctx

# my_stack/main.py
def build_template():
    return Template.from_registry(context=ctx)

# Deploy
if __name__ == "__main__":
    template = build_template()
    result = template.deploy()  # Stack: acme-api-prod, Region: us-east-1
    print(f"Stack {result.stack_name}: {result.status.value}")
```

### Explicit Control

```python
from cloudformation_dataclasses import Template
from cloudformation_dataclasses.stack_manager import Deployer

template = build_template()
deployer = Deployer(profile="prod-account", region="eu-west-1")

# Preview changes
diff = deployer.diff(template, "my-custom-stack", detect_drift=True)
if diff.has_drift:
    print("Warning: Stack has drifted!")

# Deploy with explicit settings
result = deployer.deploy(
    template,
    stack_name="my-custom-stack",
    parameters={"Environment": "production"},
    tags={"CostCenter": "12345"},
    auto_approve=True,  # CI/CD mode
)
```

### CLI

```bash
# Deploy from module (context-driven naming)
cfn-stack deploy my_stack.main

# Deploy with explicit name
cfn-stack deploy my_stack.main --stack-name custom-name --profile prod

# Non-interactive for CI/CD
cfn-stack deploy my_stack.main --yes

# Preview changes
cfn-stack diff my_stack.main --detect-drift

# Delete
cfn-stack delete acme-api-prod --yes
```
