import requests

currencyToConvert = str(
    #our api doesnt accept lowercase values
    input("Enter in the currency you'd like to convert: ")).upper()

convertedCurrency = str(
    #our api doesnt accept lowercase values
    input("Enter in the currency you'd like to convert to: ")).upper()

cashAmount = float(input("Enter in the amount of money you want to convert: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={cashAmount}&from={currencyToConvert}&to={convertedCurrency}")

print(
    f"{cashAmount} {currencyToConvert} is {response.json()['rates'][convertedCurrency]} {convertedCurrency}")
