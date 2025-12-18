import os
from dotenv import load_dotenv
import base64
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st

load_dotenv() 

# OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
# Initialize client (API key is read from env variable)
client = OpenAI(api_key=OPENAI_API_KEY)


def encode_image(image):
    if hasattr(image, "read"):  # uploaded file
        return base64.b64encode(image.read()).decode("utf-8")
    else:  # file path
        with open(image, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
        
# Convert the Swimlane image to structured json
def convert_swimlane_to_json(encoded_image: str, model):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert at converting swim lane diagrams into structured workflows.\n"
                    "Extract both actions and conditional decision points.\n"
                    "Return valid JSON only."
                )
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Analyze this swim lane diagram and extract a step-by-step workflow:\n"
                            "- Include actors (swim lanes) and their actions.\n"
                            "- Include conditional decision points with 'yes' and 'no' branches.\n"
                            "- Preserve the order of steps.\n\n"
                            "Return JSON in this format:\n"
                            "[\n"
                            '  {"step": 1, "actor": "ActorName", "action": "Action performed"},\n'
                            '  {"step": 2, "condition": "Condition text?", "yes": "Next step if yes", "no": "Next step if no"}\n'
                            "]\n"
                            "Only return valid JSON."
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_image}"
                        }
                    }
                ]
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content

def chat_node(user_input, chatmodel, swimlane_json, chat_history):
    llm = ChatOpenAI(model_name=chatmodel)
    messages = []
    messages.append(
        SystemMessage(
            content=(
                "You are a domain-specific chatbot assistant.\n"
                "Answer questions only using the swimlane workflow json below.\n"
                "If a question is outside the workflow, mention that questions is out of context and then answer except it is greeting like hi, hello messages.\n\n"
                f"Swimlane Workflow:\n{swimlane_json}"
            )
        )
    )
    if chat_history is not None:
        for conv in chat_history:
            messages.append(HumanMessage(content=conv["user_input"]))
            messages.append(AIMessage(content=conv["answer"]))
    messages.append(HumanMessage(content=user_input))
    response = llm.invoke(messages)
    return response.content