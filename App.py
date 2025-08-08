import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data.get("info"):
            rate = data["info"]["rate"]
            result = data["result"]
            print(f"\n💱 Exchange Rate: 1 {from_currency} = {rate:.2f} {to_currency}")
            print(f"✅ {amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            print("❌ Could not fetch exchange rate. Try again later.")
    except Exception as e:
        print("⚠️ Error:", e)

# ---------- User Input ----------
print("🌍 Currency Converter")
from_currency = input("Enter FROM currency code (e.g., USD, INR): ").upper()
to_currency = input("Enter TO currency code (e.g., EUR, JPY): ").upper()
amount = float(input("Enter amount to convert: "))

convert_currency(from_currency, to_currency, amount)
