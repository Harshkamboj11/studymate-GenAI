import streamlit as st
import os
from dotenv import load_dotenv
from agents.main_agent import process_request

# Load environment variables from the .env file
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(page_title="StudyMate AI", page_icon="📚", layout="centered")

st.title("📚 StudyMate AI")
st.write("Your personal multi-agent study assistant powered by Google Gemini!")

# Alert the user if the API key is missing
if not os.getenv("GEMINI_API_KEY"):
    st.error("⚠️ GEMINI_API_KEY is missing. Please add it to your .env file.")
    st.stop()

# User Input
user_input = st.text_area(
    "What do you want to learn today?", 
    height=150, 
    placeholder="Try typing:\n- 'Summarize the history of Rome'\n- 'Explain quantum computing'\n- 'Give me a quiz on Python lists'"
)

# Submit Button
if st.button("Generate Response", type="primary"):
    if user_input.strip() == "":
        st.warning("Please enter some text to get started.")
    else:
        with st.spinner("Your AI agents are thinking..."):
            # Route the request through the main agent
            result = process_request(user_input)
            
            # Display which agent took the job
            st.info(f"🤖 Routed to: **{result['agent']}**")
            
            # Display the AI's response
            st.markdown("### Response")
            st.write(result['response'])