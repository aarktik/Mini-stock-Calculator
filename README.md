# Mini stock calculator
Mini stock calculator โปรเจคจากภาษา Python ที่ทำงานบน colab มีไว้เพื่อคำนวณการซื้อขาย-หุ้น, คำนวณกำไร-ขาดทุน, คำนวณความเปลี่ยนแปลงของราคาหุ้นเป็นเปอร์เซ็นต์ แสดงผลรวมกำไร-ขาดทุน ของหุ้นที่กรอกมาทั้งหมด 

โปรเจกต์Mini project นี้เป็นส่วนหนึ่งของรายวิชา CP352301 Script Programming ภาคเรียนที่ 1 ปีการศึกษา 2568
# 📌 Sprint Progress – Mini Stock Calculator

## 🟢 Sprint 1: Initial Prototype

ในสปรินต์แรก ทีมได้เริ่มต้นสร้าง **โปรแกรมต้นแบบ (prototype)** ของ Mini Stock Calculator โดยเน้นไปที่ฟังก์ชันพื้นฐาน ได้แก่

* รับค่า **ราคาซื้อ (buy price)**, **ราคาขาย (sell price)** และ **จำนวนหุ้น (number of shares)** จากผู้ใช้
* เขียนเงื่อนไขตรวจสอบ input เบื้องต้น เช่น หากผู้ใช้ใส่ค่าที่เป็นลบ จะบังคับให้กรอกใหม่
* คำนวณ **กำไร/ขาดทุน (Profit/Loss)** และ **เปอร์เซ็นต์การเปลี่ยนแปลง (Percentage Change)**
* แสดงข้อความตามผลลัพธ์ เช่น `"คุณมีกำไร"`, `"คุณขาดทุน"`, หรือ `"ไม่มีการเปลี่ยนแปลง"`
* ออกแบบโครงสร้างให้รองรับการวนลูป (loop) เพื่อให้ผู้ใช้สามารถทำการคำนวณได้หลายครั้ง

---

## 🟡 Sprint 2: Feature Expansion

ในสปรินต์ที่สอง ได้มีการพัฒนาโปรแกรมให้ **มีความสามารถมากขึ้นและใกล้เคียงโปรแกรมจริง** โดยเพิ่มฟีเจอร์และปรับปรุงการทำงานดังนี้

* เชื่อมต่อกับ **yfinance API** เพื่อดึงราคาหุ้นสด (live price) โดยผู้ใช้สามารถเลือกใช้ได้
* หากการดึงข้อมูลสดล้มเหลว จะมี **fallback option** ให้ผู้ใช้กรอกราคาขายเอง
* ปรับปรุงการตรวจสอบ input ให้ละเอียดขึ้น เช่น ตรวจสอบว่าเป็นตัวเลข, ต้องไม่ติดลบ
* เพิ่มระบบเก็บผลลัพธ์ (profit/loss และ percentage change) ของแต่ละรอบไว้ใน **list**
* เตรียมระบบสำหรับการสรุปผลรวมเมื่อสิ้นสุด session
---

## 🔵 Sprint 3: Refinement & User Experience

ในสปรินต์ที่สาม ทีมได้โฟกัสไปที่การ **ปรับปรุงคุณภาพโค้ดและประสบการณ์ผู้ใช้ (UX)** โดยมีการเปลี่ยนแปลงดังนี้

* สรุปผลการลงทุนทั้ง session ได้แก่

  * **ผลรวมของกำไร/ขาดทุนทั้งหมด (Total Profit/Loss)**
  * **ค่าเฉลี่ยของเปอร์เซ็นต์การเปลี่ยนแปลง (Average Percentage Change)**
* จัดการการแสดงผลด้วยการ **กำหนดจำนวนทศนิยม** ให้คงที่ เช่น แสดงผลเป็น 2 ตำแหน่ง (.2f)
* ปรับโฟลว์ของโปรแกรมให้ใช้งานง่ายขึ้น:

  * หลังคำนวณเสร็จ ผู้ใช้สามารถเลือก **“ลองใหม่”** เพื่อทำรอบใหม่ หรือ **“จบการทำงาน”** เพื่อแสดงสรุป
* เพิ่มระบบ **ข้อความแนะนำ (commentary system)** ตามผลลัพธ์ เช่น

  * หาก % change สูง → `"การลงทุนครั้งนี้ยอดเยี่ยม"`
  * หากขาดทุนมาก → `"ควรพิจารณาตัดขาดทุน"`
* ปรับปรุงการเก็บข้อมูลและ loop ให้ทำงานได้อย่างต่อเนื่อง

---
# Mini-stock-Calculator
Mini Stock Calculator (Sprint 1) : [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/supakron-exe/5f577417caa7f240c2da731d683b2853/mini-stock-calculator.ipynb)

Mini Stock Calculator (Sprint 2) : [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/supakron-exe/9e17abaaa439ac528ad1ad45fe568788/-colab.ipynb)

Mini Stock Calculator (Sprint 3) : [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/supakron-exe/c25e963c71cb0f11a689f4e4f12bcffb/mini-stock-calculator-sprint-3.ipynb)
