from src.services.chatbot import ChatBot


def main():
    bot = ChatBot()

    test_questions = [
        "What's the difference between Widget B and C?",
        "How much does Widget A cost?",
        "Tell me about your company mascot",
        "Why is the sky blue?",  # Not in knowledge base
    ]

    for question in test_questions:
        print(f"Q: {question}")
        print(f"A: {bot.answer_question(question)}\n")
        print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
