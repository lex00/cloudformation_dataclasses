# TODO

Notes and future enhancement ideas for cloudformation_dataclasses.

## cfn-dataclasses-lint CLI

**Decision**: Not adding a separate `cfn-dataclasses-lint` CLI at this time.

**Rationale**:
- Linter is already integrated into `cfn-dataclasses-import` via `--lint`/`--no-lint` flags
- Linter is available programmatically via `lint_code()`, `fix_code()`, `LintChecker`, etc.
- For hand-written code, developers should use type-safe constants from the start (which is the whole point of this library)
- The primary use case for linting is imported code, which `cfn-dataclasses-import` already handles

**Revisit if**:
- There's user demand for a standalone lint command
- A use case emerges for linting code outside the import workflow

## Future Enhancements

### Documentation
- API reference documentation (Sphinx/MkDocs)
- Getting started tutorial
- Advanced patterns guide
- Migration guide (from CDK/Troposphere)

### Developer Experience
- Type stubs (.pyi files) for better IDE support
- VS Code extension/snippets

### Code Generator
- **Alexa::ASK support** - The CloudFormation spec includes `Alexa::ASK::Skill` resource which uses a non-standard `Alexa::` prefix instead of `AWS::`. The code generator currently only handles `AWS::` prefixed services. Need to extend generator to support Alexa namespace.

### Advanced Features
- Higher-level constructs (common patterns library)
- boto3 deployment integration
- CloudFormation drift detection
- Resource visualization
