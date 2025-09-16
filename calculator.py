import yfinance as yf

def calculate_profit_loss(buy_price: float, sell_price: float, shares: int) -> float:
    return (sell_price - buy_price) * shares

def calculate_percentage_change(buy_price: float, sell_price: float) -> float:
    if buy_price == 0:
        return 0.0
    return ((sell_price - buy_price) / buy_price) * 100

# ---------- API helper ----------
def get_price_yfinance(ticker: str) -> float | None:
    try:
        t = yf.Ticker(ticker)

        # ลองใช้ fast_info ก่อน
        price = None
        try:
            fi = getattr(t, "fast_info", None)
            if fi is not None:
                price = getattr(fi, "last_price", None)
                if price is None and isinstance(fi, dict):
                    price = fi.get("last_price")
        except Exception:
            price = None

        if price is None:
            # fallback: ดึงราคาปิดล่าสุดจากประวัติ 1 วัน
            hist = t.history(period="1d")
            if not hist.empty:
                price = float(hist["Close"].iloc[-1])

        return float(price) if price is not None else None
    except Exception:
        return None
