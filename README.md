# 📊 Mini Stock Calculator

โปรเจกต์นี้เป็น **Mini Stock Calculator** สำหรับนักศึกษา/นักลงทุนมือใหม่  
ประกอบด้วย 2 ส่วนหลัก:  
- **Core (CLI)** → โปรแกรม command-line ใช้คำนวณกำไร/ขาดทุนหุ้น  
- **GUI (Gradio)** → ส่วนติดต่อผู้ใช้แบบ web interface (เหมาะกับการรันใน Colab หรือ local)  

รองรับการดึงราคาหุ้นสดจาก **Alpha Vantage API** และสามารถรันผ่าน **Docker** ได้

---

## 🗂️ โครงสร้างโปรเจกต์
```
mini-stock-calculator/
├─ apps/
│  └─ gradio_ui/
│     └─ app.py               # Gradio web UI
│     └─ requirements.txt     # deps ของ core
│
│
├─ docker/
│  ├─ Dockerfile.cli
│  └─ Dockerfile.gradio
│
│
├─ src/
│  └─ mini_stock_calculator/
│     ├─ alpha_vantage.py     # เรียก API ราคาหุ้น
│     ├─ calculations.py      # logic คำนวณ P/L, %change
│     ├─ cli.py               # main program (CLI)
│     └─ config.py            # จัดการ API key จาก environment
│     
│
├─ .env.example               # ตัวอย่าง environment file
├─ .gitignore
├─ README.md
└─ compose.yaml               # docker compose (optional)
```

---

## ⚙️ การตั้งค่า API Key
1. สมัคร API key ฟรีจาก [Alpha Vantage](https://www.alphavantage.co/support/#api-key)  
2. คัดลอก `.env.example` → `.env` แล้วใส่ key ของคุณ  
   ```bash
   ALPHAVANTAGE_API_KEY=YOUR_REAL_KEY
3. อย่า commit .env ขึ้น GitHub (มีใน .gitignore แล้ว)

---

## ▶️ วิธีรัน (Local)
### 1) Run CLI

สร้าง virtualenv
python -m venv .venv
source .venv/bin/activate  # บน Windows: .venv\Scripts\activate

ติดตั้ง dependencies
pip install -r requirements.txt

export key
export ALPHAVANTAGE_API_KEY=YOUR_REAL_KEY   # macOS/Linux
หรือบน Windows PowerShell:
$env:ALPHAVANTAGE_API_KEY="YOUR_REAL_KEY"

รันโปรแกรม
python -m mini_stock_calculator.cli

### 2) Run Gradio UI
pip install -r apps/gradio_ui/requirements.txt
export ALPHAVANTAGE_API_KEY=YOUR_REAL_KEY
python apps/gradio_ui/app.py

---

## 🐳 รันด้วย Docker
### CLI
docker build -f docker/Dockerfile.cli -t mini-stock-cli .
docker run --rm -it -e ALPHAVANTAGE_API_KEY=YOUR_KEY mini-stock-cli

### Gradio UI
docker build -f docker/Dockerfile.gradio -t mini-stock-gradio .
docker run --rm -p 7860:7860 -e ALPHAVANTAGE_API_KEY=YOUR_KEY mini-stock-gradio

### Compose (รัน CLI + GUI พร้อมกัน)
docker compose up --build

---

## 📌 ตัวอย่างการใช้งาน (CLI)
```
Welcome to Mini Stock Calculator!
Enter stock tickers separated by comma (e.g., AAPL,MSFT,NVDA): AAPL,MSFT,TOST
Enter the buy price for AAPL (USD): 200
Enter the number of shares for AAPL: 1
Enter the buy price for MSFT (USD): 130
Enter the number of shares for MSFT: 3
Enter the buy price for TOST (USD): 35
Enter the number of shares for TOST: 2
Use live sell price from a REAL API (Alpha Vantage)? (y/n): y
Live price for AAPL: 254.43 USD

--- Results for AAPL ---
Buy Price: 200.00 USD
Sell Price: 254.43 USD
Shares: 1
Profit: 54.43 USD
Percentage Change: 27.22%
It's a great investment!
Live price for MSFT: 514.45 USD

--- Results for MSFT ---
Buy Price: 130.00 USD
Sell Price: 514.45 USD
Shares: 3
Profit: 1153.35 USD
Percentage Change: 295.73%
It's a great investment!
Live price for TOST: 37.95 USD

--- Results for TOST ---
Buy Price: 35.00 USD
Sell Price: 37.95 USD
Shares: 2
Profit: 5.90 USD
Percentage Change: 8.43%
It's a good investment!

Summary of Portfolio
AAPL: Profit = 54.43 USD, Change = 27.22%
MSFT: Profit = 1153.35 USD, Change = 295.73%
TOST: Profit = 5.90 USD, Change = 8.43%

Total Profit: 1213.68 USD
Average Percentage Change: 110.46%
```
---

## 🔄 CI/CD (DevOps)
- มีไฟล์ GitHub Actions (.github/workflows/ci.yml) สำหรับ
 - ตรวจสอบโค้ด (compileall)
 - สร้าง Docker image (CLI และ GUI)
- สามารถขยายไปยัง CD (Continuous Deployment) ได้ เช่น Deploy อัตโนมัติไปยัง Render/Railway/Cloud VM

---

## 📌 หมายเหตุ
- Alpha Vantage ฟรีมี rate limit (5 calls/minute) ถ้าเรียก API ถี่เกินไปจะได้ None
- ควรใช้ .env หรือ GitHub Secrets เก็บคีย์จริง
- GUI ใช้ gradio เหมาะกับการรันใน Colab หรือบนเซิร์ฟเวอร์
