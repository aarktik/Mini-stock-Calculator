import os
def get_alpha_vantage_key() -> str | None:
    return os.getenv("ALPHAVANTAGE_API_KEY")
