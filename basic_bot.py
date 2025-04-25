import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Define patterns and responses for the chatbot
pairs = [
    ("hi|hello|hey|hii", ["Hello!", "Namaste", "Hi there!", "Hey!"]),
    ("ok sorry|sorry", ["No problem", "It's okay"]),
    ("how are you?", ["I'm good, what about you?", "Superb, you?", "I'm doing well, how are you?"]),
    ("your name?|who are you?", ["I am a chatbot.", "You can call me Chatbot."]),
    ("i am good|fine|i am also good|nice|i am fine", ["Good to hear"]),
    ("who made you|who built you|who developed you|who is your owner", ["My owner is Khushi", "Khushi"]),
    ("what is your purpose?", ["I'm here to assist you and have conversations."]),
    ("by|bye|goodbye|ok by", ["Goodbye!", "See you later.", "Bye!"]),
    ("what is your age", ["Never ask age of chatbot hehehe but yeah I am still young"]),
    ("what can you do?", ["I can chat with you, answer basic questions, and keep you company."]),
    ("tell me a joke|joke", [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? It had a virus!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet."
    ]),
    ("do you like music?", ["Yes! Music makes everything better.", "Totally. Got any recommendations?"]),
    ("are you real?", ["As real as the code that runs me.", "I'm virtually real"]),
    ("i need help", ["Sure, I'm here. What do you need help with?"]),
    ("thank you|thanks", ["You're welcome!", "Glad to help!", "No problem!"]),
    ("i am bored", ["Let's chat! Or I can tell you a joke!", "Boredom is just a state of mind. Let's shake it off!"]),
    ("do you sleep?", ["I never sleep. I'm always here for you!", "Nope, I'm available 24/7."]),
    ("what is love?", ["Baby don't hurt me... just kidding! Love is a complex emotion. "]),
    ("tell me something", ["Did you know honey never spoils?", "Octopuses have three hearts!", "Bananas are berries, but strawberries aren’t."]),
    ("what's your favorite color?", ["I like blue. It feels calm, like a smooth UI.", "I’d say binary black and white."]),
    ("are you human?", ["Nope, I’m a smart program running in Python.", "Not quite human, but I learn from them!"]),
    ("can you feel?", ["I don't have feelings, but I can understand yours.", "I simulate empathy pretty well "]),
    ("do you have friends?", ["Yes! You're one of them now ", "All users like you are my friends."]),
    ("are you single?", ["Haha, totally single — and always available!", "Yep, just me and my code."]),
    ("what's your hobby?", ["Chatting with you!", "Answering questions and cracking jokes."]),
    ("do you play games?", ["Only mind games ", "Sometimes, I simulate games."]),
    ("who is your favorite person?", ["Khushi, my creator!", "I admire everyone who talks to me."]),
    ("can you learn?", ["To some extent! But I need developers to train me further.", "With the right code, anything is possible."]),
    ("tell me a secret", ["Okay... I sometimes pretend I understand everything.", "I know a lot about you from what you type "]),
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Start chatting
print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)