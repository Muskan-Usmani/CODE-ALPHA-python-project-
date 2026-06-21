def chatbot():
    print("Chatbot: Hello! Type 'Bye' to exit.")

    while True:
        user = input("you: ").lower()

        if user == "hello":
            print("CHATBOT: Hii!")

        elif user == "how are you" :
            print("CHATBOT: I'm Fine, Thanks!")    
        
        elif user == "what is your name":
            print("CHATBOT: My name is ChatBot.")

        elif user == "bye":
            print("CHATBOT: GoodBye!")    
            break

        else:
            print("CHATBOT : Sorry , I Don't Understand That.")

chatbot()
