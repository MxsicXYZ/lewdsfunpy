import requests
from . import session
from dotenv import dotenv_values
config = dotenv_values(".env")

class LewdsAPI(object):

    def __init__(self, ctx):
        self.name = ctx

    def nsfw(self):

        try:

            path = 'https://kyra.tk/v2/nsfw/img?end={}&apikey={}'.format(self, config.LEWDS_API_KEY)
            response = session.get(path, timeout=5)

            if response.json()["error"] == True:
                 return ("Invalid API Key Provided!")

            if response.json()["error"] == "False":
                return response.json()['result']

        except requests.Timeout:
            return ("No such endpoint exists or the API is down!")
