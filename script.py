# import pyautogui
import time
import openai
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_usermessage():
   
    url = "https://agents.moderationinterface.com/chat/index"  

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
  
    response = requests.get(url, headers=headers)

 
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        p_tag = soup.find_all('p', attrs={'_ngcontent-': True})
        print("the user message RAW1:", response.text)
        print("the user message RAW2:", [p.text for p in p_tag])
        
        if p_tag:
            latest_message = p_tag[-1].text.strip() 
            print("användare:" + latest_message )
            return latest_message 
            
        else:
            return "No user messages found." 
            
    else:
        return f"Failed to fetch the page. Status code: {response.status_code}"


#generate a message from the gpt api
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
    message = fetch_usermessage()
    print("Fetched message:", message)
  


 # error handling for the fetched usermessage
    if "Failed to fetch" not in message and "No usermessage was found." not in message:
        gpt_response = generate_response(message)
        print("Kvinnan:", gpt_response)
       
    else:
        print("Skipping GPT generation due to fetch issue.")

















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





