import csv


def save_conversions_history(from_currency, to_currency, amount, converted_amount):
    with open("conversion_history.csv", mode="a", newline="") as history_file:
        fieldnames = ["From Currency", "To Currency", "Amount", "Converted Amount"]
        writer = csv.DictWriter(history_file, fieldnames=fieldnames)

        # Write header if the file is empty
        if history_file.tell() == 0:
            writer.writeheader()

        # Write the conversion data
        writer.writerow({
            "From Currency": from_currency,
            "To Currency": to_currency,
            "Amount": amount,
            "Converted Amount": converted_amount
        })


def view_conversions_history():
    with open("conversion_history.csv", mode="r") as history_file:
        reader = csv.DictReader(history_file)
        for row in reader:
            print(f"{row['Amount']} {row['From Currency']} is equal to {row['Converted Amount']} {row['To Currency']}")
