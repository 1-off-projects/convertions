import requests
import os

def clear(): 
    if os.name == 'nt': 
        os.system('cls') 
    else:
        os.system('clear')

def get_conversion_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data["rates"][target_currency]

def convert_currency(amount, rate):
    return amount * rate

def main():
    while True:
        print("Currency Converter")
        print("1. Convert EUR to USD")
        print("2. Convert USD to EUR")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            euros = float(input("Enter amount in Euros: "))
            rate = get_conversion_rate("EUR", "USD")
            usd = convert_currency(euros, rate)
            print(f"{euros:.2f} Euros = {usd:.2f} USD")
        elif choice == '2':
            usd = float(input("Enter amount in USD: "))
            rate = get_conversion_rate("USD", "EUR")
            euros = convert_currency(usd, rate)
            print(f"{usd:.2f} USD = {euros:.2f} Euros")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    clear()
    main()
