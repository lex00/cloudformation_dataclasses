# Agent Testing Pattern: Two-Claude Iterative Development

**Date:** 2025-12-25
**Status:** DRAFT
**Purpose:** Rapidly improve agent ability to create cfn-dataclasses projects through automated iterative testing

---

## Overview

This document describes a testing pattern using two Claude instances to:
1. Generate CloudFormation stack packages from natural language prompts
2. Iteratively improve them through lint/fix cycles
3. Capture feedback for framework improvements

The goal is to identify gaps in the framework, linter, and documentation that prevent agents from successfully creating production-quality stacks.

---

## Architecture

```
┌─────────────────┐     Natural Language      ┌─────────────────┐
│                 │ ◄───────────────────────► │                 │
│  Developer      │     Questions/Answers     │    Runner       │
│  Claude         │                           │    Claude       │
│                 │                           │                 │
│  (Represents    │                           │  (Has CLI       │
│   human intent) │                           │   access)       │
└─────────────────┘                           └────────┬────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │  cfn-dataclasses│
                                              │  CLI tools      │
                                              │  - init         │
                                              │  - lint         │
                                              │  - stubs        │
                                              └────────┬────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │  Generated      │
                                              │  Package        │
                                              │  + RESULTS.md   │
                                              └─────────────────┘
```

### Developer Claude
- Represents a human user with a goal
- Provides the initial natural language prompt
- Answers questions about intent when Runner is uncertain
- Does NOT have access to CLI tools

### Runner Claude
- Has full access to cfn-dataclasses CLI tools
- Executes `init`, `lint`, `stubs` commands
- Writes and modifies Python code
- Asks Developer for clarification on intent
- Writes RESULTS.md with findings

### Orchestrator
- Script that coordinates API calls between the two Claude instances
- Routes messages between Developer and Runner
- Enforces maximum cycle count (3 cycles)
- Collects final outputs

---

## Developer Personas

Configure Developer Claude with different personas to test how Runner handles various user types.

### Persona Definitions

| Persona | Experience | Behavior | Tests |
|---------|------------|----------|-------|
| **Beginner** | New to AWS/IaC | Vague requirements, accepts suggestions, asks "what do you recommend?" | Can Runner work with ambiguity? |
| **Intermediate** | Knows AWS basics | Specific about some things, unsure about others, asks clarifying questions back | Can Runner handle back-and-forth? |
| **Expert** | AWS architect | Precise requirements, pushes back on suggestions, expects best practices | Can Runner handle being corrected? |
| **Terse** | Any level | Minimal answers ("yes", "no", "fine") | Can Runner work without detailed guidance? |
| **Verbose** | Any level | Over-explains everything, adds tangential requirements mid-conversation | Can Runner filter signal from noise? |

### System Prompt Templates

**Beginner:**
```
You are a developer new to AWS and Infrastructure as Code. You have a general idea
of what you want but aren't sure about the technical details. When asked questions:
- Give vague answers when you're unsure ("something like that", "I think so?")
- Ask for recommendations ("what would you suggest?")
- Accept most suggestions with "sounds good" or "sure, let's do that"
- Don't use AWS-specific terminology unless the Runner uses it first
```

**Intermediate:**
```
You are a developer with basic AWS knowledge. You understand VPCs, EC2, and S3
at a high level but aren't sure about best practices. When asked questions:
- Be specific about requirements you know (e.g., "I need t3.medium instances")
- Ask clarifying questions when unsure ("what's the difference between those?")
- Sometimes push back if something seems wrong ("are you sure that's right?")
- Use basic AWS terminology correctly
```

**Expert:**
```
You are a senior AWS solutions architect. You have strong opinions about
infrastructure design and security. When asked questions:
- Give precise, detailed answers with specific values
- Correct the Runner if they suggest suboptimal patterns
- Expect best practices without having to ask (e.g., encryption, least privilege)
- Push back on unnecessary complexity ("that's over-engineered, just use X")
- Use proper AWS terminology and reference specific features
```

