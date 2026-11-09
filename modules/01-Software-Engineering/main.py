import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    print("API Key tidak ditemukan!")
    exit()
    
url = "https://openrouter.ai/api/v1/chat/completions"   
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"  
}

payload = {
    "model": "nvidia/nemotron-3.5-super-vl:free",
    "messages": [
        {"role": "system", "content": "You are a political analyst who provides insights on global politics."},
        {"role": "user", "content": "Who is Jokowi, and what do you think about Indonesia's politics?"}
    ]
}

print("Mengirim request..")
response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    reply = data.get("choices")[0].get("message").get("content")
    # reply = data.get("choices")(0)("message")("content")
    print("Response dari API:", reply)
else:
    print("Request Gagal dengan status code:", response.status_code)
    print("Response:", response.text)





# response =requests.get('https://jsonplaceholder.typicode.com/todos/1')

# if response.status_code == 200:
#     print("Request Berhasil!")
#     print("Data:", response.json())
# else:
#     print("Request Gagal dengan status code:", response.status_code)