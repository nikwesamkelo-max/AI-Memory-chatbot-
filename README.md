# AI Memory Chatbot (Python)

## Overview
This project is a simple rule-based chatbot that uses memory and classification to simulate conversation.

It can:
- Recognize user intent (name, emotion, learning, preferences)
- Store memory during conversation
- Respond differently based on context
- Maintain session state

---

## Features
- Intent classification (rule-based NLP)
- Memory system (stores user name, interests, learning topics)
- Emotion tracking
- Interactive command-line chatbot loop

---

## How it works
The chatbot:
1. Reads user input
2. Classifies the message type
3. Updates memory if needed
4. Generates a contextual response

---

## Example
User: My name is Sam  
Bot: Nice to meet you, Sam!

User: I'm learning Python  
Bot: Got it. I'll remember you're learning python.

---

## Tech Stack
- Python (core logic)
- No external libraries

---

## Future Improvements
- Add AI/NLP library (like spaCy or transformers)
- Improve memory persistence (save to file/database)
- Add web interface
