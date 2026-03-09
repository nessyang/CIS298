

import requests

api_key = "ozZR2GUvzSXWYHBC59RogKcpKUkKhLJP"
base_url = "https://api.massive.com/"
saved_data = {}



def prev_day():
    symbol = input("Enter a stock ticker: ").upper()

    url = f"{base_url}/v2/aggs/ticker/{symbol}/prev?apiKey={api_key}"

    if url in saved_data:
        print("\nUsing saved result...")
        info = saved_data[url]
    else:
        response = requests.get(url)
        info = response.json()
        saved_data[url] = info

    if "results" not in info or len(info["results"]) == 0:
        print("No stock data found.")
        return

    stock_info = info["results"][0]

    print("\nPrevious Day Stock Info")
    print("Ticker:", symbol)
    print("Open:", stock_info.get("o", "N/A"))
    print("High:", stock_info.get("h", "N/A"))
    print("Low:", stock_info.get("l", "N/A"))
    print("Close:", stock_info.get("c", "N/A"))
    print("Volume:", stock_info.get("v", "N/A"))


def company_info():
    symbol = input("Enter a stock ticker: ").upper()

    url = f"{base_url}/v3/reference/tickers/{symbol}?apiKey={api_key}"

    if url in saved_data:
        print("\nUsing saved result...")
        info = saved_data[url]
    else:
        response = requests.get(url)
        info = response.json()
        saved_data[url] = info

    if "results" not in info:
        print("No company information found.")
        return

    company = info["results"]

    print("\nCompany Information")
    print("Ticker:", symbol)
    print("Name:", company.get("name", "N/A"))
    print("Market:", company.get("market", "N/A"))
    print("Type:", company.get("type", "N/A"))
    print("Exchange:", company.get("primary_exchange", "N/A"))


choice = ""

while choice != "3":
    print("\n----- STOCK EXPLORER PROJECT 3 CIS 298-----")
    print("1. Look up previous day prices")
    print("2. Look up company info")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        prev_day()
    elif choice == "2":
        company_info()
    elif choice == "3":
        print("Program ended.")
    else:
        print("Invalid choice. Try again.")