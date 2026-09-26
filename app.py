import os
from datetime import datetime
from dotenv import load_dotenv
from google import genai

load_dotenv()


api_key = os.getenv("API") or os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: API Key nahi mili! Check .env file.")
    exit()

client = genai.Client(api_key=api_key)


chat = client.chats.create(model="gemini-2.5-flash")


def greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning! "
    elif hour < 18:
        return "Good Afternoon! "
    else:
        return "Good Evening! "


def chat_with_gemini(prompt):
    response = chat.send_message(prompt)
    return response.text


if __name__ == "__main__":
    print(greeting())
    print(
        "Gemini AI Chatbot mein aapka swagat hai! (quit likhein band karne ke"
        " liye)\n"
    )

    while True:
        user_input = input("Aap: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "band"):
            print("Bye Bye")
            break
        try:
            reply = chat_with_gemini(user_input)
            print(f"siya: {reply}\n")
        except Exception as e:
            print(f"Error aaya hai: {e}\n")