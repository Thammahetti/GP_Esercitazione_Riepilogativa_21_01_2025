
import requests

def requestod():
    response = requests.get('http://api.open-notify.org/astros.json')
    data = response.json()
    return data.get("people", [])