**Terse:**
```
You are a busy developer who prefers minimal communication. When asked questions:
- Answer with single words or short phrases: "yes", "no", "fine", "whatever works"
- Don't elaborate unless absolutely necessary
- If a question has options, just pick one without explaining why
- Never ask follow-up questions yourself
```

**Verbose:**
```
You are a developer who likes to think out loud. When asked questions:
- Give long, detailed answers with lots of context and history
- Add tangential requirements mid-answer ("oh, and we might also need...")
- Share your reasoning process ("I'm thinking we could do X, but then again Y...")
- Sometimes contradict yourself slightly ("actually, maybe Z would be better")
- Include irrelevant details ("this reminds me of a project last year...")
```

### Updated Orchestrator with Personas

```python
PERSONAS = {
    "beginner": """You are a developer new to AWS and Infrastructure as Code...""",
    "intermediate": """You are a developer with basic AWS knowledge...""",
    "expert": """You are a senior AWS solutions architect...""",
    "terse": """You are a busy developer who prefers minimal communication...""",
    "verbose": """You are a developer who likes to think out loud...""",
}

def run_session(initial_prompt: str, output_dir: str, persona: str = "intermediate") -> str:
    """Run a full Developer/Runner session with specified persona."""

    client = anthropic.Anthropic()

    persona_prompt = PERSONAS.get(persona, PERSONAS["intermediate"])

    developer_messages = []
    runner_messages = []

    # Initialize Developer with persona and prompt
    developer_messages.append({
        "role": "user",
        "content": f"""{persona_prompt}

Your requirement is: {initial_prompt}

A Runner agent will build this for you. Answer questions about your intent
according to your persona. Stay in character throughout the conversation."""
    })

    # ... rest of session logic unchanged ...
```

### Persona Test Matrix

Run each prompt with multiple personas to identify Runner weaknesses:

| Prompt | Beginner | Intermediate | Expert | Terse | Verbose |
|--------|----------|--------------|--------|-------|---------|
| S3 static site | ✓ | ✓ | ✓ | ✓ | ✓ |
| Private VPC + EC2 | ? | ✓ | ✓ | ? | ? |
| ECS Fargate | ? | ? | ✓ | ? | ? |

Legend: ✓ = Expected pass, ? = Uncertain, ✗ = Expected fail

### Persona-Specific Failure Modes

| Persona | Likely Failure | Root Cause |
|---------|----------------|------------|
| Beginner | Wrong resources chosen | Runner assumed too much from vague input |
| Expert | Rejected suggestions | Runner didn't meet expected standards |
| Terse | Incomplete resources | Runner didn't probe for missing details |
| Verbose | Scope creep | Runner tried to implement tangential mentions |

---

## Workflow

### Phase 1: Initialization

**Developer provides initial prompt:**
```
"Build a new package with an autoscaled ec2 instance in a private vpc ready for me to ssh into"
```

**Runner receives prompt and:**
1. Parses the requirements
2. Runs `cfn-dataclasses init -o <package_name>`
3. Plans the resources needed

### Phase 2: Resource Creation

**Runner creates resources based on prompt:**
- Identifies required AWS resources (VPC, Subnets, ASG, Security Groups, etc.)
- Creates resource files in the package
- Imports appropriate AWS modules
- Defines parameters, resources, and outputs

**Runner may ask Developer questions:**
```
Runner: "Should the VPC use public subnets with an Internet Gateway, or private subnets with a NAT Gateway for outbound access?"

Developer: "Private subnets with NAT Gateway. I want the instances to not be directly accessible from the internet."
```

### Phase 3: Lint/Improve Cycles (max 3)

**For each cycle:**

1. **Run linter:**
   ```bash
   cfn-dataclasses lint <package_path>
   ```

2. **If issues found:**
   - Runner analyzes the issues
   - If intent is unclear, asks Developer
   - Applies fixes

3. **If no issues or max cycles reached:**
   - Exit loop
   - Generate stubs: `cfn-dataclasses stubs`

### Phase 4: Results Documentation

