import streamlit as st
from datetime import datetime
from model_inference import chat_query

# Initialize the chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to handle the sending of messages
def send_message():
    user_input = st.session_state.user_input
    
    if user_input:
        # Append user input and bot response to chat history
        st.session_state.chat_history.append({'user': user_input, 'bot': bot_response(user_input)})
        # Clear the input box by resetting the session state value
        st.session_state.user_input = ''

def chat_interface():
    st.title("Chat with AI")

    # Display chat history
    for chat in st.session_state['chat_history']:
        message(chat['user'], is_user=True)
        message(chat['bot'], is_user=False)
    
    # User input area
    st.text_input("You: ", "", key="user_input", on_change=send_message)

def message(text, is_user):
    # Format messages based on the sender
    align = "end" if is_user else "start"
    color = "#cfe3ff" if is_user else "#f0f0f0"
    st.markdown(f"<div style='text-align: {align}; background-color: {color}; padding: 10px; border-radius: 10px; margin: 5px 0;'>{text}</div>", unsafe_allow_html=True)

def bot_response(user_input):
    query_res = chat_query(user_input)
    return query_res

if __name__ == "__main__":
    chat_interface()