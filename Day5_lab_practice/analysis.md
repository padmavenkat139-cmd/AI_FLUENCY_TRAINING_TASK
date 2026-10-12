# Day 5 Lab Analysis — Groq API

## 1. Objective

To test LLM API responses, streaming, prompt instructions, and response time using Groq.

## 2. API Demo Results

- Provider: Groq
- Model: `openai/gpt-oss-120b`
- Non-streaming response time: 1.033 seconds
- Streaming time to first token (TTFT): 0.528 seconds
- Total streaming time: 1.043 seconds
- Streaming characters received: 870

## 3. Benchmark Results

| Test | Response time |
|---|---:|
| Variable explanation | 1.277 seconds |
| Rules test | 0.849 seconds |
| Repeated prompt | 1.445 seconds |

The model explained Python variables, answered a question about Python lists, and generated an answer for a repeated prompt.

The rules test instructed the model to explain a Python list in exactly two sentences without bullet points. The returned answer followed that format.

Generation speed and model load time were not reported by this benchmark script.

## 4. Prompt Override Results

- System prompt: Act as a beginner-friendly Python tutor.
- User prompt: Explain Python variables in simple English.
- Response time: 0.79 seconds.
- Result: The model returned a beginner-friendly explanation with Python examples.

## 5. Observations

1. Non-streaming returns the completed response.
2. Streaming displays the response progressively.
3. TTFT measures the time until the first response content arrives.
4. System prompts guide the model's role and response style.
5. Response times vary between requests.

## 6. Conclusion

The Groq API integration worked successfully in all three scripts. Streaming, response-time measurement, benchmark prompts, and system-prompt customization were tested.

## 7. Limitation

This practical used Groq's hosted API. Local Ollama model execution and quantization experiments were not performed.
