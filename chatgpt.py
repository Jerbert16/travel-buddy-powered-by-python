import requests
import os
from dotenv import load_dotenv

load_dotenv()

def call_openai_api(prompt):
    api_key = os.getenv('OPENAI_API_KEY')
    endpoint = 'https://api.openai.com/v1/completions'
    model = 'gpt-3.5-turbo-instruct'
    temperature = 0.6
    max_tokens = 500

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    data = {
        'model': model,
        'prompt': prompt, 
        'temperature': temperature,
        'max_tokens': max_tokens,
    }

    response = requests.post(endpoint, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        assistant_reply = result['choices'][0]['text']
        print(assistant_reply)
        return assistant_reply
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
        return None  # or handle the error as needed










