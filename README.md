**Project Portfolio: https://github.com/calebyhan/CalebHan** 

# currency-ch

Python library for currency exchanges.

All rates originated from [FloatRates](https://www.floatrates.com/json-feeds.html).

Disclaimer: all rates may or may not be the most accurate, and could vary by search on the internet.


## Installation
----------------------

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install currency-ch.

```bash
pip install currency-ch
```


## Usage
----------------------

```python
import currency

# converts amount of money from one currency to another
currency.convert("usd", "eur", 1)

# returns rate from one currency to another
currency.rate("usd", "eur")
```


## Documentation
----------------------

``currency.convert(input_currency, output_currency, amount, roundTo)``

Converts input_currency of amount (default 1) to output_currency with rounded to roundTo decimal places (default 2).

``currency.rate(input_currency, output_currency, roundTo)``

Returns rate of converting input_currency to output_currency rounded to roundTo decimal places (default 2).

``currency.add(values, output_currency, roundTo)``

Adds up currencies in 2-D array values (in format [amount, input_currency]), and displays in form of output_currency rounded to roundTo decimal places (default 2).

## Contributing
----------------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
----------------------

[MIT](https://choosealicense.com/licenses/mit/)
