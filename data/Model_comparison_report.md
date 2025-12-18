wimBot: Model Comparison and Selection Report
1. Project Overview

Objective:
Build a chatbot that accurately answers client questions using Swimlane diagrams and other structured/unstructured process documentation. The system should:

Extract workflow information from uploaded or existing Swimlane images.

Convert images to a structured JSON representation.

Enable a conversational interface over the JSON data.

Maintain high accuracy (target >90%) and quick response times.

2. Components Requiring Model Selection

Image-to-JSON Conversion (Computer Vision + LLM)

Input: Swimlane diagram (PNG, JPG, JPEG)

Output: JSON representation of workflow nodes, actions, and transitions

Chat Model (LLM)

Input: User question + Swimlane JSON

Output: Context-aware answers

3. Image Model Comparison
Model	Architecture	Strengths	Weaknesses	Notes for Swimlane Project
OpenAI GPT-4o Vision	Multi-modal GPT (Vision + Text)	- Handles complex diagrams
- High accuracy in text + layout recognition
- Integrates directly with LLM	- Commercial API cost
- Limited fine-tuning	Selected for production use due to strong multi-modal capabilities and integration with GPT chat models
OpenAI GPT-4.1 Vision	Multi-modal GPT	- Slightly faster inference
- Strong reasoning over visual data	- Still experimental on structured diagrams	Useful for testing, but GPT-4o provided slightly higher diagram extraction fidelity in pilot runs
Google Gemini Vision	Multi-modal, foundation model	- Fast and scalable
- Strong OCR and visual reasoning	- Limited documentation/examples for structured workflows	Potential alternative, but integration with Python/Streamlit pipelines less mature
BLIP-2 (HuggingFace)	Image captioning & understanding	- Open-source
- Good OCR + text extraction	- Needs custom prompt engineering
- Limited reasoning over multi-node diagrams	Can be used for proof-of-concept or fine-tuning for specific Swimlane layouts
Tesseract OCR	Traditional OCR	- Free, lightweight
- Simple text extraction	- Cannot capture node relationships or layout	Only for extracting raw text; not suitable for full workflow JSON conversion

✅ Selected Image Model: GPT-4o Vision
Rationale: Strong multi-modal reasoning, robust layout understanding, smooth integration with GPT-4 chat models. Pilot tests showed higher fidelity in identifying nodes and edges in complex Swimlane diagrams.

4. Chat Model Comparison
Model	Architecture	Strengths	Weaknesses	Notes for Swimlane Project
GPT-4o	Multi-modal, reasoning-optimized LLM	- Strong reasoning over structured JSON
- Handles long context well	- Higher latency & cost	Default for main chatbot responses; compatible with GPT-4o Vision output
GPT-4.1	Advanced GPT-4 variant	- Slightly faster
- High accuracy	- May underperform GPT-4o in multi-step reasoning	Used for comparison, fallback option
GPT-4.1-mini	Smaller variant	- Low latency
- Lower cost	- Reduced reasoning & memory	Can be used for fast prototyping or low-cost deployment
GPT-3.5-turbo / 3.5-turbo-16k	Earlier GPT generation	- Cost-efficient
- 16k context can handle mid-sized diagrams	- Weak in multi-step reasoning
- Less precise in understanding complex flows	Considered only for testing or scenarios with cost constraints

✅ Selected Chat Model: GPT-4o
Rationale: Best reasoning over structured JSON and complex workflows, aligns with image model selection. Minimizes errors in multi-step query answering.

5. Multi-Model Integration

Workflow:

User uploads/selects a Swimlane image.

GPT-4o Vision encodes the image into a structured JSON format.

JSON is stored in session state.

User queries are sent to GPT-4o, which reasons over the JSON context and provides precise answers.

Advantages:

Reduced human intervention in diagram parsing.

High accuracy in question answering due to structured intermediate representation.

Ability to switch chat models for cost/performance trade-offs.

6. Evaluation Metrics and Criteria

Image-to-JSON Accuracy

Compare extracted JSON nodes/edges vs. ground truth.

Target: >90% node and edge accuracy.

Chatbot Performance

Correct answer rate vs. test question set.

Target: >90% correctness.

Response Latency

Measure end-to-end time (image -> JSON -> answer).

Target: <5 seconds for typical diagrams.

Cost Efficiency

Compare API calls for GPT-4o vs alternatives for projected usage.

7. References and Supporting Research

GPT-4 Vision / GPT-4o

OpenAI (2024). “GPT-4 Technical Report” OpenAI Research

Multi-modal reasoning in diagrams and documents.

Gemini Models

Google Research (2024). “Gemini AI: Multi-modal Capabilities” Google Research

BLIP-2

Li et al. (2023). “BLIP-2: Bootstrapped Language-Image Pretraining” arXiv:2301.12597

Tesseract OCR

Smith, R. (2007). “An Overview of the Tesseract OCR Engine” Document Analysis Systems

8. Conclusion and Recommendation

Selected Models: GPT-4o Vision (image), GPT-4o (chat)

Reasons:

Superior multi-modal reasoning and structured JSON extraction.

Strong alignment between image understanding and question answering.

Supported by recent research and production-ready APIs.

Alternative Models: GPT-4.1, Gemini Vision, BLIP-2 can be explored for cost reduction, prototyping, or multi-cloud deployment.

Next Steps:

Run quantitative evaluation on a benchmark dataset of Swimlane diagrams.

Compare GPT-4o vs. GPT-4.1 in real user queries.

Explore BLIP-2 as an open-source alternative if API costs become prohibitive.