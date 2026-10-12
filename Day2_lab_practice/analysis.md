# Analysis - Smart Agriculture Assistant

## 1. Scenario

This experiment uses a Smart Agriculture Assistant scenario.

The farmer has:

* Tomato: 2 acres, 1200 litres/acre
* Rice: 3 acres, 2000 litres/acre
* Cotton: 1 acre, 1500 litres/acre
* Water-saving method: 15%

The experiment compares Direct Prompting, Step-by-Step Reasoning, ReAct-style tool use, and Self-Consistency.

---

## 2. Direct Prompting

Direct prompting asks the model to provide the final answer directly without detailed calculations.

The calculation is:

```text
Tomato = 2 × 1200 = 2400 litres
Rice = 3 × 2000 = 6000 litres
Cotton = 1 × 1500 = 1500 litres

Total = 2400 + 6000 + 1500
      = 9900 litres

Water saved = 9900 × 0.15
            = 1485 litres

Final requirement = 9900 - 1485
                  = 8415 litres
```

**Final water requirement = 8415 litres**

Direct prompting is useful when a concise answer is sufficient.

---

## 3. Step-by-Step Reasoning

The step-by-step approach asks the model to show the important calculation steps before giving the final answer.

The calculation is:

```text
Tomato = 2 × 1200 = 2400 litres
Rice = 3 × 2000 = 6000 litres
Cotton = 1 × 1500 = 1500 litres

Total = 9900 litres
Saving = 9900 × 15 / 100
       = 1485 litres

Final = 9900 - 1485
      = 8415 litres
```

**Final water requirement = 8415 litres**

This approach makes the calculation easier to inspect.

---

## 4. Comparison

| Aspect       | Direct           | Step-by-Step | ReAct                |
| ------------ | ---------------- | ------------ | -------------------- |
| Explanation  | Short            | Detailed     | Action + observation |
| Tool use     | No               | No           | Yes                  |
| Transparency | Lower            | Higher       | Higher               |
| Speed        | Faster           | More output  | Extra tool steps     |
| Suitable for | Simple questions | Calculations | Tool-based tasks     |

Direct prompting focuses on the final answer.

Step-by-step reasoning focuses on the calculation process.

ReAct combines reasoning with tool interaction.

---

## 5. ReAct and Tool Use

The ReAct experiment uses the `get_crop_water()` function from `day2_tools.py`.

The tool contains:

```text
Tomato → 1200 litres/acre
Rice → 2000 litres/acre
Cotton → 1500 litres/acre
```

The ReAct process is:

```text
Thought → Action → Observation
```

Example:

```text
Action: get_crop_water("tomato")
Observation: 1200 litres/acre
```

The same process is performed for rice and cotton.

The returned values are then used for calculation:

```text
(2 × 1200) + (3 × 2000) + (1 × 1500)
= 9900 litres
```

Then:

```text
9900 × 0.15 = 1485 litres
9900 - 1485 = 8415 litres
```

Therefore:

**Final water requirement = 8415 litres**

This demonstrates how a tool can provide information used in the final calculation.

---

## 6. Self-Consistency

The self-consistency experiment uses this problem:

```text
A college has 120 students.

40% choose Python.
35% choose Java.
The remaining students choose Web Development.
```

The calculation is:

```text
Python = 40% of 120 = 48
Java = 35% of 120 = 42

Web Development
= 120 - 48 - 42
= 30 students
```

**Expected answer = 30 students**

The program runs the problem five times using:

```text
Number of runs = 5
Temperature = 0.8
```

Each response is displayed separately.

Different runs may use different wording while giving the same numerical answer.

The current implementation records and displays the five responses.

It does **not** automatically perform majority voting.

---

## 7. Suitability

### Direct Prompting

Suitable when the required information is already available and only a short answer is needed.

### Step-by-Step Reasoning

Suitable for calculations and multi-step problems where intermediate calculations are useful.

### ReAct

Suitable when information must be obtained from a tool before completing the task.

### Self-Consistency

Suitable for checking whether repeated model runs produce consistent answers.

---

## 8. Reliability and Transparency

Direct prompting provides a concise result but fewer details about the calculation.

Step-by-step reasoning provides intermediate calculations, making the solution easier to inspect.

ReAct provides an action-and-observation trace showing the tool calls and returned values.

Self-consistency repeats the same problem multiple times so that the outputs can be compared.

For the agriculture calculation, the verified numerical results are:

```text
Total water = 9900 litres
Water saved = 1485 litres
Final water = 8415 litres
```

For the self-consistency problem:

```text
Web Development = 30 students
```

---

## 9. Speed and Cost

Direct prompting normally produces less output.

Step-by-step reasoning produces additional calculation information.

ReAct requires tool interactions in addition to the model response.

Self-consistency requires five model executions in this experiment.

Therefore, the methods differ in the amount of processing and output required.

```text
Direct Prompting
→ Single response

Step-by-Step
→ Response + calculations

ReAct
→ Response + tool interaction

Self-Consistency
→ Five model responses
```

---

## 10. Files Used

The Day 2 folder contains:

```text
Day2/
├── day2_tools.py
├── day2_direct.py
├── cot_compare.py
├── react_trace.py
├── self_consistency.py
├── analysis.md
└── screenshots/
```

### day2_tools.py

Contains the `get_crop_water()` function.

### day2_direct.py

Calculates the total water requirement and final requirement.

### cot_compare.py

Compares direct prompting with step-by-step reasoning.

### react_trace.py

Demonstrates the ReAct-style Thought → Action → Observation process.

### self_consistency.py

Runs the reasoning problem five times at temperature 0.8.

### analysis.md

Contains the analysis of the Day 2 experiments.

---

## 11. Overall Observation

The experiments demonstrate four approaches:

**Direct Prompting**

Provides a concise final answer.

**Step-by-Step Reasoning**

Shows important calculation steps.

**ReAct**

Uses a tool to obtain required information before calculating.

**Self-Consistency**

Runs the same problem multiple times to observe consistency.

For the Smart Agriculture scenario:

```text
Tomato = 2400 litres
Rice = 6000 litres
Cotton = 1500 litres

Total = 9900 litres
Saving = 1485 litres
Final = 8415 litres
```

For the self-consistency problem:

```text
Python = 48 students
Java = 42 students
Web Development = 30 students
```

---

## 12. Conclusion

The experiment compares different reasoning and acting approaches for AI tasks.

Direct prompting is simple and concise.

Step-by-step reasoning makes calculations easier to inspect.

ReAct demonstrates interaction between reasoning and tools.

Self-consistency demonstrates repeated model execution for checking consistency.

The main Smart Agriculture result is:

```text
Total water requirement = 9900 litres
Water saved = 1485 litres
Final water requirement = 8415 litres
```

The self-consistency problem has an expected answer of:

```text
30 students
```

These results are obtained from the calculations and outputs of the implemented Day 2 programs.
