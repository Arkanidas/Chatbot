import pyautogui
import time
from transformers import pipeline

# Load a pre-trained chatbot model (e.g., OpenAI or HuggingFace)
chatbot = pipeline('text-generation', model='gpt-3.5-turbo')

def read_message():
    # Simulate reading the latest message (you may replace this with actual API calls or OCR)
    # For API: Fetch latest message from the platform
    return "Hello, how are you?"

def generate_response(message):
    # Generate a response based on the context
    response = chatbot(message, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

def send_message(response):
    # Simulate typing and sending the message
    pyautogui.write(response)
    pyautogui.hotkey('option', 'enter')

def main():
    while True:
        message = read_message()
        response = generate_response(message)
        send_message(response)
        time.sleep(1)  # Delay to avoid spamming

if __name__ == "__main__":
    main()




