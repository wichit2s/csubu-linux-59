# การพัฒนาเว็บโดยใช้ python บน Linux

มาฝึกใช้ django-cms ในการสร้างเว็บไซต์ชื่อ csubusite
ความรู้ที่ควรมี python, CMS, html

อ้างอิง: http://docs.django-cms.org/en/release-3.4.x/introduction/index.html

## 1. ติดตั้ง
```sh
virtualenv .env
source .env/bin/activate
pip install --upgrade pip
pip install djangocms-installer
```

## 2. สร้าง directory และ csubusite
```sh
mkdir csubuproject
cd csubuproject
djangocms -f -p . csubusite
```

## 3. เปิด server ให้บริการ
```sh
python manage.py runserver
```

## 4. เข้าเว็บไซต์เพื่อสร้าง page

http://localhost:8000/admin

โดยใช้ user/password เป็น admin/admin



