import requests
import os
from dotenv import load_dotenv
load_dotenv()

def send_sms(api_key, to, message, sender):
    url = 'https://smspoh.com/api/v2/send'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'to': to,
        'message': message,
        'sender': sender,  
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("SMS sent successfully")
    else:
        print("Failed to send SMS:", response.status_code, response.text)

if __name__ == "__main__":
    api_key = os.getenv('API_KEY')  # Replace this with your API key
    to = os.getenv('PHONE_NUMBER')  # Replace this with the recipient's phone number
    sender = os.getenv('SENDER_NAME') # Replace this with the sender's name
    message = "Hello, this is a test SMS from SMS Poh API."

    send_sms(api_key, to, message, sender)
