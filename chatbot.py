memory = {
    "name": None,
    "learning": None,
    "likes": [],
}

session = {
    "emotion": None,
    "problem": None
}


def classify_message(message):
    message = message.lower()

    if "my name is" in message:
        return "set_name"
    elif "i'm learning" in message or "i am learning" in message:
        return "learning"
    elif "i love" in message or "i like" in message:
        return "preference"
    elif "i feel" in message:
        return "emotion"
    elif "problem" in message or "not working" in message:
        return "problem"
    elif "?" in message:
        return "question"
    else:
        return "statement"


def update_memory(category, message):
    global memory, session
    msg = message.lower()

    if category == "set_name":
        name = msg.replace("my name is", "").strip().title()
        memory["name"] = name

    elif category == "learning":
        topic = msg.replace("i'm learning", "").replace("i am learning", "").strip()
        memory["learning"] = topic

    elif category == "preference":
        item = msg.replace("i love", "").replace("i like", "").strip()
        memory["likes"].append(item)

    elif category == "emotion":
        session["emotion"] = msg.replace("i feel", "").strip()

    elif category == "problem":
        session["problem"] = message


def generate_response(category, message):
    name = memory["name"]

    if category == "set_name":
        if name:
            return f"Nice to meet you, {name}!"
        return "Nice to meet you!"

    elif category == "learning":
        return f"Got it. I'll remember you're learning {memory['learning']}."

    elif category == "preference":
        return f"Nice! I'll remember you like {memory['likes'][-1]}."

    elif category == "emotion":
        return "I hear you. Want to talk more about it?"

    elif category == "problem":
        return "Let's try to fix it together."

    elif category == "question":
        if name:
            return f"Let me think about that, {name}."
        return "Let me think about that."

    else:
        return "Tell me more."


# MAIN LOOP
print("Chatbot is running... (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye 👋")
        break

    category = classify_message(user_input)
    update_memory(category, user_input)
    response = generate_response(category, user_input)

    print("Bot:", response)
