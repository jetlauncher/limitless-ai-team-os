

## 2026-05-05 01:35:30 +07 — AWS ships agent performance loop + SageMaker model-customization agent skills

**Source links**
- AWS Machine Learning Blog — AgentCore Optimization preview: https://aws.amazon.com/blogs/machine-learning/introducing-the-agent-performance-loop-agentcore-optimization-now-in-preview/
- AWS Machine Learning Blog — SageMaker AI agent-guided model customization: https://aws.amazon.com/blogs/machine-learning/agent-guided-workflows-to-accelerate-model-customization-in-amazon-sagemaker-ai/

**What changed**
- AWS announced **AgentCore Optimization** in preview for Amazon Bedrock AgentCore: recommendations from production traces, offline batch evaluation, and live A/B testing before promotion.
- AWS says the preview targets **system prompts and tool descriptions** for agents deployed on **AgentCore Runtime** using **AgentCore Observability** and **AgentCore Evaluations**; available in regions where AgentCore Evaluations is available.
- AWS also published a SageMaker AI workflow where developers describe a model-customization use case in natural language and coding agents/skills guide data prep, SFT/DPO/RLVR technique selection, LLM-as-judge evaluation, and deployment to Bedrock or SageMaker AI endpoints.

**Why it matters**
- This is a practical sign that production-agent operations are becoming a cloud-platform primitive: traces -> evaluator reward signal -> recommendation -> config bundle -> batch eval -> A/B test -> promotion/rollback.
- It moves agent reliability from manual prompt tweaking toward measurable CI/CD-style release management for prompts, tool descriptions, and eventually broader runtime changes.
- The SageMaker workflow turns model customization into an agent-assisted pipeline, which could shorten the gap between proprietary data and deployable domain models.

**Who should care**
- Founders/operators running customer-facing agents, internal workflow agents, or regulated enterprise automations.
- Teams teaching agent operations, evals, prompt/tool governance, and model customization.
- Limitless Club members building AI service businesses around agent reliability and domain-specific model workflows.

**Recommended action / angle**
- Treat this as the new enterprise-agent ops pattern to teach/test: instrument traces, define evaluator metrics, version prompts/tool descriptions as deployable config, require batch eval, then A/B live traffic before rollout.
- For Limitless, make a short internal checklist: “Does your agent have observability, evals, config versioning, live A/B, and rollback?”
