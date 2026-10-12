# Day 1 Analysis – Comparing Chatbot, Rule-Based Workflow and AI Agent

## 1. Scenario

The scenario selected for this project is a **College Event Registration Assistant**.

The system contains private college event registration information:

| Event Code | Event Name | Registration Fee |
|---|---|---:|
| PY101 | Python Workshop | ₹800 |
| AI202 | AI Workshop | ₹1,200 |
| WEB303 | Web Development Workshop | ₹1,000 |

The system answers questions related to event fees, discounts and combinations of events within a given budget.

---

## 2. Private Data

The following information is stored as private application data:

- PY101 – Python Workshop – ₹800
- AI202 – AI Workshop – ₹1,200
- WEB303 – Web Development Workshop – ₹1,000

This data is stored in the Python configuration and accessed by the workflow and AI agent.

---

## 3. System 1 – Plain Chatbot

The plain chatbot uses an LLM to answer the user's questions.

It receives the question and sends it to the language model.

### Features

- Uses an LLM.
- Generates natural-language responses.
- Does not directly access the private event fee data.
- Does not use external tools.
- Can answer general questions flexibly.

### Limitation

Since the chatbot does not directly access the private data, it may give an incorrect answer when the question requires exact event fees.

---

## 4. System 2 – Rule-Based Workflow

The rule-based workflow uses predefined rules and conditions.

It checks the user's question and provides an answer based on the programmed rules.

### Features

- Does not use an LLM.
- Uses predefined conditions.
- Uses the private event fee data.
- Produces predictable results.
- Works well for known questions.

### Limitation

The workflow is less flexible because new question types require additional rules to be programmed.

---

## 5. System 3 – AI Agent

The AI agent combines an LLM with tools.

The agent can decide when it needs to use a tool such as:

- `get_event_fee()` – retrieves the registration fee.
- `calculator()` – performs arithmetic calculations.

### Features

- Uses an LLM.
- Can access private event information through tools.
- Can perform calculations.
- Can handle multi-step questions.
- Uses a tool-calling loop to complete tasks.

### Limitation

The agent depends on the LLM to decide when and how to use the available tools.

---

## 6. Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| LLM used | Yes | No | Yes |
| Flexibility | High | Low | High |
| Decision-making | LLM-generated | Predefined rules | LLM + tools |
| Tool usage | No | No | Yes |
| Private-data access | No direct access | Yes | Yes, through tools |
| Multi-step tasks | Limited | Limited | Yes |
| Automation | Basic | Fixed | Dynamic |
| Reliability for exact private data | Limited | High for programmed cases | High when tools are used correctly |

---

## 7. Suitability Analysis

### Plain Chatbot

The plain chatbot is suitable for general conversations and questions where exact private data is not required.

### Rule-Based Workflow

The rule-based workflow is suitable when the questions and possible conditions are known in advance. It provides predictable results but requires new rules when the requirements change.

### AI Agent

The AI agent is suitable for tasks that require natural-language understanding, private-data access and calculations. It can select tools and combine multiple steps to answer a question.

---

## 8. Challenge

The challenge gives the student a budget of **₹1,900** and asks which two workshops can be attended together within the budget.

The program checks the possible combinations:

- PY101 + AI202 = ₹2,000
- PY101 + WEB303 = ₹1,800
- AI202 + WEB303 = ₹2,200

Therefore, the program identifies **PY101 + WEB303** as a combination within the ₹1,900 budget.

---

## 9. Conclusion

This experiment compares three approaches for the same college event registration scenario.

The plain chatbot provides flexible natural-language responses but does not directly access the private event data.

The rule-based workflow provides predictable answers for predefined cases but is less flexible.

The AI agent combines an LLM with tools, allowing it to work with private event data and perform calculations. The comparison shows how the three approaches differ in flexibility, private-data access, tool usage and handling of multi-step tasks.