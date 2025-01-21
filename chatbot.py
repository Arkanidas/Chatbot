import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the API key for OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": "how are you?"}],
        max_tokens=100
    )

    return response.choices[0].message.content.strip() 

if __name__ == "__main__":
    print(generate_response())
