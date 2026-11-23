print("Welcome to USTUN ZEKA AI")
print("Version 0.1.0")
print("AI Development Started!")def get_user_message():
    message = input("You: ")
    return message


def main():
    ai = UstunZeka()
    ai.introduce()

    user_message = get_user_message()
    print("Your message:", user_message:",user_message)
if __name__ == "__main__":
    main()
    
def generate_response(self, message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! Welcome to USTUN ZEKA."

    elif "name" in message:
        return f"My name is {self.name}."

    elif "version" in message:
        return f"My version is {self.version}."

    elif "languages" in message:
        return f"My target is {self.languages} languages."

    else:
        return "I am still learning. Please try another question."
        
