amount_input = input("Enter the amount: ")
currency = input("Enter currency pair (USD to EUR, EUR to USD, USD to GBP, GBP to USD): ")

if not amount_input.replace('.', '', 1).isdigit():
    print("Invalid amount entered.")
else:
    amount = float(amount_input)

    if amount < 0:
        print("Amount must be non-negative.")
    else:
        if currency.lower() == "usd to eur":
            converted = amount * 0.92
            print("Converted amount:", converted, "EUR")
        elif currency.lower() == "eur to usd":
            converted = amount * 1.09
            print("Converted amount:", converted, "USD")
        elif currency.lower() == "usd to gbp":
            converted = amount * 0.78
            print("Converted amount:", converted, "GBP")
        elif currency.lower() == "gbp to usd":
            converted = amount * 1.28
            print("Converted amount:", converted, "USD")
        else:
            print("Invalid currency pair entered.")
