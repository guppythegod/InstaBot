from plugins import bitly_plugin, hootsuite_plugin, imgur_plugin, instapy_plugin, unsplash_plugin, pexels_plugin
from credentials import config

import multiprocessing
import json
import requests

# ----- SETUP ----- #

configs = config.configurations

unsplash = unsplash_plugin.UnsplashClient(configs["api_keys"]["UNSPLASH_API_KEY"])
pexels = pexels_plugin.PexelsClient(configs["api_keys"]["PEXELS_API_KEY"])

print(unsplash.get_images(10, "office"))
