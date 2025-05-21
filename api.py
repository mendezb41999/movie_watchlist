import requests

API_KEY = "3f4eb3b0" # Replace with your OMDb key

def search_movie(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()