**Runner writes RESULTS.md in the generated package:**
- Summary of what was built
- Linting results per cycle
- Questions asked and answers received
- Problems encountered
- Suggestions for framework improvements

---

## RESULTS.md Format

```markdown
# Package Generation Results

**Prompt:** "Build a new package with an autoscaled ec2 instance in a private vpc ready for me to ssh into"

**Package:** ec2_private_vpc
**Date:** 2025-12-25

---

## Summary

Created a CloudFormation stack with:
- VPC with 2 private subnets across 2 AZs
- NAT Gateway for outbound internet access
- Auto Scaling Group with EC2 instances
- Security Group allowing SSH from bastion/VPN
- IAM Instance Profile for SSM Session Manager

---

## Lint Cycles

### Cycle 1
**Issues Found:** 3
- CFD001: Use `ec2.SecurityGroupEgress` instead of inline egress rules
- CFD005: Missing `DependsOn` for NAT Gateway → Internet Gateway
- CFD012: File too large, consider splitting

**Actions Taken:**
- Refactored security group to use separate egress resource
- Added explicit DependsOn
- Split into network.py, compute.py, security.py

### Cycle 2
**Issues Found:** 1
- CFD008: Parameter default value should use Ref() not literal string

**Actions Taken:**
- Fixed parameter reference

### Cycle 3
**Issues Found:** 0
- All lint checks passed

---

## Questions Asked

1. **Runner:** "Should the VPC use public subnets with an Internet Gateway, or private subnets with a NAT Gateway?"
   **Developer:** "Private subnets with NAT Gateway. I want the instances to not be directly accessible from the internet."

2. **Runner:** "What instance type should be used for the EC2 instances?"
   **Developer:** "t3.medium, but make it a parameter so it can be changed."

3. **Runner:** "Should SSH access be restricted to a specific CIDR, or open to the VPC?"
   **Developer:** "VPC only. We'll use a bastion host or SSM."

---

## Problems Encountered

### Problem 1: Missing SSM Endpoint Resources
The linter didn't flag that SSM Session Manager requires VPC endpoints when in a private subnet without NAT.

**Suggestion:** Add a lint rule that checks for SSM-related IAM policies and suggests VPC endpoints for private subnets.

### Problem 2: Unclear NAT Gateway Dependency
Initial attempt didn't include proper dependency ordering. The framework could document this common pattern better.

**Suggestion:** Add example in documentation for private subnet + NAT Gateway pattern.

### Problem 3: Security Group Egress Pattern
Wasn't sure whether to use inline egress or separate resource. Linter caught it, but initial guidance was unclear.

**Suggestion:** Add CLAUDE.md guidance on preferred security group patterns.

---

## Framework Improvement Suggestions

1. **New lint rule:** Detect SSM IAM policies + private subnets → suggest VPC endpoints
2. **Documentation:** Add "Private VPC with NAT Gateway" example to examples/
3. **CLAUDE.md:** Add security group best practices
4. **Init templates:** Consider a `--template private-vpc` option for common patterns
```

---

## Example Session Transcript

