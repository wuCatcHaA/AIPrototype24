# AIPrototype24 
Github สำหรับรายวิชา SC664401 Prototyping for Artificial Intelligence and Machine Learning System

**นักศึกษา**: ชฎารัตน์ อิ่มสารพางค์ รหัส 643021198-6 STAT

**⭐งานสำหรับรายวิชานี้**:
1. Web Page โปรเจค >> [WebPage-AutoInsurance](https://bloodps.github.io/WebPage-Auto-Insurance/) 

   <img src="https://github.com/user-attachments/assets/2aa0a4a0-2aaf-48a0-b72d-b9cd5a3638a2" width="40%">
2. Web Application โปรเจค >> [WebApp-AutoInsurance](https://bloodps.github.io/WebPage-Auto-Insurance/WebPage.html)

   <img src="https://github.com/user-attachments/assets/d30be418-42b3-4226-b8f9-422790c66fbd" width="40%">
4. Github รายวิชา >> [Github](https://github.com/wuCatcHaA/AIPrototype24)

## 1. **Ubuntu** 🗂️
Ubuntu คือระบบปฏิบัติการที่ใช้พื้นฐานจาก Linux 

- สำหรับการติดตั้ง Ubuntu บน WSL (Windows Subsystem for Linux): [Ubuntu WSL](https://ubuntu.com/desktop/wsl)

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
Mode i                        # เข้าสู่โหมดพิมพ์หรือแก้ไขข้อความ
กด Esc :wq    ตามด้วย Enter    # ออกจาก vi พร้อมบันทึก
พิมพ์ :q!       ตามด้วย Enter   # ออกจาก vi โดยไม่บันทึก
```
</details>

- **screen** เป็นเครื่องมือที่ใช้สำหรับ เปิด session หลายอันใน Terminal และช่วยให้โปรแกรมยังคงรันอยู่แม้จะปิด Terminal ไปแล้ว
<details>
<summary>คำสั่ง</summary>
  
 ```bash
sudo apt install screen
screen -S <name_session>	   # สร้าง session ใหม่พร้อมตั้งชื่อ
Ctrl + A แล้วกด D            # ออกจาก screen โดยที่ยังทำงานอยู่
screen -ls	                 # แสดงรายการ session ที่กำลังทำงาน
screen -r	                   # กลับเข้าสู่ session ล่าสุดที่ยังทำงานอยู่
screen -r <name_session>     # กลับเข้าสู่ session ตามชื่อที่ระบุ
screen -d -r <name_session>  # บังคับเข้า session แม้จะมีการใช้งานอยู่ที่อื่น
exit	                       # ปิด session (หรือใช้ Ctrl + D)
screen -X -S <name_session> quit	# บังคับปิด session ที่ระบุ หรือ Ctrl + A แล้ว K (Kill Session)
```
</details>

## 2. **Github** 🐙
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

## 3. **Miniconda** 🐍

**ดาวน์โหลด** [Miniconda](https://docs.anaconda.com/miniconda/)
เป็นเวอร์ชันที่เล็กและเบาของ Anaconda โดยเป็นตัวติดตั้ง Python ที่มาพร้อมกับ conda ซึ่งเป็นตัวจัดการ Package & Environment
โดย conda environment ใช้เพื่อ แยกไลบรารีและ Python ของแต่ละโปรเจกต์
<details>
<summary>คำสั่งพื้นฐานของ Miniconda</summary>

  ```bash
conda --version                       # ตรวจสอบ version
conda create -n myenv python=3.9	    # สร้าง environment ใหม่ชื่อ myenv พร้อม Python 3.9
conda activate myenv	                # เปิดใช้งาน environment myenv
conda deactivate	                    # ออกจาก environment ปัจจุบัน
conda install numpy pandas	          # ติดตั้ง NumPy และ Pandas
conda list	                          # แสดงแพ็กเกจทั้งหมดที่ติดตั้ง
conda update conda	                  # อัปเดต conda เป็นเวอร์ชันล่าสุด
```
</details>

## 4. **Web Page** 🖥️
การสร้างเว็บเพจประกอบด้วย 3 ส่วนหลัก ได้แก่ โครงสร้าง (Structure), รูปแบบ (Style), และการทำงาน (Functionality) ซึ่งใช้ HTML, CSS, และ JavaScript
- HTML
การกำหนดโครงสร้างของเว็บเพจ

- CSS
กำหนดรูปแบบของเว็บเพจ เช่น สี, ฟอนต์, ขนาด, ระยะห่าง, การจัดตำแหน่ง
ทำให้เว็บเพจดูสวยงามและเป็นระเบียบ

- JavaScript
เพิ่มความสามารถในการโต้ตอบ เช่น ปุ่มกด, เมนูแบบ Dropdown, การตรวจสอบฟอร์ม, ดึงข้อมูล API

- Github ที่รวบรวมโค้ด web page & web app : [code](https://github.com/BloodPS/WebPage-Auto-Insurance)

## 5. **Web Application** 📲
Backend คือ ส่วนที่ทำงานเบื้องหลัง เช่น การจัดการฐานข้อมูล, ระบบล็อกอิน, API
- Flask (Python)  เว็บเฟรมเวิร์กที่ช่วยให้เราสร้างเว็บไซต์หรือ API ใช้สร้างหน้าเว็บ, ส่ง-รับข้อมูล, และเชื่อม Machine Learning กับเว็บได้

![image](https://github.com/user-attachments/assets/6a0e0ee6-3255-45ce-a486-b98281846e13)

**โครงสร้างพื้นฐานของ Flask**
  ```bash
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

## 6. **Web Service** 🌐
Web Service (เว็บเซอร์วิส) คือ ระบบหรือบริการที่ช่วยให้โปรแกรมหรือแอปพลิเคชันต่าง ๆ สามารถสื่อสารและแลกเปลี่ยนข้อมูลกันได้ผ่านเครือข่ายอินเทอร์เน็ต หรืออินทราเน็ต โดยปกติจะใช้ มาตรฐานเปิด (Open Standards) เช่น HTTP, XML, JSON และ SOAP หรือ REST API ในการรับส่งข้อมูล ทำให้แอปพลิเคชันที่เขียนด้วยภาษาโปรแกรมที่ต่างกันหรืออยู่คนละระบบสามารถทำงานร่วมกันได้

   <img src="https://github.com/user-attachments/assets/8eeca293-6bf0-401b-9a74-3c5d7d49bd9d" width="40%">

✅ Web Service ทำงานอย่างไร?
1. ส่งคำขอ (Request): ระบบหนึ่งส่งข้อมูลไปหาอีกระบบผ่านเครือข่าย (เช่น อินเทอร์เน็ต)
2. ประมวลผล (Process): Web Service ฝั่งเซิร์ฟเวอร์รับคำขอแล้วจัดการ
3. ส่งผลลัพธ์กลับ (Response): เซิร์ฟเวอร์ตอบกลับมาด้วยข้อมูลที่ร้องขอ หรือแจ้งผลการทำงาน
   
<details>
<summary>สร้าง Web Service API ด้วย Flask</summary>

  ```bash
##api
from flask import Flask, request
import json

@app.route('/simpleAPI',methods=['POST'])
def web_service_API_simple():
    #รับข้อมูล
    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)

    # แสดงผลข้อมูลที่รับเข้ามา
    print(inmessage)

    # ส่ง response กลับไป
    json_data = json.dumps({'y': 'received!'})
    return json_data

if __name__ == "__main__":   # run code 
    app.run(host='0.0.0.0',debug=True,port=5001) # เป็นคำสั่งที่ทำให้ Flask สร้าง Web Server ขึ้นมาเพื่อรอรับ Request จาก Client
```
</details>
<details>
<summary>Client ส่งข้อมูลไปยัง Web Service ด้วย requests</summary>

  ```bash
import json
import requests 

url = 'http://172.188.9.245:5001/simpleAPI'

# ข้อมูลที่จะส่งไปในรูปแบบ dictionary
myobj = {
    'message_key': 'message_val',
    'msg': 'tob_chadarat'
}

# ส่ง POST request ไปยัง web service
x = requests.post(url, data=json.dumps(myobj))
```
</details>



## 7. **Deep Learning** 🤖
**ลักษณะของ Neural Networks**
- เพอร์เซปตรอน

	ค่าที่เรียนรู้คือ weight

	1 cell ที่เรียนรู้จะพยายามปรับ weight จนกว่าจะตอบถูกทั้งหมด
  
- การเพิ่ม layer ทำให้เรียนรู้ไปเรื่อย ๆ ตอบได้ 100% แต่มันจะเกิดปัญหา overfiting
  
Input layer = feature + 1

hidden layer = ยิ่งมีเยอะ ยิ่งเเก้ปัญหาได้เยอะ

- เวลาตรวจสอบว่า model ทำงานได้ดีมั้ย 
จำนวนโหนดใน output layer เท่ากับจำนวน class ที่มี

สามารถกำหนดลักษณะของ output ได้ เช่น ตอบพร้อมกัน

เวลานำ data เข้ามาเเล้วให้มันได้คำตอบ >> feed forward 

ตัววัดประสิทธิภาพเรียกว่า loss > หาคำนวณได้เเล้วต้องไปดูว่าผิดที่ตรงไหน เเล้วเเก้ปัญญา“Backpropagation” แก้ weight โดยใช้ดิฟ 

- ข้อจำกัดของ ANN ยังต้องเป็นตัวเลข ถ้าวิเคราะห์ภาพต้องทำยังไง  (feature engineering)
1. รูปเปลี่ยนเป็นเลขอะไรได้บ้าง ภาพสี>histogram of color (“feature vector”)
2. **convolutional layers** > weight จะถูกรวมอยู่ในตารางเล็ก ๆ
   
   <img src="https://github.com/user-attachments/assets/7e95a415-5c3c-43da-81ab-927a6ecfdd9c" width="40%">
   
**Convolutional Neural Networks (CNN)**

   <img src="https://github.com/user-attachments/assets/98c70796-9c77-4a91-bf83-65ca02962249" width="40%">

**histogram of gradients**

   <img src="https://github.com/user-attachments/assets/c3fa5f03-b98d-4461-94c5-1f57a5d81a5b" width="40%">

**Deep learning** ก็คือการเพิ่ม layers ให้สามารถเรียนรู้ได้เองอัตโนมัติ

Activation function ทำหน้าที่บีบค่า ไม่ให้ค่าเยอะจนโมเดลระเบิด

batch size 

การป้องกันปัญหา overfit ด้วย dropout 

  <img src="https://github.com/user-attachments/assets/bd2234df-3a9a-4f40-9a43-bcc2e7803091" width="40%">

**ถ้า loss จากกราฟ Epoch ไม่ลดลง ก็คือไม่เริ่ด เเสดงว่าอาจจะต้องแก้โค้ด**
**ถ้า overfit ให้ดูว่า Epoch ที่เท่าไหร่ เเล้วฝึกใหม่**
1. Dropout
2. ควร plot กราฟดู

