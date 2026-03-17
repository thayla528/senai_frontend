import requests

base_url = "https://api.thecatapi.com/v1"

def get_gatos():
    url = f'{base_url}/breeds'

    headers = {

        "x - api - key": "live_iWDD4mMUxWoRwbJgRuEcabGIi8wN6YLMf8XTV1ya4MP8DhShRE4ctgQgqQ6I9tbD"

    }

    resposta = requests.get(url, headers=headers)
    return resposta.json()

def get_image():
    url = "https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)
    return resposta.json()[0]