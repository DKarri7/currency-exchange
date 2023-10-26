import requests
import time

MAX_RETRIES = 3

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://api.currencyapi.com/v3/latest?apikey=cur_live_If3XfM6XdU0pRpZKErhh1Z5d1gwR8kmuf5ZJSaQd"
    retries = 0

    while retries < MAX_RETRIES:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if to_currency in data['data']:
                    return data['data'][to_currency]['value']
                else:
                    print(f"Conversion rate for {to_currency} not found")
                    return None
            else:
                print(f"Error fetching data from the API")
                return None
        except requests.exceptions.RequestException as i:
            print(f"Request failed. Retrying in 5 seconds...")
            time.sleep(3)
            retries += 1

def convert_currency():
    api_key = "60e5dc0fae15fbc716c36125"
    from_currency = input("Enter the currency to convert from: ").upper()
    to_currency = input("Enter the currency to convert to: ").upper()
    amount = float(input(f"Enter the amount in {from_currency}: "))

    exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        new_converted_amount = format(converted_amount,".2f")
        print(f"{amount} {from_currency} is equal to {new_converted_amount} {to_currency}")
    else:
        print(f"Failed to retrieve exchange rate for {from_currency} to {to_currency}")

if __name__ == "__main__":
    convert_currency()