import requests
import json
from datetime import datetime

url = "https://openexchangerates.org/api/"


def get_exchange_rate(date, base_currency, target_currency):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        return None

    valid_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD']
    if base_currency.upper() not in valid_currencies or target_currency.upper() not in valid_currencies:
        print("Invalid currency code. Please enter a valid currency code.")
        return None

    endpoint = f"{url}historical/{date}.json"
    params = {
        "app_id": "39019316a3d749f3917208c84f77b577",
        "base": base_currency.upper(),
        "symbols": target_currency.upper(),
    }

    try:
        response = requests.get(endpoint, params=params)
    except requests.exceptions.RequestException as e:
        print("Failed to retrieve exchange rate.")
        return None

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    try:
        data = json.loads(response.text)
    except json.JSONDecodeError as e:
        print("Invalid response from API.")
        return None

    if target_currency.upper() not in data["rates"]:
        print(f"Error: {target_currency.upper()} is not a valid currency")
        return None

    exchange_rate = data["rates"][target_currency.upper()]

    return exchange_rate


if __name__ == "__main__":

    date = input("Enter the date you want to convert from (YYYY-MM-DD), or leave blank for latest: ")
    base_currency = input("Enter the currency you have (e.g. USD): ")
    amount = input("Enter the amount you have: ")
    target_currency = input("Enter the currency you want to convert to (e.g. EUR): ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        exit()

    exchange_rate = get_exchange_rate(date, base_currency.upper(), target_currency.upper())

    if exchange_rate is None:
        print("Failed to retrieve exchange rate")
    else:

        converted_amount = amount * exchange_rate

        print(
            f"{amount:.2f} {base_currency.upper()} on {date} is equal to {converted_amount:.2f} {target_currency.upper()}")
