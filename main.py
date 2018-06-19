from plugins import bitly_plugin, hootsuite_plugin, instapy_plugin, unsplash_plugin, pexels_plugin
from credentials import config

import multiprocessing
import json
import requests

# ----- SETUP ----- #

configs = config.configurations

unsplash = unsplash_plugin.UnsplashClient(configs["api_keys"]["UNSPLASH_API_KEY"])
pexels = pexels_plugin.PexelsClient(configs["api_keys"]["PEXELS_API_KEY"])

instapy = instapy_plugin.InstapyClient(
    configs["instapy_configs"]["INSTAGRAM_USERNAME"],
    configs["instapy_configs"]["INSTAGRAM_PASSWORD"],
    configs["instapy_configs"]["NICHES"],
    configs["instapy_configs"]["COMMENTS"],
    configs["instapy_configs"]["COMMENT_PERCENTAGE"],
    configs["instapy_configs"]["LIKE_PRECENTAGE"]
)

if __name__ == '__main__':
    instapy.like()