def chatbot():
    print("Chatbot: Hello! Type 'Bye' to exit.")

    while True:
        user = input("YOU: ").lower()

        if user == "hello":
            print("CHATBOT: Hii!")

        elif user == "how are you" :
            print("CHATBOT: I'm Fine, Thanks!")    
        
        elif user == "what is your name":
            print("CHATBOT: My name is ChatBot.")

        elif user == "what is python":
            print("CHATBOT:Python is a Programming Language")

        elif user == "what is your favorite color" :
            print("CHATBOT:I Like Black colour") 

        elif user == "where do you live":
            print("CHATBOT:I Live Inside Your Computer" ) 

        elif user == "Tell me a joke":
            print("CHATBOT: Why do programers prefer dark mode? Because light attracts bugs!")           

        elif user == "bye":
            print("CHATBOT: GoodBye!")    
            break

        else:
            print("CHATBOT : Sorry , I Don't Understand That.")

chatbot()
