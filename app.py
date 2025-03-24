import streamlit as st
from api import chat_with_gemini
from ui import render_ui

def main():
    st.set_page_config(page_title="Chatbot", layout="wide")
    render_ui()
    
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    
    for message in st.session_state['messages']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

    user_input = st.chat_input("Your message")
    if user_input:
        st.session_state['messages'].append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            response = chat_with_gemini(user_input)
            st.markdown(response)
            st.session_state['messages'].append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()