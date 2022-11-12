import requests
from sseclient import SSEClient

print("Слушатель запущен") 
messages = SSEClient("http://127.0.0.1:3000/api/services/subscribe")
for msg in messages:
    print(msg)
