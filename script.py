# import pyautogui
import time
import openai
import os
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
        {"role": "system", "content": "Du ska låtsas vara en kvinna som kräver uppmärksamhet från män som är intresserade av dig"},
        {"role": "user", "content": user_message}
        ],
        max_tokens=100
    )

    return response.choices[0].message.content.strip() 

if __name__ == "__main__":
# userinput är chattmeddelandet fån kunden 
    user_input = "vad gör du idag älskade?"
    print(generate_response(user_input))



# def send_message(response):
    # Simulate typing and sending the message
   # pyautogui.write(response)
   # pyautogui.hotkey('option', 'enter')

#def main():
  #  while True:
    #    message = read_message()
    #    response = generate_response(message)
    #    send_message(response)
    #    time.sleep(1)  # Delay to avoid spamming





