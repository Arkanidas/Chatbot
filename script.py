# import pyautogui
import time
import openai
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

url = "https://agents.moderationinterface.com/chat/index"

def fetch_usermessage():
    latest_message = None 
    
    options = Options()
    options.set_capability("moz:firefoxOptions", {"args": ["--remote-debugging-port=9222"]})


    driver = webdriver.Remote(
        command_executor='http://localhost:9222',  # The URL to connect to the running Firefox instance
        options=options
    )

   

    try:
        print("Waiting for user to load the page...")

        # Open the page
        driver.get(url)
        
        # Wait for the page to load and verify the URL
        time.sleep(2)  # Adjust as necessary to ensure page has loaded
        current_url = driver.current_url

        if current_url != url:
            print("Error: Not on the expected chat page.")
            return None

        # Wait until at least one <p> tag with _ngcontent attribute appears
        wait = WebDriverWait(driver, 30)  # Wait up to 30 seconds
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p[_ngcontent-]")))

        # Find all <p> elements with _ngcontent attribute
        p_tags = driver.find_elements(By.CSS_SELECTOR, "p[_ngcontent-]")

        # Get the last message
        if p_tags:
            latest_message = p_tags[-1].text.strip()
            print("User message:", latest_message)
            return latest_message
        else:
            print("No user messages found.")
            return None
    finally:
        print("User message:", latest_message)




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
    if "No user messages found." not in message:
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





