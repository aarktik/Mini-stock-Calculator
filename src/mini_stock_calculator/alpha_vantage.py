import requests
from .config import get_alpha_vantage_key

def get_price_alpha_vantage(ticker: str, api_key: str | None = None) -> float | None:
    api_key = api_key or get_alpha_vantage_key()
    if not api_key:
        print("⚠️ Missing ALPHAVANTAGE_API_KEY.")
        return None

    url = "https://www.alphavantage.co/query"
    params = {"function": "GLOBAL_QUOTE", "symbol": ticker, "apikey": api_key}

    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        data = r.json()
        quote = data.get("Global Quote") or data.get("globalQuote")
        if not quote:
            return None
        price_str = quote.get("05. price") or quote.get("05.price")
        return float(price_str) if price_str else None
    except Exception as e:
        print(f"⚠️ API error for {ticker}: {e}")
        return None
