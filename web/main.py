import requests

valyta1 = "USD"
valyta2 = "EUR"
valyta3 = "UAH"

amount = 1000

url = f"https://api.apilayer.com/exchangerates_data/convert?from={valyta1}&to={valyta2}&amount={amount}"

headers = {
    "apikey" : "TOKEN_HERE"
}

result = requests.get(url = url, headers = headers)

round_number = round(result.json()[result], 1)

print(round_number)