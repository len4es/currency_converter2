import json


def save_history(from_currency, to_currency, amount, converted_amount):
    history_entry = {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "amount": amount,
        "converted_amount": converted_amount
    }

    with open('history.json', 'a') as file:
        json.dump(history_entry, file)
        file.write("\n")


def view_history():
    try:
        with open('history.json', 'r') as file:
            history = file.readlines()
            if history:
                print("Conversion History:")
                for entry in history:
                    data = json.loads(entry)
                    print(
                        f"{data['amount']} {data['from_currency']} -> {data['converted_amount']} {data['to_currency']}")
            else:
                print("No conversion history found.")
    except FileNotFoundError:
        print("No history found.")
