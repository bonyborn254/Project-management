import random
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi, how can I help you?"]],
    [r"how are you", ["I'm just a bot, but I'm doing great! How about you?"]],
    [r"(.*) your name", ["I'm a simple chatbot created for this session!", "Call me ChatBot!"]],
    [r"quit", ["Goodbye! Have a great day ahead!"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I am your chatbot. Type 'quit' to exit.")
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":
    start_chat()