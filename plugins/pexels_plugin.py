import requests
import json

PEXELS_API = ""

class PexelsClient:
    
    def __init__(self, api_key, token):
        self.api_key = api_key
        self.token = token

    def get_images(self, amount, query):
        links = []
        return links