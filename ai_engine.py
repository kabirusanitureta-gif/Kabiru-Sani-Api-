import json

def load_knowledge():
    try:
        with open("data/knowledge.json", "r") as f:
            return json.load(f)
    except:
        return {}

knowledge = load_knowledge()

def get_answer(question: str):
    q = question.lower().strip()

    if q in knowledge:
        return knowledge[q]

    if "arduino" in q:
        return "Arduino is a microcontroller used for electronics projects."

    if "ai" in q:
        return "AI allows machines to learn and solve problems."

    if "python" in q:
        return "Python is a programming language for AI and web development."

    if "battery" in q:
        return "Battery systems must be monitored for safety and voltage."

    return "Sorry, I don't have enough data yet."
