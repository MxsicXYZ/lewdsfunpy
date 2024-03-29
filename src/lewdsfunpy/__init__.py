from dotenv import dotenv_values
import requests
config = dotenv_values(".env")

Lewds_API_KEY = config.get('AhniKey', None)


class APIKeyMissingError(Exception):
    pass


if Lewds_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://kyra.tk "
        "for how to retrieve an authentication token from "
        "Lewds API and make a .env file "
        "with your key and value"
        "ex:  AhniKey=YOURAPITOKENHERE"
    )

session = requests.Session()
session.params = {}
session.headers['authorization'] = Lewds_API_KEY

from .lewds import LewdsAPI
