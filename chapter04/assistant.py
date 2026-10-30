from tools import get_current_time, generate_password, roll_dice
from openai import OpenAI
from dotenv import load_dotenv
import os

from tools_manager import execute_tool_command
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


message_history = [{
    "role": "system",
    "content": "You are a helpful AI assistant."
}]

# print(f"You have chosen the role: {roles[choice]}")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ["exit", "quit"]:
        print("Exiting the AI Assistant. Goodbye!")
        break

    message_history.append({"role": "user", "content": user_input})

    tool_response = execute_tool_command(user_input)
    if tool_response is not None:
        # The API only accepts text, so turn numbers (like dice rolls) into strings
        tool_response = str(tool_response)
        print("Tool Response: ", tool_response)
        message_history.append({"role": "assistant", "content": tool_response})
        continue

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=message_history
    ) 
    user_response = response.choices[0].message.content

    print("AI: " + user_response)
    print("="*40)

    # print("Message History:")
    # for message in message_history:
    #     print(f"{message['role'].capitalize()}: {message['content']}")  
    # print("="*40)
