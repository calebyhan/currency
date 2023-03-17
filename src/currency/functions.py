import csv

def check(currency):
    with open("currency.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if currency in row[1]:
                return True
    return False