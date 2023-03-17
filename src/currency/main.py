import csv
import functions

def convert(input_currency, output_currency, amount=1):
    if not functions.check(input_currency):
        raise ValueError("Invalid input currency" + input_currency)
    if not functions.check(output_currency):
        raise ValueError("Invalid output currency" + output_currency)