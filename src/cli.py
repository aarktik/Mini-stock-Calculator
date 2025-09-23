from __future__ import annotations
from .calculations import calculate_profit_loss, calculate_percentage_change
from .alpha_vantage import get_stock_info

def main():
    stock_portfolio = []  # {"ticker","buy_price","sell_price","shares","profit","percentage_change"}
    total_session_profit_loss = 0.0
    all_percentage_changes = []

    print("Welcome to Mini Stock Calculator!")

    tickers_input = input("Enter stock tickers separated by comma (e.g., AAPL,MSFT,NVDA): ")
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]

    buy_prices = []
    shares_list = []

    for ticker in tickers:
        while True:
            try:
                buy = float(input(f"Enter the buy price for {ticker} (USD): "))
                if buy < 0:
                    print("Buy price cannot be negative.")
                    continue
                buy_prices.append(buy)
                break
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                share = int(input(f"Enter the number of shares for {ticker}: "))
                if share <= 0:
                    print("Shares must be greater than 0.")
                    continue
                shares_list.append(share)
                break
            except ValueError:
                print("Please enter a valid integer.")

    use_api = input("Use live sell price from a REAL API (Alpha Vantage)? (y/n): ").strip().lower() == "y"

    for i, ticker in enumerate(tickers):
        buy_price = buy_prices[i]
        shares = shares_list[i]

        if use_api:
            info = get_stock_info(ticker)
            if info is None:
                # fallback manual
                while True:
                    try:
                        sell_price = float(input(f"Enter the sell price for {ticker} (USD): "))
                        if sell_price < 0:
                            print("Sell price cannot be negative.")
                            continue
                        break
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                sell_price = info["price"]
                print(f"Live price for {ticker}: {sell_price:.2f} USD")
        else:
            while True:
                try:
                    sell_price = float(input(f"Enter the sell price for {ticker} (USD): "))
                    if sell_price < 0:
                        print("Sell price cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")

        profit_loss = calculate_profit_loss(buy_price, sell_price, shares)
        percentage_change = calculate_percentage_change(buy_price, sell_price)

        stock_portfolio.append({
            "ticker": ticker,
            "buy_price": buy_price,
            "sell_price": sell_price,
            "shares": shares,
            "profit": profit_loss,
            "percentage_change": percentage_change
        })

        total_session_profit_loss += profit_loss
        all_percentage_changes.append(percentage_change)

        if profit_loss > 0 and percentage_change > 15:
            advice = "It's a great investment!"
        elif profit_loss > 0 and percentage_change <= 15:
            advice = "It's a good investment!"
        elif profit_loss == 0 and percentage_change == 0:
            advice = "It's a neutral investment."
        elif profit_loss < 0 and percentage_change > -20:
            advice = "You should consider cutting your losses next time."
        else:
            advice = "Wow, more than -20%? At this rate, you’re not investing—you’re donating to the market."

        print(f"\n--- Results for {ticker} ---")
        print(f"Buy Price: {buy_price:.2f} USD")
        print(f"Sell Price: {sell_price:.2f} USD")
        print(f"Shares: {shares}")
        if profit_loss >= 0:
            print(f"Profit: {profit_loss:.2f} USD")
        else:
            print(f"Loss: {profit_loss:.2f} USD")
        print(f"Percentage Change: {percentage_change:.2f}%")
        print(advice)

    # --------- Summary ---------
    average_percentage_change = sum(all_percentage_changes) / len(all_percentage_changes) if all_percentage_changes else 0
    print("\nSummary of Portfolio")
    for stock in stock_portfolio:
        if stock['profit'] >= 0:
            print(f"{stock['ticker']}: Profit = {stock['profit']:.2f} USD, Change = {stock['percentage_change']:.2f}%")
        else:
            print(f"{stock['ticker']}: Loss = {stock['profit']:.2f} USD, Change = {stock['percentage_change']:.2f}%")

    if total_session_profit_loss >= 0:
        print(f"\nTotal Profit: {total_session_profit_loss:.2f} USD")
    else:
        print(f"\nTotal Loss: {total_session_profit_loss:.2f} USD")

    print(f"Average Percentage Change: {average_percentage_change:.2f}%")

if __name__ == "__main__":
    main()
