import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']],
    ['how are you?', ['I am doing well, thank you!', 'I am great, thanks for asking!']],
    ['what is your name?', ['My name is Chatbot.', 'You can call me Chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'Bye!', 'See you later!']],
    ['default', ['I am not sure I understand.', 'Could you please repeat that?', 'I am a simple chatbot.']],
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

def main():
    print("Welcome! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
