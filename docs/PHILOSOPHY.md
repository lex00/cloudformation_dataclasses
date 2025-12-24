# Philosophy: Readable Infrastructure

> **Status:** Draft - refining statements and sources

---

## Core Thesis

Infrastructure code should be readable at every stage—by the "ops" people who write it, the "dev" people who rely on it, and our ai agents that now help maintain it. Every IaC wrapper that loses sight of these things eventually reimplements its substrate badly and evolves into a burden within and across teams.

---

## Part 1: The Current State

### On Write-Only Infrastructure

- Infrastructure code can easily become "write once, run away".  Even when it starts out looking perfect.
- Cloud vendor tooling at its core tends to be serialization formats masquerading as a programming languages.
- Even Terraform can end up looking very different across teams.
- We've accepted that infrastructure is "just complex" instead of asking why our tools make it harder than it needs to be.

### On Tool Sprawl

- Developers manage an average of 14 different tools, and 97% report context switching due to using tools from multiple vendors.
  - *Source: [CD Foundation - State of DevOps 2024](https://cd.foundation/blog/2024/08/15/decoding-real-state-of-devops-2024/)*

- "Despite the great value Terraform and associated IaC tools have brought, DevOps teams are feeling more frustrated than ever."
  - *Source: [The New Stack - Infrastructure as Code in 2024: Why It's Still So Terrible](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/)*

### On Terraform State

- "After two production outages and countless hours debugging state file issues, I'm done with it."
  - *Source: [Medium - Why I Stopped Using Terraform](https://medium.com/@theopinionatedev/why-i-stopped-using-terraform-after-it-took-down-production-twice-ea80e945c096)*

- "Developers often find themselves waiting for Ops to unlock state files or fix 'drift' errors before they can deploy simple changes."
  - *Source: [Qovery - State File Nightmares](https://www.qovery.com/blog/top-10-terraform-cloud-alternatives)*

- State files contain sensitive information in plaintext. State management isn't a feature - it's an operational liability someone has to own forever.

### On CDK's Leaky Abstractions

- "CDK is full of leaky abstractions... when L2 and L3 constructs abstract important details away, forcing you to fall back to using L1 constructs, at which point, you are just writing CloudFormation with extra steps."
  - *Source: [Leo Xiong - AWS CDK: You Can't Polish a Turd](https://leoxiong.com/2024/10/aws-cdk-you-cant-polish-a-turd/)*

- "The CDK's approach of client-side generation of CloudFormation templates is deeply flawed."
  - *Source: [Last Week in AWS - The CDK's Most Fundamental Flaw](https://www.lastweekinaws.com/blog/the-cdks-most-fundamental-flaw-is-fixable/)*

- CDK promises developer-friendly infrastructure, yet can deliver highly verbose templates from simple looking examples.

---

## Part 2: The Complexity Problem

### Rich Hickey on Simplicity

- "We have a culture of complexity. To the extent we all continue to use these tools that have complex outputs, we're just in a rut."
- "Simplicity is a choice. It's your fault if you don't have a simple system."
- "You can make a sophisticated system with simple tools - you can focus on the system, what it's supposed to do, instead of the constructs."
  - *Source: [InfoQ - Simple Made Easy (2011)](https://www.infoq.com/presentations/Simple-Made-Easy/)*

### On Complecting

Hickey's concept of "complecting" - interleaving concerns until they can't be separated - applies directly to IaC:

- CDK complects your infrastructure definition with its abstraction layer
- CloudFormation YAML complects configuration with serialization format
- Terraform complects your infrastructure with state management

### Charity Majors on Operational Complexity

- "Our systems are only getting more complex, more difficult to operate, and simultaneously more critical to life on earth."
- The longer deployment takes, the more engineers you need, leading to the "engineer death spiral."
  - *Source: [charity.wtf](https://charity.wtf/tag/devops/), [The New Stack](https://thenewstack.io/charity-majors-recipe-for-high-performing-teams/)*

### Kelsey Hightower on Invisible Infrastructure

- "If done right, Kubernetes would become invisible and just an implementation detail."
- "Trying to describe your entire infrastructure using a YAML file delivered via Git also becomes more of a kind of a dead end."
- "Whether you like YAML or not, it just doesn't matter... you need to ask for what you want the infrastructure to do."
  - *Source: [CNCF Interview](https://www.cncf.io/blog/2024/01/22/kubernetes-and-beyond-a-year-end-reflection-with-kelsey-hightower/), [Platform Engineering Podcast](https://platformengineeringpod.com/episode/guest-host-kelsey-hightower-are-ci-cd-and-gitops-just-making-things-harder)*

---

## Part 3: Lock-In and Lock-Out

### On Tool Lock-In

- "Full-featured" tools become prisons. The more they do, the harder they are to leave.
- Vendor-specific abstractions are technical debt with a subscription fee.
- The best migration path is the one you never have to take because you weren't locked in.
- Your infrastructure tool shouldn't require a certification to understand.

### On Developer Lock-Out

- When only two people on the team can touch deployments, you don't have DevOps - you have a new silo.
- The "us vs. them" between dev and ops exists because our tools enforce it.
- Developers should be able to read, modify, and deploy their own infrastructure.
- Code review should work for infrastructure the same way it works for application code.

### On Imperative Divergence

- Imperative ops scripts diverge over time. Every person who touches them adds their own style, their own assumptions, their own "temporary" workarounds.
- Many scripts emerge with slightly different AWS CLI invocations. `deploy_prod.sh` vs `deploy-prod-new.sh` vs `deploy_prod_FIXED.sh`.
- Declarative syntax provides a forcing function for consistency.

---

## Part 4: The Agentic Future

### The State of AI + IaC

- "Earlier in 2024, attempts to use LLMs to generate Terraform configurations found results to be unusable, with rampant hallucinations."
- "None of the models produced working configurations in one attempt, often due to incorrect or insufficient IAM policies and security groups."
  - *Source: [ITNEXT - Status of LLM-based Terraform Generation 2024](https://itnext.io/the-status-of-llm-based-terraform-generation-at-the-end-of-2024-e31639068318)*

- "Current large language models can generate syntactically correct Terraform HCL code, but generating deployable, functional Terraform stacks is challenging."
  - *Source: [The New Stack - Can AI Generate Functional Terraform?](https://thenewstack.io/can-ai-generate-functional-terraform/)*

- "AI-generated infrastructure code is frequently invalid, requiring human review for correctness. Code generated by AIs commonly contains security vulnerabilities."
  - *Source: [Styra - AI-Generated IaC: The Good, the Bad and the Ugly](https://www.styra.com/blog/ai-generated-infrastructure-as-code-the-good-the-bad-and-the-ugly/)*


### On Human-Agent Collaboration

- AI agents inherit our tooling choices. If our tools produce illegible output, agents can't help us understand it.
- The best IaC for human-agent collaboration is code that both can read, write, and review.  Declarative infra shines here.
- Type safety isn't just for IDEs anymore - it's how agents know they got it right.

### On Shared Artifacts

- The future of infrastructure isn't "AI writes it for you." It's "AI writes it *with* you." That requires a shared language.
- Human-agent collaboration requires a shared artifact both can read. 2000 lines of generated YAML isn't it.
- When something breaks, you debug it together. That requires legibility.
- Abstractions that hide complexity from humans also hide it from agents.

### The Counter-Argument (Acknowledged)

- Terraform and CloudFormation have more training data today. Agents are statistically "better" at generating them.
- But "better at generating unreadable output" compounds the maintenance problem.
- The question isn't what's easiest for the agent to write. It's what's easiest for the team to own.

---

## Part 5: What We Actually Need

### On Simplicity

- Generate JSON. Deploy with the CLI you already have. That's it.
- No state files. No daemon processes. No control planes to manage.
- The best infrastructure tool is one you can delete and replace.
- If you can't explain how it works to a new hire in 10 minutes, it's too complicated.

### On Readability

- Infrastructure code should be readable by anyone who can read code.
- The gap between "what I wrote" and "what gets deployed" should be zero.
- Ops knowledge shouldn't be tribal. It should be in the codebase, legible.
- If the team can read it, they can own it. If they can't, it becomes the domain of whoever wrote it originally.

### On Python

- A Python dataclass with 5 typed fields is a better prompt than a 50-line YAML example.
- Type hints provide constraints that reduce the search space - for humans, IDEs, and agents.
- The agent doesn't need to know CloudFormation. It needs to know Python. The library handles the translation.

### On CloudFormation

- CloudFormation isn't going anywhere. AWS has 20 years of it. Bet on the substrate, not the tooling.
- The service is fine. The authoring experience is hostile.
- Every IaC wrapper eventually reimplements its substrate badly.
- Don't fight the platform. Make it easier to use correctly.
- Deployment is a solved problem. `aws cloudformation deploy` works. Template authoring isn't solved.

---

## Part 5.5: Why Dataclasses

Python 3.7 introduced [dataclasses](https://peps.python.org/pep-0557/), designed by Eric V. Smith. They've since become the standard way to define structured data in Python.

### The Structural Fit

Dataclasses are not incidentally suited to infrastructure-as-code. They are *structurally* suited to it.

A dataclass is a declaration: "here are the fields, here are their types, here are the defaults." That's exactly what infrastructure configuration is. No ceremony. No framework. Just fields.

```python
@dataclass
class MyBucket:
    bucket_name: str
    versioning: bool = True
```

This *looks* like configuration because it *is* configuration. The code is the spec.

### What Dataclasses Provide

| Feature | Why It Matters for IaC |
|---------|------------------------|
| **Type hints** | Agents, IDEs, and mypy all understand them natively |
| **Default values** | Sensible defaults are obvious, not buried in docs |
| **Inheritance** | Resource specialization maps naturally to class hierarchies |
| **Field metadata** | Clean separation of Python names vs CloudFormation names |
| **`asdict()` serialization** | JSON output is one stdlib call away |
| **Field introspection** | Code generation and validation without reflection hacks |

### Comparison with Alternatives

| Approach | Problem |
|----------|---------|
| **Pydantic** | Validation-first, heavier runtime, more opinionated |
| **attrs** | Predates dataclasses, less stdlib integration |
| **TypedDict** | No methods, no inheritance, just shapes |
| **NamedTuple** | Immutable, awkward defaults, no field metadata |
| **Plain classes** | Boilerplate, no `asdict()`, no introspection |
| **TypeScript interfaces** | Structural typing = less constraint, erased at runtime |
| **Go structs** | No inheritance, verbose field tags, no generics until recently |
| **Java records** | New (Java 16+), ecosystem still catching up |
| **Rust structs** | Great but derive macros are complex, steeper curve |

### The "Just Enough" Principle

Dataclasses give you:
- Type safety
- Default values
- Inheritance
- Serialization
- Field introspection
- IDE autocomplete

Without:
- Runtime validation overhead
- Complex metaclasses
- DSL learning curve
- Framework lock-in

They're the minimum viable abstraction for "typed configuration as code."

### Why This Matters for Agents

A Python dataclass with 5 typed fields is a better prompt than a 50-line YAML example.

The agent doesn't need to learn CloudFormation's schema. It needs to understand a Python class with constrained fields. The library handles the translation to CloudFormation JSON.

Type hints aren't just documentation - they're constraints that reduce the search space for both humans and AI.

### Beyond AWS

This project targets CloudFormation, but the approach isn't AWS-specific.

Azure Resource Manager templates have the same verbosity problem. Google Cloud Deployment Manager has the same YAML fatigue. Every cloud vendor has a declarative format that's hard to read and harder to maintain.

The dataclass pattern could work for any of them:

```python
# Hypothetical Azure example
@dataclass
class MyStorageAccount:
    resource: AzureStorageAccount
    name: str
    sku: StorageSku = StorageSku.STANDARD_LRS
    kind: StorageKind = StorageKind.STORAGE_V2
```

```python
# Hypothetical GCP example
@dataclass
class MyGCSBucket:
    resource: GCSBucket
    name: str
    location: str = "US"
    storage_class: StorageClass = StorageClass.STANDARD
```

The underlying principle is portable: typed Python classes that generate vendor-specific JSON/YAML. The substrate changes, but the authoring experience stays readable.

If this approach proves valuable for CloudFormation, there's no reason it couldn't be extended - or inspire similar projects - for other clouds.

---

## Part 6: Closing

AI coding agents are here. They will write your infrastructure code whether you plan for it or not.

The question is: what artifact do you want to review together?

### The YAML Problem

Reviewing 500 lines of generated YAML is theoretically possible. In practice, it becomes a rubber stamp.

The content is too dense to parse. Every line looks like every other line. The diff tells you what changed, not what it *means*. Team reviews become performative - no one wants to be the person who missed the misconfigured security group buried on line 347.

### The Workflow Problem

Reviewing agent-generated Terraform means understanding not just the HCL, but the state file implications, the plan output, the apply sequence.

Each layer adds cognitive load. The agent doesn't know your state history. "Fixing" agent output often requires understanding the full workflow - and the agent doesn't.

### The Convention Problem

Agents don't know your team's naming conventions. They don't know your module structure. They generate "correct" code that doesn't match your patterns.

Now you have two styles in your codebase: pre-agent and post-agent. The consistency that made your infrastructure maintainable is gone.

### The Alternative

But reviewing a Python dataclass? You see the fields. You see the types. You see what's different from the base class.

The structure carries meaning. The diff is legible. A junior engineer can understand what changed without understanding CloudFormation's entire schema.

### The Point

The future isn't "AI writes infrastructure for you." It's "AI writes infrastructure *with* you."

That requires artifacts both humans and agents can reason about - at every stage of the workflow.

Choose your tools accordingly.
