# This is a simple chatbot that can reply to basic user inputs

# Define a dictionary with common user inputs and chatbot responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great! 😊",
    "bye": "Goodbye! Have a nice day!",
    "help": "Sure! You can ask me anything about weather, time, or general questions.",
    "what is your name": "I'm a chatbot created using Python.",
    "thanks": "You're welcome! 😊",
    
}

# Function to get a response from the chatbot
def get_bot_response(user_input):
    # Convert input to lowercase to make matching easier
    user_input = user_input.lower()

    # Check if the input is in the known responses
    if user_input in responses:
        return responses[user_input]
    else:
        # Default reply if the chatbot doesn't understand the input
        return "I'm not sure how to respond to that. Try asking something else!"

# Start the chatbot
print("🤖 Hello! I am your friendly chatbot.")
print("Type 'bye' to end the conversation.\n")

# Use a loop to keep the conversation going
while True:
    # Take user input
    user_input = input("You: ")

    # If the user types 'bye', end the chat
    if user_input.lower() == "bye":
        print("Bot: " + responses["bye"])
        break

    # Get and print the chatbot's response
    bot_reply = get_bot_response(user_input)
    print("Bot:", bot_reply)
