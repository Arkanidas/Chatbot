from openai import OpenAI

client = OpenAI(api_key='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')




def generate_response():
    response = client.chat.completions.create(model="gpt-3.5-turbo",  
    messages=[{"role": "user", "content": "write me a joke"}],
    max_tokens=100)
    return response.choices[0].message.content.strip() + "hello"

if __name__ == "__main__":
    generate_response()
