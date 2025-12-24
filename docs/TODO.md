# Path to 1.0

Target audience: Teams heavily invested in AWS who are at a crossroads with their IaC tooling due to the cumulative people-cost of complexity (state management, abstraction leaks, tooling sprawl).

## Remaining Work

| Priority | Item | Status |
|----------|------|--------|
| 1 | **Migration path documentation** | Not started |
| | How teams adopt alongside existing stacks | |
| | Side-by-side with CDK/Terraform/raw CFN | |
| | Incremental adoption strategy | |
| 2 | **Escape hatch documentation** | Not started |
| | When/how to use raw JSON passthrough | |
| | Handling resources not yet typed | |
| 3 | **Team onboarding playbook** | Not started |
| | "First week" adoption guide | |
| | Not a reference manual—a playbook | |

## Completed

- [x] Comparison doc (COMPARISON.md) - trade-offs vs CDK/Terraform
- [x] Quick Start guide - getting started tutorial
- [x] CLI documentation - init, import, lint
- [x] Multi-file organization patterns
- [x] Philosophy document

## Nice to Have

- Template validation (pre-deploy sanity checks)
- Example repo with realistic multi-stack setup
- Walk an agent through designing a stack based on a blog post
