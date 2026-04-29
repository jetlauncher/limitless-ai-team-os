# 08 — ปัญหาที่เจอบ่อย

## 1. รัน `hermes` แล้ว command not found

ลอง reload shell:

```bash
source ~/.bashrc
```

หรือ:

```bash
source ~/.zshrc
```

ถ้ายังไม่ได้ ให้ปิด terminal แล้วเปิดใหม่

## 2. Windows ใช้ไม่ได้

Hermes ไม่รองรับ Windows native

ใช้ WSL2 แทน:

```bash
wsl --install
```

แล้วติดตั้ง Hermes ใน WSL2

## 3. Agent ตอบไม่ได้ / provider error

เช็กว่าเลือก model/provider แล้ว:

```bash
hermes model
```

เช็ก API key ว่าใส่ถูกไหม

## 4. Telegram bot ไม่ตอบ

ตรวจ 4 อย่าง:

- token ถูกไหม
- gateway เปิดอยู่ไหม
- user ID ได้รับอนุญาตไหม
- ถ้าอยู่ใน group: privacy mode / admin ถูกไหม

## 5. Agent ทำงานมั่ว

อาจเกิดจาก prompt ไม่ชัด

แก้โดยใส่:

- เป้าหมาย
- context
- output format
- ข้อห้าม
- ตัวอย่างผลลัพธ์

## 6. ใช้ local model แล้ว error เรื่อง context

Hermes ต้องใช้ context window ใหญ่พอสำหรับงานหลายขั้นตอน

ถ้าใช้ local model ให้ตั้ง context length ให้เหมาะกับ model/server และทดสอบ chat พื้นฐานก่อน

## 7. จำข้อมูลผิด

Memory ไม่ควรเก็บทุกอย่าง

ถ้า agent จำผิด ให้บอกให้แก้ memory เช่น:

```text
จำใหม่นะ: ฉันต้องการให้คู่มือสำหรับนักเรียนเป็นภาษาไทยแบบง่าย ไม่ใช้ศัพท์เทคนิคเยอะ
```

## 8. หา log ได้ที่ไหน

โดยทั่วไป logs อยู่ใน:

```text
~/.hermes/logs/
```

ใช้ดู error เมื่อติดตั้งหรือ gateway มีปัญหา
