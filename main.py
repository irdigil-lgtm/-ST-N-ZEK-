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
