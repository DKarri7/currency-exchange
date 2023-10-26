import requests
import time

MAX_RETRIES = 3

def get_exchange_rate(data, from_currency, to_currency):
    if to_currency in data['data']:
        return data['data'][to_currency]['value']
    else:
        print(f"Conversion rate for {to_currency} not found.")
        return None

def currency_input(prompt, valid_currencies):
    while True:
        try:
            currency = input(prompt).upper()
            if currency in valid_currencies:
                return currency
            else:
                print("Invalid currency code. Please enter a valid code currency.")
        except ValueError:
            print("Invalid input. Please enter a valid code currency.")

def currency_conversion():
    api_key = "60e5dc0fae15fbc716c36125"

    data = None
    while data is None:
        try:
            response = requests.get(f"https://api.currencyapi.com/v3/latest?apikey=cur_live_If3XfM6XdU0pRpZKErhh1Z5d1gwR8kmuf5ZJSaQd")
            if response.status_code == 200:
                data = response.json()
            else:
                print("Error fetching data from the API. Retrying in 3 seconds...")
                time.sleep(3)
        except requests.exceptions.RequestException as i:
            print("Please wait...")
            time.sleep(3)

    from_currency = currency_input("Enter the currency to convert from: ", data['data'].keys())
    to_currency = currency_input("Enter the currency to convert to: ", data['data'].keys())

    while True:
        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount as a number.")

    exchange_rate = get_exchange_rate(data, from_currency, to_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        new_converted_amount = format(converted_amount, ".2f")
        print(f"{amount} {from_currency} is equal to {new_converted_amount} {to_currency}")
    else:
        print(f"Failed to retrieve exchange rate for {from_currency} to {to_currency}")

if __name__ == "__main__":
    currency_conversion()