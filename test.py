import requests

API_KEY = "a7758b35-3454-4038-bd80-48a2300f2d03"

url = "https://api.vapi.ai/call/web"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "assistant": {
        "firstMessage": "Hello! I am a voice assistant. How can I help you today?",
        "model": {
            "provider": "openai",
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful voice assistant."
                }
            ]
        },
        "voice": {
            "provider": "playht",
            "voiceId": "jennifer"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
result = response.json()

print(" Open this link NOW in Chrome:")
print(result['webCallUrl'])