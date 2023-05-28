import random

def get_greeting():
    greetings = ["Hello!,Welcome to ShopEasy! ", "Welcome! to ShopEasy!", "Greetings!,Welcome to ShopEasy!"]
    return random.choice(greetings)


def generate_response(user_input):
    
    if "hii" in user_input:
        return "Hello , Hey there"
    elif "product" in user_input:
        return "We have a wide range of products available. How can I assist you in finding a specific product?"
    elif "price" in user_input:
        return "Our prices vary depending on the product. Could you please provide more details so that I can assist you better?"
    elif "delivery" in user_input:
        return "We offer various delivery options. To provide accurate information, could you please provide your location?"
    elif "booking" in user_input:
        return "Sure! I can help you with that. May I know the destination and travel date?"
    elif "account" in user_input:
        return "If you need assistance with your account, please visit our website and go to the account section."
    elif "help" in user_input:
        return "I'm here to help! Please let me know how I can assist you."
    elif "bye" or "quit" in user_input:
        return "Bye! Take care. Have a great day ahead!"
    else:
        return "I'm sorry, but I couldn't understand your request. Could you please rephrase or provide more information?"
    

def main():
    print(get_greeting())
    while True:
        user_input = input("User: ")
        response = generate_response(user_input.lower())
        print("ShopEasy: ",response)

        if "bye" in user_input.lower() or "quit" in user_input.lower():
            print("Thank you for using our chatbot.")
            print("Exiting the program...")
            break
       


if __name__ == "__main__":
    main()