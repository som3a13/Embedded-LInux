import requests

response = requests.get('https://www.boredapi.com/api/activity')
if response.status_code==200:
    data=response.json()
    print(data)
    for key,value in data.items():
        print(f"{key}: {value}")

