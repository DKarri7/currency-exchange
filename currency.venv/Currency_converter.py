import requests

def get_exchange_rate(api_key, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['conversion_rate']
    else:
        print("Error fetching data from the API")
        return None

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