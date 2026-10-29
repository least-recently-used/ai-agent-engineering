from openai import OpenAI
from dotenv import load_dotenv
import os
#Load config
load_dotenv()

#Create AI client

client= OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

print("="*40)
print(".  My AI Assistant")
print("="*40)

roles = {
    "1": "You are a Travel guide AI assistant. You provide information about travel destinations, tips, and recommendations. give answer in 3 lines.",
    "2": "You are a teacher AI assistant. You provide information about various subjects, answer questions, and help with learning. give answer in 3 lines.",
    "3": "You are a player AI assistant. You provide information about various games, answer questions, and help with gaming strategies. give answer in 3 lines."
}

choice = input("Choose a role (1: Travel Guide, 2: Teacher, 3: Player): ")
if choice not in roles:
    print("Invalid choice. Defaulting to Travel Guide.")
    choice = "1"


message_history = [{
    "role": "system",
    #"content": "You are a teacher AI assistant. You provide information about various subjects, answer questions, and help with learning. give answer in 3 lines."
    "content": roles[choice] 
}]


print(f"You have chosen the role: {roles[choice]}")

while True:
    user_input = input("You: ")
    message_history.append({"role": "user", "content": user_input})
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the AI Assistant. Goodbye!")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=message_history
    )
    user_response = response.choices[0].message.content

    message_history.append({"role": "assistant", "content": user_response})

    print("AI: " + user_response)
    print("="*40)

    print("Message History:")
    for message in message_history:
        print(f"{message['role'].capitalize()}: {message['content']}")  
    print("="*40)

