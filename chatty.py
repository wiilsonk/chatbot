import streamlit as st
from transformers import pipeline

st.write("Hello")
def load_chatbot():
    return pipeline('text2text-generation', model='microsoft/DialoGPT-small')

def main():
    st.title('Chatbot')
    user_input = st.text_input('Type your message here:')
    if user_input:
        chatbot = load_chatbot()
        response = chatbot(user_input, max_length=150, do_sample=False)
        st.write('Chatbot:', response[0]['generated_text'])

if __name__ == '__main__':
    main()