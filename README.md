# AIPrototype24
นักศึกษา : ชฎารัตน์ อิ่มสารพางค์ รหัส 643021198-6 STAT

## 1. **Ubuntu**
Ubuntu คือระบบปฏิบัติการที่ใช้พื้นฐานจาก Linux 

**ดาวน์โหลด Ubuntu**
- สำหรับการติดตั้งบน WSL (Windows Subsystem for Linux): [Ubuntu WSL](https://ubuntu.com/desktop/wsl)

<details>
<summary>คำสั่งพื้นฐาน</summary>

```bash
sudo apt update                   # อัปเดตแหล่งข้อมูลแพ็คเกจ
sudo apt upgrade                  # อัปเกรดแพ็คเกจทั้งหมด
sudo apt install <package_name>   # ติดตั้ง package
sudo apt-get install <application>   # ติดตั้งแอปพลิเคชัน
mkdir <directory_name>            # สร้าง folder
rm <file_name>                    # ลบไฟล์หรืออื่นๆ
pwd                                # เราอยู่ที่ไหนในคอมพิวเตอร์ของเรา
ls                                 # เรียกดูไฟล์และโฟลเดอร์ที่เราอยู่
ls -l                              # ดูรายละเอียดในไฟล์และโฟลเดอร์
ls -ltr                            # เรียกดูไฟล์ เรียงตามเวลา เก่ามาใหม่
ls -ltrh                           # เรียกดูไฟล์ เรียงตามเวลา เก่ามาใหม่ แบบเข้าใจง่าย
man ls                             # เรียกดูคู่มือคำสั่ง ls (กด q เพื่อออก)
```
</details>

<details>
<summary>คำสั่ง Change Directory</summary>
  
```bash
cd <name>                        #เข้าไฟล์
cd ..                            # ออกไฟล์
cd  หรือ cd ~                     # กลับไป home
cat ~/<file_name>                # เปิดไฟล์เฉยๆ
mv newfile.x ./test_lv3/test_lv4/.                 # ย้ายไฟล์
mv ./test_lv3/test_lv4/newfile.x ./test_lv3/test_lv4/newfile.z   # เปลี่ยนชื่อไฟล์
cp ./test_lv3/test_lv4/newfile.z .                 # คัดลอกไฟล์

#ตัวอย่าง
chadarat@chachacharat:~/test/test_lv2/test_lv3/test_lv4$ cd ../../test2_lv3  #ออกเเล้วเข้า
chadarat@chachacharat:~/test/test_lv2/test2_lv3$                             #เข้ามาละ
```
</details>

<details>
<summary>คำสั่งอื่น ๆ</summary>
  ```bash
vi abc.txt                    # เปิดไฟล์ด้วย vi
  Mode i                       # เข้าสู่โหมดแก้ไข
  Esc :wq                      # ออกจาก vi พร้อมบันทึก
  :q!                          # ออกจาก vi โดยไม่บันทึก
```
</details>

## 2. **Github**
<details>
<summary>push ขึ้น Git ครั้งแรก</summary>
  
  ```bash
git remote add origin <URL ของ repo>       # เพิ่ม remote repository 
git branch -M main                         # เปลี่ยนชื่อ branch เป็น main (GitHub ใช้ main แทน master)
git push -u origin main                    # Push โค้ดขึ้น GitHub 
git config --global user.name "Your Name"  # ตั้งค่าชื่อของผู้ใช้ Git
git config --global user.email "your-email@example.com"  # ตั้งค่าอีเมลของผู้ใช้ Git
```
</details>

<details>
<summary>คำสั่งใน Github</summary>

  ```bash
git init                             # เริ่มต้น Git repository ใหม่ในโฟลเดอร์ปัจจุบัน
git status                           # แสดงสถานะของไฟล์ใน repository 
git branch                           # ตรวจสอบ branch ปัจจุบัน
git add .                            # เพิ่มไฟล์ทั้งหมดเข้า 
git commit -m "เพิ่มคำอธิบาย commit"    # บันทึกการเปลี่ยนแปลงใน Git
git log                              # แสดงประวัติ commit ล่าสุด
git rm <filename>                    # ลบไฟล์และ commit การลบ
git mv <old-name> <new-name>         # เปลี่ยนชื่อไฟล์และ commit การเปลี่ยนแปลง
git push --force                     # บังคับ push ทับของเดิม (ใช้ระวัง)
```
</details>

## 3. **conda**

## 4. **Web Page**
การสร้างเว็บเพจประกอบด้วย 3 ส่วนหลัก ได้แก่ โครงสร้าง (Structure), รูปแบบ (Style), และการทำงาน (Functionality) ซึ่งใช้ HTML, CSS, และ JavaScript
- HTML
การกำหนดโครงสร้างของเว็บเพจ

- CSS
กำหนดรูปแบบของเว็บเพจ เช่น สี, ฟอนต์, ขนาด, ระยะห่าง, การจัดตำแหน่ง
ทำให้เว็บเพจดูสวยงามและเป็นระเบียบ

- JavaScript
เพิ่มความสามารถในการโต้ตอบ เช่น ปุ่มกด, เมนูแบบ Dropdown, การตรวจสอบฟอร์ม, ดึงข้อมูล API

- Github ที่รวบรวมโค้ด web page & web app : [code](https://github.com/BloodPS/WebPage-Auto-Insurance)
- Project's Web Page : [WebPage-AutoInsurance](https://bloodps.github.io/WebPage-Auto-Insurance/)

## 5. **Web Application**
Backend คือ ส่วนที่ทำงานเบื้องหลัง เช่น การจัดการฐานข้อมูล, ระบบล็อกอิน, API
- Flask (Python) 
- Project's Web App : [WebApp-AutoInsurance](https://bloodps.github.io/WebPage-Auto-Insurance/WebPage.html)

## 6. **Web Service**


## 7. **Deep Learning**

