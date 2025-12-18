🟦 SwimBot

• SwimBot is a Domain-specific chatbot for processing and querying Swimlane diagrams from a development portal.

• SwimBot converts swimlane diagrams into structured JSON and answers client questions about workflows using AI models.


🌐 Access the App:

    https://swimbot.streamlit.app/

📌 Background

• SwimBot was developed as part of a assessment for a Development Portal chatbot. 


🛠️ Features

📷 Swimlane Processing:

• Upload a new swimlane image or select an existing image from the dropdown. Convert diagrams into structured JSON representing workflow sequences.

💬 AI Chat:

• Ask questions about workflow sequences from swimlane diagrams. Supports multiple OpenAI models for performance optimization.

🔄 Session Management:

• Maintains chat history and allows one-click session clearing.

⚙️ Model Options:

• Image models: gpt-4o, gpt-4.1

• Chat models: gpt-4o, gpt-4.1, gpt-4.1-mini, gpt-3.5-turbo, gpt-3.5-turbo-16k

🔑 Environment Configuration:

• Supports .env files locally or Streamlit Cloud secrets.toml for OpenAI API key management.


🚀 How It Works

1️⃣ Upload / Select Image:

• Upload a new swimlane diagram or select an existing one.

2️⃣ Process Diagram:

• Click Process Swimlane Image to convert it into structured JSON.

3️⃣ Ask Questions:

• Interact with the chatbot to query workflow events.

• Chat history is displayed in the sidebar.

4️⃣ Clear Session:

• Reset chat and workflow results anytime using the Clear Session button.


⚙️ Installation

• Clone the repository:

    git clone https://github.com/MahavirK1997/Aurus_Assignment.git
    cd Aurus_Assignment

• Create a virtual environment and activate it:

    python -m venv venv
    source venv/bin/activate      # Linux/Mac
    venv\Scripts\activate         # Windows

• Install dependencies:

    pip install -r requirements.txt

• Set OpenAI API Key:

    Local: Create .env in the root folder:
        OPENAI_API_KEY=your_openai_api_key_here
    Streamlit Cloud: Add key in Secrets tab of app settings:
        OPENAI_API_KEY = "your_openai_api_key_here"


🧠 AI Models:

• Image Processing: Converts swimlane diagrams to structured JSON.

• Chat Models: Handles user queries referencing the parsed JSON.

• Recommended Models:

    Image processing:
        High accuracy: gpt-4o
        Cost-efficient: gpt-4.1 (if textual extraction is primary)

    Chat models:
        High accuracy/reasoning: gpt-4.1, gpt-4o
        Cost-efficient: gpt-3.5-turbo, gpt-3.5-turbo-16k


📊 Accuracy & Performance:

• Target: ≥ 90% accuracy in parsing workflow events.

• Conversational AI provides structured responses referencing parsed workflow data.


❗ Notes:

• Ensure .env is not committed to GitHub (add it to .gitignore).

• Streamlit Cloud requires API keys in secrets.toml.

• App works locally and on the cloud seamlessly.


✅ SwimBot simplifies complex workflow diagrams and empowers users to query them intelligently using AI.