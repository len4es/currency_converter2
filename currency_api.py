import requests
import history_manager


def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Exchange rates: {data['rates']}")
        return data['rates']
    else:
        print("Error fetching data.")
        return None


def convert_currency():
    rates = get_exchange_rate()
    if rates:
        from_currency = input("Enter the currency you want to convert from (e.g., USD): ").upper()
        to_currency = input("Enter the currency you want to convert to (e.g., EUR): ").upper()

        if from_currency in rates and to_currency in rates:
            amount = input("Enter the amount to convert: ")

            try:
                amount = float(amount)
                if amount < 0:
                    print("Amount cannot be negative.")
                    return

                converted_amount = amount * (rates[to_currency] / rates[from_currency])
                print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
                history_manager.save_history(from_currency, to_currency, amount, converted_amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        else:
            print("Invalid currency codes entered.")
