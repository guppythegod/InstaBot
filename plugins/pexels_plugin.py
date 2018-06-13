import requests
import json

PEXELS_API = "https://api.pexels.com/v1"


class PexelsClient(object):

    def __init__(self, api_key, token)
        self.AUTH_HEADER = {"Authorization": api_key}

    def get_images(self, amount, query):
        links = []
        search_response = json.loads(
            (
                requests.get(
                    PEXELS_API
                    + "/search?per_page={}&query={}&orientation=squarish".format(
                        amount, query
                    ), 
                    headers=self.AUTH_HEADER
                )
            ).content
        )
        for i in range(amount):
            links.append(search_response["photos"][i]["url"])
        for i in range((len(links))):
            print(links[i] + "\n")
        return links