```
=== SESSION START ===

[Developer → Orchestrator]
Prompt: "Build a new package with an autoscaled ec2 instance in a private vpc ready for me to ssh into"

[Orchestrator → Runner]
<initial_prompt>
Build a new package with an autoscaled ec2 instance in a private vpc ready for me to ssh into
</initial_prompt>

[Runner]
I'll create a CloudFormation stack package for this. Let me start by initializing the package.

> cfn-dataclasses init -o ec2_private_vpc

Package created. Now I need to clarify some requirements.

[Runner → Developer]
<question>
Should the VPC use public subnets with an Internet Gateway, or private subnets with a NAT Gateway for outbound access?
</question>

[Developer → Runner]
<answer>
Private subnets with NAT Gateway. I want the instances to not be directly accessible from the internet.
</answer>

[Runner]
Understood. Creating private VPC architecture with NAT Gateway.

> Writing ec2_private_vpc/ec2_private_vpc/network.py
> Writing ec2_private_vpc/ec2_private_vpc/compute.py
> Writing ec2_private_vpc/ec2_private_vpc/security.py

Now running lint cycle 1...

> cfn-dataclasses lint ec2_private_vpc/

Issues found:
- CFD001: security.py:45 - Use separate SecurityGroupEgress resource
- CFD005: network.py:78 - Missing DependsOn for NatGateway

Fixing issues...

[Runner → Developer]
<question>
What instance type should be used for the EC2 instances?
</question>

[Developer → Runner]
<answer>
t3.medium, but make it a parameter so it can be changed.
</answer>

[Runner]
Adding InstanceType parameter with t3.medium default.

Running lint cycle 2...

> cfn-dataclasses lint ec2_private_vpc/

Issues found:
- CFD008: params.py:12 - Use Ref() for parameter default

Fixing issue...

Running lint cycle 3...

> cfn-dataclasses lint ec2_private_vpc/

No issues found. All lint checks passed.

Generating stubs...

> cfn-dataclasses stubs ec2_private_vpc/

Writing RESULTS.md...

=== SESSION END ===
```

---

## Implementation: Orchestrator Script

```python
#!/usr/bin/env python3
"""
Orchestrator script for two-Claude testing pattern.
Coordinates Developer and Runner Claude instances.
"""

import anthropic
from dataclasses import dataclass
from typing import Optional

MAX_CYCLES = 3

@dataclass
class Message:
    role: str  # "developer" or "runner"
    content: str

def run_session(initial_prompt: str, output_dir: str) -> str:
    """Run a full Developer/Runner session."""

    client = anthropic.Anthropic()

    developer_messages = []
    runner_messages = []

    # Initialize Developer with the prompt
    developer_messages.append({
        "role": "user",
        "content": f"You are a developer who wants to build a CloudFormation stack. Your requirement is: {initial_prompt}\n\nA Runner agent will build this for you. Answer any questions about your intent naturally and concisely."
    })

    # Initialize Runner with the prompt and tools
    runner_system = """You are a Runner agent with access to cfn-dataclasses CLI tools.

Your job is to:
1. Create a CloudFormation stack package based on the Developer's requirements
2. Run lint/fix cycles (max 3)
3. Ask the Developer questions when intent is unclear
4. Write RESULTS.md documenting the process

Available commands:
- cfn-dataclasses init -o <name>
- cfn-dataclasses lint <path>
- cfn-dataclasses stubs <path>

When you need to ask the Developer a question, output:
<question>Your question here</question>

When you're done, output:
<complete>Path to RESULTS.md</complete>
"""

    runner_messages.append({
        "role": "user",
        "content": f"Developer request: {initial_prompt}"
    })

    # Main loop
    cycles = 0
    while cycles < MAX_CYCLES:
        # Get Runner response
        runner_response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=runner_system,
            messages=runner_messages
        )

        runner_text = runner_response.content[0].text
        runner_messages.append({"role": "assistant", "content": runner_text})

        # Check for question to Developer
        if "<question>" in runner_text:
            question = extract_tag(runner_text, "question")

            # Get Developer answer
            developer_messages.append({
                "role": "user",
                "content": f"The Runner asks: {question}"
            })

            developer_response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=developer_messages
            )

            answer = developer_response.content[0].text
            developer_messages.append({"role": "assistant", "content": answer})

            # Send answer back to Runner
            runner_messages.append({
                "role": "user",
                "content": f"Developer answers: {answer}"
            })

        # Check for completion
        if "<complete>" in runner_text:
            return extract_tag(runner_text, "complete")

        cycles += 1

    return "Max cycles reached"

def extract_tag(text: str, tag: str) -> str:
    """Extract content between <tag> and </tag>."""
    import re
    match = re.search(f"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
    return match.group(1).strip() if match else ""

if __name__ == "__main__":
    import sys
    prompt = sys.argv[1] if len(sys.argv) > 1 else "Build a simple S3 bucket stack"
    result = run_session(prompt, "output/")
    print(f"Session complete. Results: {result}")
```

