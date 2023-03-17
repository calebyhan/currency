import currency.functions as functions
import requests

def convert(input_currency, output_currency, amount=1, roundTo=2):
    if not functions.check(input_currency.upper()):
        raise ValueError("Invalid input currency " + input_currency)
    if not functions.check(output_currency.upper()):
        raise ValueError("Invalid output currency " + output_currency)
    if amount <= 0:
        raise ValueError("Input amount must be positive.")
    url = "http://floatrates.com/daily/" + input_currency + ".json"
    data = requests.get(url).json()[output_currency.lower()]
    return round(amount * data["rate"], roundTo)


def rate(input_currency, output_currency, roundTo=2):
    if not functions.check(input_currency.upper()):
        raise ValueError("Invalid input currency " + input_currency)
    if not functions.check(output_currency.upper()):
        raise ValueError("Invalid output currency " + output_currency)
    url = "http://floatrates.com/daily/" + input_currency + ".json"
    data = requests.get(url).json()[output_currency.lower()]
    return round(data["rate"], roundTo)
