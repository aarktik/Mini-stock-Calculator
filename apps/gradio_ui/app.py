import os
import gradio as gr

from mini_stock_calculator.calculations import (
    calculate_percentage_change as calc_pct,
    calculate_profit_loss as calc_pl,
)
from mini_stock_calculator.alpha_vantage import get_price_alpha_vantage

COLS = ["Ticker","Buy (USD)","Live/Sell (USD)","Shares","P/L (USD)","Change (%)"]

def add_row(ticker, buy, shares, table):
    table = table or []
    ticker = (ticker or "").strip().upper()
    try:
        buy = float(buy)
        shares = int(shares)
    except:
        return table, table, "**Total P/L: 0.00 USD**", "**Average % Change: 0.00%**", "กรอก Buy/Shares ให้ถูกต้อง"

    if not ticker or buy < 0 or shares <= 0:
        return table, table, "**Total P/L: 0.00 USD**", "**Average % Change: 0.00%**", "Ticker ว่าง หรือค่าไม่ถูกต้อง"

    price = get_price_alpha_vantage(ticker)
    if price is None:
        return table, table, "**Total P/L: 0.00 USD**", "**Average % Change: 0.00%**", f"ดึงราคา {ticker} ไม่ได้ (อาจติด rate limit)"

    pl  = calc_pl(buy, price, shares)
    pct = calc_pct(buy, price)
    row = [ticker, round(buy,4), round(price,4), int(shares), round(pl,2), round(pct,2)]
    table = table + [row]
    total = sum(r[4] for r in table)
    avg   = sum(r[5] for r in table)/len(table)

    return table, table, f"**Total P/L: {total:.2f} USD**", f"**Average % Change: {avg:.2f}%**", "เพิ่มรายการแล้ว"

def remove_row(index, table):
    table = table or []
    try:
        idx = int(index)
        if 0 <= idx < len(table):
            table.pop(idx)
            msg = f"ลบแถวที่ {idx} แล้ว"
        else:
            msg = "index ไม่อยู่ในช่วง"
    except:
        msg = "ใส่ index เป็นจำนวนเต็ม"

    total = sum((r[4] for r in table), 0.0) if table else 0.0
    avg   = (sum(r[5] for r in table)/len(table)) if table else 0.0
    return table, table, f"**Total P/L: {total:.2f} USD**", f"**Average % Change: {avg:.2f}%**", msg

def clear_all():
    return [], [], "**Total P/L: 0.00 USD**", "**Average % Change: 0.00%**", "ล้างตารางแล้ว"

def build_app():
    with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue")) as demo:
        gr.Markdown("## 📊 Mini Stock Portfolio (Gradio UI)")
        with gr.Row():
            ticker = gr.Textbox(label="Ticker", placeholder="AAPL")
            buy    = gr.Number(label="Buy (USD)", value=0.0, precision=2)
            shares = gr.Number(label="Shares", value=1, precision=0)
        table_state = gr.State([])
        add_btn = gr.Button("Add (Fetch & Calc)", variant="primary")

        df = gr.Dataframe(headers=COLS, row_count=(0, "dynamic"), interactive=False)
        with gr.Row():
            rm_idx = gr.Number(label="Row index to remove (0-based)", value=0, precision=0)
            rm_btn = gr.Button("Remove Row")
            clr_btn = gr.Button("Clear All")

        total_md = gr.Markdown("**Total P/L: 0.00 USD**")
        avg_md   = gr.Markdown("**Average % Change: 0.00%**")
        status   = gr.Markdown("")

        add_btn.click(add_row, [ticker, buy, shares, table_state], [table_state, df, total_md, avg_md, status])
        rm_btn.click(remove_row, [rm_idx, table_state], [table_state, df, total_md, avg_md, status])
        clr_btn.click(clear_all, [], [table_state, df, total_md, avg_md, status])

    return demo

if __name__ == "__main__":
    app = build_app()
    app.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", "7860")))
