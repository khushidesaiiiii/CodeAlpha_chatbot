import openai
import gradio

openai.api_key = "sk-###your-api-key-here###"
# Replace with your actual OpenAI API key

messages = [{"role": "system", "content": "You are a digital assistant that helps users with various tasks and provides information."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Digital Assistant")

demo.launch(share=True)