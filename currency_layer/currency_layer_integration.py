import json
from configparser import ConfigParser

import requests as requests
from requests import Response

from constants import Constants


class CurrencyLayerIntegration:

    def __init__(self, properties_file_name) -> None:
        config = ConfigParser()
        config.read(properties_file_name)
        print(config.__len__())
        self.host = config['currency_layer'][Constants.CONFIG_API_HOST]

    def get_price(self, source_currency: str, target_currency: str, amount: int = 1) -> float:
        querystring = {Constants.REQUEST_PARAM_FROM: source_currency, Constants.REQUEST_PARAM_TO: target_currency,
                       Constants.REQUEST_PARAM_AMOUNT: amount}
        response = requests.request("GET", self.host, params=querystring)
        price = self.get_conversion_rate(response)
        print(price)
        return price

    def get_conversion_rate(self, response: Response) -> float:
        return_object = json.loads(response.text)
        if return_object['info']:
            return return_object['info']['rate']
        return 0