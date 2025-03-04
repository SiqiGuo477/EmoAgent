import openai
import os
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create OpenAI client (New API Format)
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = client.chat.completions.create(  # New API method
            model="gpt-4o",
            messages=[{"role": "user", "content": user_input}]
        )

        print("Chatbot:", response.choices[0].message.content)

if __name__ == "__main__":
    chatbot()
