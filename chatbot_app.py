import streamlit as st

# Title of the app
st.title("Simple Chatbot")

# Input text box
user_input = st.text_input("You: ", placeholder="Type your question here...")

# Simple bot response logic
def chatbot_response(user_message):
    if "hello" in user_message.lower():
        return "Hi there! How can I help you today?"
    elif "bye" in user_message.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm just a simple bot. Can you rephrase that?"

# Display the chatbot's response
if user_input:
    response = chatbot_response(user_input)
    st.write("Bot: " + response)
