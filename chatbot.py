def chatbot():

    print("===================================")
    print("      BASIC CHATBOT")
    print("Type 'bye' to exit")
    print("===================================")

    while True:

        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hello! Welcome.")

        elif user == "how are you":
            print("Bot: I'm fine, thank you!")

        elif user == "what is your name":
            print("Bot: I'm CodeAlpha ChatBot.")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()