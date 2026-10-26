from openai import OpenAI
from dotenv import load_dotenv
import os

#load config from env file
load_dotenv()

#Create a client that communicates with Ollama
client=OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

#send a question to AI model

response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role":"user",
            "content":"What is AI?"
        }
    ]
)

#Display the response
print(response.choices[0].message.content)