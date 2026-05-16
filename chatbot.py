# Basic Chatbot
# CodeAlpha Internship - Faryal Abro

def chatbot():
    print("=" * 40)
    print("        WELCOME TO CHATBOT!")
    print("=" * 40)
    print("Type 'bye' to exit the chat.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "":
            print("Chatbot: Please say something!\n")

        elif user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi there! How can I help you today?\n")

        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I am doing great, thanks for asking!\n")

        elif user_input in ["what is your name", "what's your name"]:
            print("Chatbot: My name is ChatBot! Nice to meet you!\n")

        elif user_input in ["what can you do", "what do you do"]:
            print("Chatbot: I can have a simple conversation with you!\n")

        elif user_input in ["who made you", "who created you"]:
            print("Chatbot: I was created by Faryal Abro as part of CodeAlpha Internship!\n")

        elif user_input in ["bye", "goodbye", "see you"]:
            print("Chatbot: Goodbye! Have a great day!\n")
            break

        else:
            print("Chatbot: I am sorry, I did not understand that. Can you try again?\n")

chatbot()
