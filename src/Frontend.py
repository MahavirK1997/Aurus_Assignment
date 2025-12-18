import streamlit as st
from PIL import Image
from Backend import encode_image, convert_swimlane_to_json, chat_node

st.markdown(
    "<h1 style='text-align: center; color: #1E90FF;'>SwimBot</h1>",
    unsafe_allow_html=True
)

# Creating variables in session state 
if "Chat_History" not in st.session_state:
    st.session_state.Chat_History = [] 
if "Swimflow_json" not in st.session_state:
    st.session_state.Swimflow_json = None
if "active_image_source" not in st.session_state:
    st.session_state.active_image_source = None
if "active_image" not in st.session_state:
    st.session_state.active_image = None
if "previous_image_option" not in st.session_state:
    st.session_state.previous_image_option = None

# Input Image 
image_option = st.radio(label="Select Image Option:", 
                        options=["Upload New Image", "Select Existing Image"], 
                        index=0, horizontal=True)

# Clearing session state if change in image 
if st.session_state.previous_image_option != image_option:
    st.session_state.Chat_History = []
    st.session_state.Swimflow_json = None
    st.session_state.previous_image_option = image_option

# Image options for selection or uploading the image
if image_option == "Select Existing Image":
    selected_file = st.selectbox(
        "Select Swimlane Image from Dropdown:",
        options=["data/Aurus_Swimlane.png", 
                "data/Swimlane_1.png", "data/Swimlane_2.png", "data/Swimlane_3.png"],
        index=None,
        placeholder="Select Image",
    )
    if selected_file is not None:
        st.session_state.active_image_source = "select"
        st.session_state.active_image = selected_file
    if st.session_state.active_image_source == "select":
        image = Image.open(st.session_state.active_image)
        st.image(
            image,
            caption="Selected Swimlane Image",
            width='content'
        )
elif image_option == "Upload New Image":
    uploaded_file = st.file_uploader(
        "Upload New Swimlane Image",
        type=["png", "jpg", "jpeg"]
        )
    if uploaded_file is not None:
        st.session_state.active_image_source = "upload"
        st.session_state.active_image = uploaded_file
    if st.session_state.active_image_source == "upload":
        st.image(
            st.session_state.active_image,
            caption="Uploaded Swimlane Image",
            width='content'
        )

# Model selection for image processing
model = st.sidebar.selectbox(
    "Image Model:",
    options=["gpt-4o", "gpt-4.1"],
    index=0
)

# Process Swimlane image to json 
if st.button("Process Swimlane Image"):
    st.session_state.Chat_History = []
    if st.session_state.active_image is None:
        st.error("Please upload or select a Swimlane Image")
    else:
        if st.session_state.active_image_source == "upload" or st.session_state.active_image_source == "select":
            encoded_image = encode_image(st.session_state.active_image)
        output = convert_swimlane_to_json(encoded_image, model)
        st.session_state.Swimflow_json = output

# Chat Model selection for chatbot
chatmodel = st.sidebar.selectbox(
    "Chat Model:",
    options=["gpt-4o", "gpt-4.1", "gpt-4.1-mini", "gpt-3.5-turbo", "gpt-3.5-turbo-16k"],
    index=0
)

# Clear session button on sidebar 
st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
with st.sidebar:
    if st.button("Clear Session"):
        st.session_state.Chat_History = []
        st.rerun()

# Header to show json output
if st.session_state.Swimflow_json is not None:
    st.subheader("Swimlane to Json:")
    st.write(st.session_state.Swimflow_json)
    st.subheader("ChatBot:")

# User imput for chatbot
user_input = st.chat_input('Type here')

# Displaying chat history 
if len(st.session_state["Chat_History"])>0:
    for i in range(len(st.session_state["Chat_History"])):
        with st.chat_message('user'):
            st.text(st.session_state["Chat_History"][i]['user_input'])
        with st.chat_message("assistant"):
            st.text(st.session_state["Chat_History"][i]['answer'])

# Access chat node and generate response
if user_input:
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.chat_message('user'):
            st.text(user_input)
        with st.spinner("Fetching answer..."):
            final_answer = chat_node(user_input, chatmodel, st.session_state.Swimflow_json, st.session_state.Chat_History)
            with st.chat_message("assistant"):
                st.text(final_answer)

            # Save conversation
            st.session_state["Chat_History"].append({
                "user_input": user_input,
                "answer": final_answer,
            })
