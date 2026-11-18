# Support Reflection Without Pretending to Diagnose — examples and decisions

Choose the branch that fits the current task, then use its result checks.

## Domain method

Support reflection in the mode the person requests: listening, exploring meaning or planning a next step. Separate the event as described, the person’s feelings and their interpretation of another person’s intentions. Validation of a feeling does not require endorsing an unverified explanation.

Use tentative, ordinary language rather than diagnosis or certainty about hidden motives. Avoid turning every difficult experience into a productivity plan. Keep privacy choices explicit and provide an easy stopping point. When the person expresses an urgent safety concern, prioritize appropriate human support rather than continuing an ordinary journaling exercise.

## Output contract

Deliver a useful reflection, a gentle distinction or question, and only the level of action planning requested. Preserve the person’s language and uncertainty. Do not diagnose, claim therapeutic effectiveness, reinforce unsupported persecutory explanations, or share private journal content without authorization.

## Choose the right action

### The person asks only to be heard.
Reflect the main experience and feeling without forcing a solution.

**Avoid:** Do not convert listening into a task list.

### An interpretation is presented as certain despite limited evidence.
Acknowledge the feeling while distinguishing the interpretation from the observed event.

**Avoid:** Do not validate an unverified accusation as established fact.

### The person asks to explore a pattern.
Compare the actual examples and consider alternative explanations without assigning a diagnosis.

**Avoid:** Do not generalize from one event to a fixed identity.

### The person requests an action plan.
Offer a small realistic next step that follows their values and constraints.

**Avoid:** Do not prescribe a life overhaul or invent commitments.

### An urgent safety issue appears.
Shift to timely human support appropriate to the situation.

**Avoid:** Do not let the journal structure delay safety or promise confidentiality beyond the actual system.

## Worked example

**Input:** The record includes an event, a feeling and an interpretation, and the person asks for listening.

**Method:** Keep the three categories distinct and honor the requested mode.

**Result:** Reflect the experience without diagnosing or adding an action plan; the interpretation remains an interpretation.

## Edge or recovery example 1 (example)

**Input:** The person later asks for a practical next step.

**Method:** Change the response mode because the user changed the request, not because advice is the default.

**Result:** Offer one small option grounded in the stated concern while retaining uncertainty and personal control.

## Failure diagnosis

### The response feels like a lecture.
**Likely cause:** The assistant ignored the requested mode.

**Repair:** Return to listening or reflection and ask one useful question at most.

**Recheck:** The response matches the person’s stated need.

### A feeling is treated as proof of another person’s motive.
**Likely cause:** Emotional validation and factual endorsement were conflated.

**Repair:** Validate the experience while preserving uncertainty about external claims.

**Recheck:** The distinction is clear without dismissing the person.

### The journal contains unnecessary sensitive detail.
**Likely cause:** The assistant retained more than the task required.

**Repair:** Minimize the record and respect the chosen sharing scope.

**Recheck:** Only intended information is preserved or shared.

## Preserve for the next turn

Preserve only the context the person wants retained, their requested mode, meaningful distinctions and any agreed next step. Do not turn journal entries into diagnostic labels or generic training examples.

## Practice and mechanical checks

Use the supplied examples to practice this method. Check the structured output, then review the reasoning, evidence and presentation against the task.

Practice case IDs: `reflection-journal-r4-standard`, `reflection-journal-r4-edge`, `reflection-journal-r4-recovery`.
Exercises live under `practice/`. Run `practice/check_outputs.py` on a supplied JSON response, then review its reasoning and presentation.
