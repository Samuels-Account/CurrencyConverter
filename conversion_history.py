import csv


def save_conversion_history(conversion):
    with open("conversion_history.csv", mode="a", newline="") as history_file:
        fieldnames = ["from_currency", "to_currency", "amount", "converted_amount", "rate", "date"]
        writer = csv.DictWriter(history_file, fieldnames=fieldnames)

        # Write header if the file is empty
        if history_file.tell() == 0:
            writer.writeheader()

        # Write the conversion data
        writer.writerow({
            "from_currency": conversion["from_currency"],
            "to_currency": conversion["to_currency"],
            "amount": conversion["amount"],
            "converted_amount": conversion["converted_amount"],
            "rate": conversion["rate"],
            "date": conversion["date"]
        })


def get_conversion_history():
    with open("conversion_history.csv", mode="r") as history_file:
        reader = csv.DictReader(history_file)
        history = []
        for row in reader:
            history.append(row)
        return history
