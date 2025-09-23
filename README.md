# 📊 Mini Stock Calculator

โปรเจกต์นี้เป็น **Mini Stock Portfolio Calculator** สำหรับนักศึกษา/นักลงทุนมือใหม่  
ประกอบด้วย 2 ส่วนหลัก:  
- **Core (CLI)** → โปรแกรม command-line ใช้คำนวณกำไร/ขาดทุนหุ้น  
- **GUI (Gradio)** → ส่วนติดต่อผู้ใช้แบบ web interface (เหมาะกับการรันใน Colab หรือ local)  

รองรับการดึงราคาหุ้นสดจาก **Alpha Vantage API** และสามารถรันผ่าน **Docker** ได้

---

## 🗂️ โครงสร้างโปรเจกต์

mini-stock-calculator/
├─ src/
│  └─ mini_stock_calculator/
│     ├─ calculations.py      # logic คำนวณ P/L, %change
│     ├─ alpha_vantage.py     # เรียก API ราคาหุ้น
│     ├─ config.py            # จัดการ API key จาก environment
│     └─ cli.py               # main program (CLI)
├─ apps/
│  └─ gradio_ui/
│     └─ app.py               # Gradio web UI
├─ docker/
│  ├─ Dockerfile.cli
│  └─ Dockerfile.gradio
├─ compose.yaml               # docker compose (optional)
├─ requirements.txt           # deps ของ core
├─ .env.example               # ตัวอย่าง environment file
└─ README.md


---

## ⚙️ การตั้งค่า API Key
1. สมัคร API key ฟรีจาก [Alpha Vantage](https://www.alphavantage.co/support/#api-key)  
2. คัดลอก `.env.example` → `.env` แล้วใส่ key ของคุณ  
   ```bash
   ALPHAVANTAGE_API_KEY=YOUR_REAL_KEY
3. อย่า commit .env ขึ้น GitHub (มีใน .gitignore แล้ว)

---

## ▶️ วิธีรัน (Local)
### 1) รัน CLI

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

### 2) รัน Gradio UI
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
