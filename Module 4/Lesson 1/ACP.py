import requests

def get_time():
    URL = https://time.now/developer/api/timezone/Europe/London
    response = requests.get(URL)

    if response.status_code == 200:
       london_time =   response.json()
       return f"{}"
