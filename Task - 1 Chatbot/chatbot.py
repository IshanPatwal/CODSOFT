def chatbot_response(user_input):
    user_input = user_input.lower()  # converting input to lowercase

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "where are you from" in user_input:
        return "I am from the digital world here to assist you"
    elif "what's your name" in user_input:
        return "I am a chatbot created by Codsoft A.I. intern, Ishan Patwal"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure! I'm here to help. What do you need assistance with?"
    else:
        return "I'm not sure how to respond to that. Could you please rephrase?"

# Main loop to interact with the chatbot
def main():
    print("Welcome to your AI chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
