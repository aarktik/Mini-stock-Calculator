def main():
  all_profit_losses = []
  all_percentage_changes = []
  total_session_profit_loss = 0
  average_percentage_change = 0
  while True:
    print("Welcome to Mini Stock Calculator!")

    while True:
        try:
            buy_price = float(input("Enter the buy price per share (USD): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if buy_price < 0:
            print("Buy price cannot be negative.")
        else:
            break

    use_api = input("Use live sell price from yfinance? (y/n): ").strip().lower() == "y"

    if use_api:
        ticker = input("Enter US stock ticker (e.g., AAPL, MSFT, NVDA): ").strip().upper()
        sell_price = get_price_yfinance(ticker)
        if sell_price is None:
            print("⚠️ Could not fetch live price. Please input manually.")
            while True:
                try:
                    sell_price = float(input("Enter the sell price per share (USD): "))
                    if sell_price < 0:
                        print("Sell price cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print(f"Live price for {ticker}: {sell_price:.4f} USD")
    else:
        while True:
            try:
                sell_price = float(input("Enter the sell price per share (USD): "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if sell_price < 0:
                print("Sell price cannot be negative.")
            else:
                break

    while True:
        try:
            shares = int(input("Enter the number of shares: "))
        except ValueError:
            print("Please enter an integer number of shares.")
            continue
        if shares <= 0:
            print("Number of shares must be greater than 0.")
        else:
            break

    profit_loss = calculate_profit_loss(buy_price, sell_price, shares)
    percentage_change = calculate_percentage_change(buy_price, sell_price)

    print(f"\n--- Results ---")
    print(f"Buy Price: {buy_price:.4f} USD")
    print(f"Sell Price: {sell_price:.4f} USD")
    print(f"Shares: {shares}")
    print(f"Total Profit/Loss: {profit_loss:.2f} USD")
    print(f"Percentage Change: {percentage_change:.2f}%")
    all_profit_losses.append(profit_loss)
    all_percentage_changes.append(percentage_change)

    for value in all_profit_losses:
      total_session_profit_loss += value
    for value in all_percentage_changes:
      average_percentage_change += value
    average_percentage_change /= len(all_percentage_changes)

    if profit_loss > 0 and percentage_change > 15:
        print("It's a great investment!")
    elif profit_loss > 0 and percentage_change < 15:
        print("It's a good investment!")
    elif profit_loss == 0 and percentage_change == 0:
        print("It's a neutral investment.")
    elif profit_loss < 0 and percentage_change > -20:
        print("You should consider cutting your losses next time.")
    else:
        print("Wow, more than -20%? At this rate, you’re not investing—you’re donating to the market.")
    cont = input("Do you want to try again? (y/n): ").lower()
    print("\n")
    if cont != 'y':
        print("Program ended.")
        break
  print("Summary of your Portfolio")
  if total_session_profit_loss > 0:
    print(f"Profit : {total_session_profit_loss:.2f}(USD)")
  else:
    print(f"Profit : {total_session_profit_loss:.2f}")
  print(f"Average Percentage Change : {average_percentage_change:.2f}%")
if __name__ == "__main__":
    main()
