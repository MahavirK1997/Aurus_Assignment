🟦 SwimBot

Domain-specific chatbot for processing and querying swimlane diagrams from a development portal.

SwimBot converts swimlane diagrams into structured JSON and answers client questions about workflows using AI models.

📌 Background

SwimBot was developed as part of a client requirement for a Development Portal chatbot. The portal contains multiple types of data:

📝 Structured and unstructured text

🖼️ Graphics, including swimlane diagrams

🔗 OpenAPI 3.0 specifications

The chatbot parses and understands these data formats with high accuracy (target ≥ 90%).

🛠️ Features

📷 Swimlane Processing:
Upload a new swimlane image or select an existing image from the dropdown. Convert diagrams into structured JSON representing workflow sequences.

💬 AI Chat:
Ask questions about workflow sequences from swimlane diagrams. Supports multiple OpenAI models for performance optimization.

🔄 Session Management:
Maintains chat history and allows one-click session clearing.

⚙️ Model Options:

Image models: gpt-4o, gpt-4.1

Chat models: gpt-4o, gpt-4.1, gpt-4.1-mini, gpt-3.5-turbo, gpt-3.5-turbo-16k

🔑 Environment Configuration:
Supports .env files locally or Streamlit Cloud secrets.toml for OpenAI API key management.

📁 File Structure
Aurus_Assignment/
├── data/
│   ├── Aurus_Swimlane.png
│   ├── Swimlane_1.png
│   ├── Swimlane_2.png
│   └── Swimlane_3.png
├── src/
│   ├── Backend.py        # Core processing and AI integration
│   └── Frontend.py       # Streamlit interface
├── .gitignore
├── requirements.txt
├── README.md
└── .streamlit/secrets.toml  # For API keys on Streamlit Cloud

🚀 How It Works

1️⃣ Upload / Select Image

Upload a new swimlane diagram or select an existing one.

2️⃣ Process Diagram

Click Process Swimlane Image to convert it into structured JSON.

3️⃣ Ask Questions

Interact with the chatbot to query workflow events.

Chat history is displayed in the sidebar.

4️⃣ Clear Session

Reset chat and workflow results anytime using the Clear Session button.

⚙️ Installation

Clone the repository:

git clone https://github.com/MahavirK1997/Aurus_Assignment.git
cd Aurus_Assignment


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows


Install dependencies:

pip install -r requirements.txt


Set OpenAI API Key:

Local: Create .env in the root folder:

OPENAI_API_KEY=your_openai_api_key_here


Streamlit Cloud: Add key in Secrets tab of app settings:

[general]
OPENAI_API_KEY = "your_openai_api_key_here"

🧠 AI Models

Image Processing: Converts swimlane diagrams to structured JSON.

Chat Models: Handles user queries referencing the parsed JSON.

Recommended Models:

High accuracy: gpt-4o or gpt-4.1

Cost-efficient: gpt-3.5-turbo

📊 Accuracy & Performance

Target: ≥ 90% accuracy in parsing workflow events.

Conversational AI provides structured responses referencing parsed workflow data.

💡 Future Improvements

Add support for OpenAPI 3.0 workflow diagrams.

Incorporate OCR for scanned or hand-drawn swimlane diagrams.

Extend chatbot to handle other graphics and text from the portal.

❗ Notes

Ensure .env is not committed to GitHub (add it to .gitignore).

Streamlit Cloud requires API keys in secrets.toml.

App works locally and on the cloud seamlessly.

✅ SwimBot simplifies complex workflow diagrams and empowers users to query them intelligently using AI.