# Importing the required modules for the program working
import gradio as gr
import openai
from train import messages

# Putting the API Key for nlp processing
openai.api_key = "PASTE_THE_API_KEY"



# Define a function to interact with the ChatGPT model
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# This part is for showing the chats on the chatting box and again doing it by appending the chats
def respond(message, chat_history):
    bot_message = CustomChatGPT(message)
    chat_history.append((message, bot_message))
    return "", chat_history

# Create a Gradio chatbot interface
with gr.Blocks(title="InfoMe",css=".gradio-container {background-color: #36454F}",theme=gr.themes.Default()) as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Enter Your Query.....")
    clear = gr.ClearButton([msg, chatbot])

    # Connect the chatbot's input to CustomChatGPT
    msg.submit(respond, [msg, chatbot],[msg, chatbot])

# Launching to the Web Browser(Now Demo)
demo.launch()
