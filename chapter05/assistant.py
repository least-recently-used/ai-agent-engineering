from tools import  open_file
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

document = input("Enter the document to summarize (from the data folder): ")
file_content = open_file(document)

if file_content.startswith("Error:"):
    print(file_content)
else:
    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": f"Summarize this document:\n\n{file_content}"}
        ]
    )

    print("AI Summary: " + response.choices[0].message.content)




