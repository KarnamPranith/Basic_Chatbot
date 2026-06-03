print("=== Basic Chatbot ===")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")
    elif user == "how are you":
        print("Bot: I'm fine, thanks!")
    elif user == "what is your name":
        print("Bot: I am a Python Chatbot.")
    elif user == "who created you":
        print("Bot: I was created by Pranith.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand that.")