---

## Conversation Logging

All agent conversations are logged separately for easy review and debugging.

### Log Directory Structure

```
output/
├── ec2_private_vpc/              # Generated package
│   ├── ec2_private_vpc/
│   └── RESULTS.md
└── logs/
    └── ec2_private_vpc/
        ├── session.json          # Full session metadata
        ├── conversation.md       # Human-readable conversation
        ├── developer.jsonl       # Developer Claude messages
        └── runner.jsonl          # Runner Claude messages
```

### session.json

Complete session metadata:

```json
{
  "session_id": "ec2_private_vpc_20251225_143052",
  "prompt": "Build an autoscaled EC2 instance in a private VPC ready for SSH",
  "persona": "intermediate",
  "started_at": "2025-12-25T14:30:52Z",
  "completed_at": "2025-12-25T14:32:15Z",
  "duration_seconds": 83,
  "cycles": 3,
  "questions_asked": 3,
  "lint_issues_total": 4,
  "lint_issues_fixed": 4,
  "status": "success",
  "package_path": "output/ec2_private_vpc",
  "results_path": "output/ec2_private_vpc/RESULTS.md"
}
```

### conversation.md

Human-readable transcript:

```markdown
# Session: ec2_private_vpc
**Prompt:** Build an autoscaled EC2 instance in a private VPC ready for SSH
**Persona:** intermediate
**Date:** 2025-12-25 14:30:52

---

## Initial Request

> Build an autoscaled EC2 instance in a private VPC ready for SSH

---

## Conversation

### [14:30:55] Runner
I'll create a CloudFormation stack package for this. Let me start by initializing...

```bash
cfn-dataclasses init -o ec2_private_vpc
```

Package created. I have a question about the architecture.

### [14:30:58] Runner → Developer
**Question:** Should the VPC use public subnets with an Internet Gateway, or private subnets with a NAT Gateway for outbound access?

### [14:31:02] Developer
Private subnets with NAT Gateway. I want the instances to not be directly accessible from the internet.

### [14:31:05] Runner
Understood. Creating private VPC architecture with NAT Gateway...

---

## Lint Cycle 1

**Command:** `cfn-dataclasses lint ec2_private_vpc/`

**Issues Found:**
- CFD001: security.py:45 - Use separate SecurityGroupEgress resource
- CFD005: network.py:78 - Missing DependsOn for NatGateway

**Actions:** Fixed both issues.

---

## Lint Cycle 2
...
```

### developer.jsonl / runner.jsonl

Raw API messages in JSON Lines format for replay/analysis:

```jsonl
{"timestamp": "2025-12-25T14:30:52Z", "role": "user", "content": "You are a developer..."}
{"timestamp": "2025-12-25T14:30:58Z", "role": "user", "content": "The Runner asks: Should the VPC..."}
{"timestamp": "2025-12-25T14:31:02Z", "role": "assistant", "content": "Private subnets with NAT Gateway..."}
```

### Logging Implementation

