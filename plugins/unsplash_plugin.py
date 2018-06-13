import requests
import json

UNSPLASH_API = "https://api.unsplash.com"


class UnsplashClient(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_images(self, amount, query):
        links = []
        search_response = json.loads(
            (
                requests.get(
                    UNSPLASH_API
                    + "/search/photos?client_id={}&per_page={}&query={}&orientation=squarish".format(
                        self.api_key, amount, query
                    )
                )
            ).content
        )
        # print(json.dumps(search_response, indent=4, sort_keys=True))
        for i in range(amount):
            links.append(search_response["results"][i]["urls"]["raw"])
        for i in range((len(links))): 
            print(links[i] + "\n")
        return links
