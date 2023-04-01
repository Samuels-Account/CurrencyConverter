import requests
import json

LANGUAGES = {
    "en": {
        "currency_input": "Enter the currency you have (e.g. USD): ",
        "amount_input": "Enter the amount you have: ",
        "currency_output": "Enter the currency you want to convert to (e.g. EUR): ",
        "result": "{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}"
    },
    "fr": {
        "currency_input": "Entrez la devise que vous avez (par exemple USD) : ",
        "amount_input": "Entrez le montant que vous avez : ",
        "currency_output": "Entrez la devise dans laquelle vous souhaitez convertir (par exemple EUR) : ",
        "result": "{amount:.2f} {from_currency} est égal à {converted_amount:.2f} {to_currency}"
    }
}


def convert_currency(from_currency, to_currency, amount):
    # Set up the API endpoint and parameters
    url = "https://openexchangerates.org/api/latest.json"
    params = {
        "app_id": "868481e860004e148b401d99451c30e8",  # Replace with your app ID
        "symbols": f"{from_currency},{to_currency}",
    }

    # Send a GET request to the API
    response = requests.get(url, params=params)

    # Parse the JSON response into a Python dictionary
    data = json.loads(response.text)

    # Extract the exchange rates from the dictionary
    rates = data["rates"]

    # Convert the currency
    if from_currency == to_currency:
        converted_amount = amount
    else:
        converted_amount = amount / rates[from_currency] * rates[to_currency]

    # Return the converted amount
    return converted_amount
