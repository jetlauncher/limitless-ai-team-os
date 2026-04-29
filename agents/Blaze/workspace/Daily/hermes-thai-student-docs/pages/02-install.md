# 02 — ติดตั้ง Hermes แบบเร็ว

> เหมาะกับ macOS, Linux, WSL2 และ Android ผ่าน Termux  
> Windows แบบ native ยังไม่รองรับ ควรใช้ WSL2

## สิ่งที่ต้องมี

อย่างน้อยต้องมี:

```bash
git --version
```

ถ้ายังไม่มี Git ให้ติดตั้งก่อน

## คำสั่งติดตั้งหลัก

เปิด Terminal แล้วรัน:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Installer จะช่วยจัดการหลายอย่างให้ เช่น:

- clone repo
- เตรียม Python environment
- ติดตั้ง dependency หลัก
- สร้างคำสั่ง `hermes`
- พา setup provider/model

## หลังติดตั้งเสร็จ

Reload shell:

```bash
source ~/.bashrc
```

หรือถ้าใช้ zsh:

```bash
source ~/.zshrc
```

จากนั้นลองเปิด Hermes:

```bash
hermes
```

## ถ้าติดตั้งบน Windows

ให้ติดตั้ง WSL2 ก่อน แล้วค่อยรันคำสั่งติดตั้งใน WSL2 terminal

```bash
wsl --install
```

หลังจากนั้นเปิด Ubuntu/WSL แล้วใช้คำสั่ง install ด้านบน

## จุดที่นักเรียนมักพลาด

- รันคำสั่งใน Windows PowerShell ตรงๆ — ไม่ควร ให้ใช้ WSL2
- ลืม reload shell หลังติดตั้ง
- ยังไม่ได้เลือก model/provider
- API key ใส่ผิด หรือยังไม่ได้สมัคร provider