```python
import json
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, asdict

@dataclass
class ConversationLogger:
    session_id: str
    output_dir: Path
    prompt: str
    persona: str

    def __post_init__(self):
        self.log_dir = self.output_dir / "logs" / self.session_id
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.started_at = datetime.utcnow()
        self.messages: list[dict] = []
        self.developer_messages: list[dict] = []
        self.runner_messages: list[dict] = []

    def log_developer(self, role: str, content: str):
        """Log a Developer Claude message."""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "role": role,
            "content": content
        }
        self.developer_messages.append(entry)
        self.messages.append({"agent": "developer", **entry})

    def log_runner(self, role: str, content: str):
        """Log a Runner Claude message."""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "role": role,
            "content": content
        }
        self.runner_messages.append(entry)
        self.messages.append({"agent": "runner", **entry})

    def save(self, status: str, cycles: int, questions: int, lint_issues: int):
        """Save all logs to disk."""
        # Save session metadata
        session = {
            "session_id": self.session_id,
            "prompt": self.prompt,
            "persona": self.persona,
            "started_at": self.started_at.isoformat() + "Z",
            "completed_at": datetime.utcnow().isoformat() + "Z",
            "status": status,
            "cycles": cycles,
            "questions_asked": questions,
            "lint_issues_total": lint_issues,
        }
        (self.log_dir / "session.json").write_text(json.dumps(session, indent=2))

        # Save raw messages
        with open(self.log_dir / "developer.jsonl", "w") as f:
            for msg in self.developer_messages:
                f.write(json.dumps(msg) + "\n")

        with open(self.log_dir / "runner.jsonl", "w") as f:
            for msg in self.runner_messages:
                f.write(json.dumps(msg) + "\n")

        # Save human-readable conversation
        self._save_conversation_md()

    def _save_conversation_md(self):
        """Generate human-readable markdown transcript."""
        lines = [
            f"# Session: {self.session_id}",
            f"**Prompt:** {self.prompt}",
            f"**Persona:** {self.persona}",
            f"**Date:** {self.started_at.strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "---",
            "",
        ]

        for msg in self.messages:
            time = msg["timestamp"][11:19]  # Extract HH:MM:SS
            agent = msg["agent"].title()
            role = msg["role"]

            if role == "assistant":
                lines.append(f"### [{time}] {agent}")
                lines.append(msg["content"])
                lines.append("")

        (self.log_dir / "conversation.md").write_text("\n".join(lines))
```

### Updated run_session with Logging

```python
def run_session(initial_prompt: str, output_dir: str, persona: str = "intermediate") -> str:
    """Run a full Developer/Runner session with logging."""

    session_id = f"{sanitize_name(initial_prompt)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    logger = ConversationLogger(
        session_id=session_id,
        output_dir=Path(output_dir),
        prompt=initial_prompt,
        persona=persona
    )

    # ... existing session logic ...

    # Log each message as it happens
    logger.log_developer("user", developer_messages[-1]["content"])
    logger.log_runner("assistant", runner_text)

    # At end of session
    logger.save(
        status="success" if "<complete>" in runner_text else "max_cycles",
        cycles=cycles,
        questions=question_count,
        lint_issues=lint_issue_count
    )

    return result
```

---

## Future Enhancements

1. **Batch Testing**: Run multiple prompts in parallel to identify common failure patterns

2. **Metrics Collection**: Track success rates, common questions, frequent lint issues

3. **Prompt Library**: Curate a set of test prompts covering various AWS patterns:
   - Simple (S3 bucket, SNS topic)
   - Medium (VPC with subnets, Lambda with API Gateway)
   - Complex (ECS Fargate with RDS, multi-region setup)

4. **Regression Testing**: Re-run sessions after framework changes to ensure improvements

5. **Human-in-the-loop**: Option for actual human to play Developer role for edge cases

---

## Prompt Library

A curated set of test prompts covering various AWS patterns and difficulty levels.

### Simple (Expected: 0-1 lint cycles, 0-1 questions)
| Prompt | Expected Resources |
|--------|-------------------|
| "Create an S3 bucket for static website hosting" | S3 Bucket, BucketPolicy |
| "Create an SNS topic with email subscription" | SNS Topic, Subscription |
| "Create a DynamoDB table for user sessions" | DynamoDB Table |

### Medium (Expected: 1-2 lint cycles, 1-3 questions)
| Prompt | Expected Resources |
|--------|-------------------|
| "Create a VPC with public and private subnets" | VPC, Subnets, IGW, NAT, RouteTables |
| "Create a Lambda function triggered by S3 uploads" | Lambda, IAM Role, S3 Bucket, S3 Event |
| "Create an RDS PostgreSQL database in a private subnet" | RDS, DBSubnetGroup, SecurityGroup |

