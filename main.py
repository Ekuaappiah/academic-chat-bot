from config.settings import GOOGLE_API_KEY, YOUTUBE_API_KEY
from core.chatbot import EducationalChatbot
import json

if __name__ == "__main__":
    bot = EducationalChatbot(GOOGLE_API_KEY, YOUTUBE_API_KEY)

    print("Welcome to the Educational Chatbot! Ask me anything.")
    print("Type 'exit' or press Ctrl+C to end the conversation.\n")

    try:
        while True:
            question = input("You: ").strip()
            if question.lower() in {"exit", "quit"}:
                print("Ending conversation. Goodbye!")
                break

            response = bot.chat(question)
            answer_json = json.dumps({"answer": response.answer}, indent=2)
            print(f"\nBot:\n{answer_json}\n")
    except KeyboardInterrupt:
        print("\nConversation interrupted. Goodbye!")

    # print(json.dumps(response.dict(), indent=2))
    # answer_json = json.dumps({"answer": response.answer}, indent=2)
    # print(answer_json)

