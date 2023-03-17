**Project Portfolio: https://github.com/calebyhan/CalebHan** 

# currency-ch

Python library for currency exchanges.

All rates originated from [FloatRates](https://www.floatrates.com/json-feeds.html).


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

``currency.rate(input_currency, output_currency)``

Returns rate of converting input_currency to output_currency.


## Contributing
----------------------

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License
----------------------

[MIT](https://choosealicense.com/licenses/mit/)
