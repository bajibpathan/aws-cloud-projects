# Phase 4 – Amazon Bedrock Prompt Testing

## Overview

This phase focused on validating the AI behavior **before** integrating Amazon Bedrock into the AWS Lambda function.

Instead of writing application code first, the prompt was designed, tested, and refined using the Amazon Bedrock Playground.

---

## Objectives

- Select a suitable foundation model
- Create the first production prompt
- Test the prompt with realistic resume examples
- Verify that the model improves wording without inventing facts
- Version the prompt for future improvements

---

## Model Selection

**Service:** Amazon Bedrock

**Foundation Model:** Anthropic Claude Sonnet (via Amazon Bedrock)

### Why this model?

- Produces high-quality professional writing
- Excellent instruction following
- Strong reasoning capability
- Well suited for resume enhancement
- Accessible through Amazon Bedrock

---

## Prompt Version

```
prompts/resume-enhancer-v1.txt
```

The prompt instructs the model to:

- Rewrite resume bullets professionally
- Tailor wording to the supplied job description
- Preserve technical terminology
- Never invent technologies, achievements, metrics or responsibilities
- Return only enhanced resume bullets

---

## Test Cases

| Test | Purpose | Result |
|------|---------|--------|
| Cloud Engineer Example | Normal workflow | ✅ Passed |
| Weak Resume Bullets | Improve wording | ✅ Passed |
| Existing Metrics | Preserve supplied numbers | ✅ Passed |
| Ownership Test | Avoid changing "helped" to "led" | ✅ Passed |

---

## Key Observations

- Prompt quality had a greater impact than model configuration.
- Guardrails significantly reduced hallucinations.
- Low temperature produced more consistent resume bullets.
- Explicit output instructions prevented conversational responses.

---

## Lessons Learned

- Prompt engineering is a core part of GenAI application development.
- AI should improve communication—not invent experience.
- A well-tested prompt should exist before application integration.

---

## Deliverables

- Prompt Version 1
- Prompt test cases
- Model selection completed
- Bedrock Playground validation completed

---

## Next Phase

**Phase 5 – Lambda and Amazon Bedrock Integration**

The validated prompt will be integrated into the Lambda function using the Amazon Bedrock Converse API.
