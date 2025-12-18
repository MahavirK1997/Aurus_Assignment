🟦  SwimBot: Model Comparison & Selection Report

 ---

1️⃣ Project Overview

• Objective: Build a chatbot that can:

• Extract workflows from Swimlane diagrams 

• Convert diagrams into structured JSON 

• Answer user questions based on JSON context 

• Achieve >90% accuracy with low response latency

---

2️⃣ Components Requiring Model Selection:

    | Component	       | Input	                           | Output                                         |
    | ---------------- | --------------------------------- | ---------------------------------------------- |
    | Image-to-JSON	   | Swimlane diagram (PNG, JPG, JPEG) | Structured JSON of nodes, actions, transitions |
    | Chat Model (LLM) |User question + Swimlane JSON	   | Context-aware answers                          |


---

3️⃣ Image Model Comparison:

    | Model	         | Strengths ✅                      | Weaknesses ⚠️	          | Notes 📝                     |
    | -------------- | --------------------------------- | ------------------------ | ----------------------------- |
    | GPT-4o Vision	 | High accuracy in layout & text    | High API cost;           | Best for production; directly |
    |                | recognition; Excellent reasoning	 | Limited fine-tuning	    | integrates with GPT chat      |
    | GPT-4.1 Vision | Slightly faster inference; 	     | Experimental on complex  | Good for testing or fallback  |
    |                | Strong reasoning                  | diagrams                 |                               |
    | Gemini Vision  |	Fast & scalable; Strong OCR 	 | Limited Python/Streamlit | Potential alternative for     |
    |                | & visual reasoning                | examples                 | prototyping                   |

✅ Selected: GPT-4o Vision

Rationale: Superior multi-modal reasoning, robust diagram understanding, seamless integration with GPT chat models.

--

4️⃣ Chat Model Comparison 💬

    | Model	        | Strengths ✅                             | Weaknesses ⚠️             | Notes 📝                         |
    | ------------- | ----------------------------------------- | ------------------------- | -------------------------------- |
    | GPT-4o	    | Excellent reasoning over structured JSON; | High latency & cost       | Default choice for high accuracy |
    |               | Handles multi-step queries                |                           |                                  |
    | GPT-4.1	    | Slightly faster; High accuracy	        | Slightly weaker reasoning | Fallback option                  |
    | LLaMA-2-13B	| Open-source; Cost-efficient	            | Less reasoning & context 	| Good for prototyping or low-cost |
    |               |                                           | handling                  | deployment                       |
    | LLaMA-2-7B	| Lightweight; Fast	                        | Weaker reasoning & multi- | Useful for rapid prototyping or  |
    |               |                                           | step capabilities         | smaller deployments              |

✅ Selected: GPT-4o

Rationale: Best alignment with GPT-4o Vision output, high reasoning over structured JSON, minimizes multi-step errors.

---

5️⃣ Multi-Model Workflow 🔄

• User uploads/selects Swimlane image 

• GPT-4o Vision encodes image → JSON 

•  JSON stored in session state 

•  User query → GPT-4o → Answer based on JSON 

Advantages:

• Reduced manual diagram parsing

• High accuracy question answering

• Flexibility to switch models for cost/performance

---

6️⃣ Evaluation Metrics 📊

    | Metric	             | Target                                        | 
    | Image-to-JSON Accuracy | >90% nodes/edges                              |
    | Chatbot Correctness    | >90% answers                                  |
    | Response Latency       | <5 seconds                                    |
    | Cost Efficiency	     | Minimize API usage while maintaining accuracy |

---

7️⃣ References 📚

• GPT-4 Vision / GPT-4o – OpenAI (2024), GPT-4 Technical Report : 

    https://openai.com/contributions/gpt-4v/
    https://arxiv.org/abs/2303.08774

• Gemini Models – Google Research (2024), Gemini AI Multi-modal Capabilities : 

    https://en.wikipedia.org/wiki/Gemini_%28language_model%29

• LLaMA-2 – Meta AI (2023), LLaMA-2: Open-Source LLMs : 

    https://ai.meta.com/research/publications/llama-2-open-foundation-and-fine-tuned-chat-models/

• Comparative analysis of LLMs, GPT-4 vs Gemini: 
    https://share.google/Bj9Z0K9TJrzCkI7qX

• LangChain Documentation (Docs) — Developer documentation and guides: 

    https://docs.langchain.com/

• Swimlane Diagram Templates (Venngage) — Examples and templates for swimlane diagrams: 

    https://venngage.com/blog/swimlane-templates/

---

8️⃣ Conclusion & Recommendation ✅

• Selected Models: GPT-4o Vision (image), GPT-4o (chat)

Reasons:

• Best multi-modal reasoning & JSON extraction

• Strong alignment between diagram understanding and chat reasoning

• Production-ready APIs with high accuracy

Next Steps:

• Benchmark GPT-4o vs GPT-4.1 on sample Swimlane diagrams

• Test LLaMA models for cost-efficient prototyping

• Explore Gemini Vision for multi-cloud deployment or scaling

---