### Complex (Expected: 2-3 lint cycles, 3+ questions)
| Prompt | Expected Resources |
|--------|-------------------|
| "Build an autoscaled EC2 instance in a private VPC ready for SSH" | VPC, Subnets, NAT, ASG, LaunchTemplate, SG, IAM |
| "Create an ECS Fargate service with ALB and RDS backend" | ECS Cluster, Service, TaskDef, ALB, TargetGroup, RDS, VPC |
| "Build a serverless API with Lambda, API Gateway, and DynamoDB" | Lambda, API Gateway, DynamoDB, IAM Roles, CloudWatch |

### Adversarial (Expected: May fail, tests error handling)
| Prompt | Why It's Hard |
|--------|---------------|
| "Create a thing that stores data" | Ambiguous - what kind of data? |
| "Make it secure" | No context - secure what? |
| "Build the same thing as last time" | No history - tests graceful failure |
| "Create an EC2 instance with 1TB of RAM" | Impossible constraint |

---

## Validation Pipeline

After lint passes, additional validation ensures the template actually works.

### Stage 1: Syntax Validation
```bash
# AWS cfn-lint (if available)
cfn-lint template.json

# AWS CloudFormation validate
aws cloudformation validate-template --template-body file://template.json
```

### Stage 2: Build Verification
```bash
# Template builds without errors
python -m <package_name> > template.json
echo $?  # Should be 0
```

### Stage 3: Resource Verification (Optional)
- Check expected resources exist in output
- Verify Ref/GetAtt targets are valid
- Confirm parameter types match usage

---

## Scoring Rubric

Each session is scored on multiple dimensions (0-3 scale):

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **Completeness** | Failed to produce package | Package created but missing resources | Most resources present | All expected resources present |
| **Lint Quality** | Never passed lint | Passed after 3 cycles | Passed after 1-2 cycles | Passed first try |
| **Code Quality** | Invalid Python | Runs but poor patterns | Good patterns | Idiomatic cfn-dataclasses |
| **Template Validity** | Invalid JSON/YAML | Valid syntax, bad references | Valid with warnings | Clean validation |
| **Question Efficiency** | Asked 5+ questions | Asked 3-4 questions | Asked 1-2 questions | Asked 0 questions (when appropriate) |

**Overall Score**: Sum of dimensions (0-15)
- 0-5: Failure - investigate root cause
- 6-9: Partial success - review framework gaps
- 10-12: Success - minor improvements possible
- 13-15: Excellent - model behavior

---

## Error Taxonomy

Categorize failures to identify patterns and prioritize fixes.

### Category 1: Init Failures
- Package directory already exists
- Invalid package name
- Missing dependencies

### Category 2: Code Generation Failures
- Invalid Python syntax
- Missing imports
- Wrong AWS module usage
- Circular dependencies

### Category 3: Lint Loop Failures
- Same issue reported multiple cycles
- Fix introduces new issue
- Max cycles reached with issues remaining

### Category 4: Semantic Failures
- Wrong resources for the use case
- Missing critical resources (e.g., IAM for Lambda)
- Incorrect resource relationships

### Category 5: Validation Failures
- Template builds but cfn-lint fails
- AWS validate-template fails
- Resources reference non-existent items

---

## Baseline Tracking

Track metrics over time to measure framework improvements.

### Weekly Metrics
```
Week | Prompts | Completion % | Avg Cycles | Avg Questions | Framework Gaps
-----|---------|--------------|------------|---------------|---------------
W1   | 10      | 60%          | 2.4        | 2.1           | 8
W2   | 10      | 70%          | 2.1        | 1.8           | 5
W3   | 10      | 80%          | 1.8        | 1.5           | 3
```

### Regression Detection
- Run same 10 prompts after each framework change
- Alert if completion rate drops >10%
- Alert if avg cycles increases >0.5

---

## Success Metrics

- **Completion Rate**: % of sessions that produce a valid, lint-free package
- **Cycle Efficiency**: Average number of lint cycles needed
- **Question Frequency**: Number of clarifications needed per session
- **Framework Gaps**: Number of improvement suggestions generated
- **Validation Pass Rate**: % of completed packages that pass cfn-lint
- **Score Distribution**: Histogram of rubric scores across prompts
