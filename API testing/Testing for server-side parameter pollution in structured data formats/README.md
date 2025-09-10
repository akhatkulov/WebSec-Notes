**Tuzilgan ma’lumot formatlarida server-side parameter pollution (SSPP) ni test qilish**

Hujumchi parametrlarni manipulyatsiya qilib, serverning JSON yoki XML kabi boshqa tuzilgan ma’lumot formatlarini qayta ishlashdagi zaifliklaridan foydalanishi mumkin. Buni tekshirish uchun foydalanuvchi kiritmalariga kutilmagan tuzilgan ma’lumotlarni qo‘shib ko‘rish va server qanday javob qaytarishini kuzatish kerak.

Misol tariqasida, foydalanuvchilarga o‘z profillarini tahrirlash imkonini beradigan dastur bo‘lsin. Siz ismingizni o‘zgartirsangiz, brauzeringiz server API’iga quyidagi so‘rovni yuboradi:

```
POST /myaccount
name=peter
```

Bu esa server tomonda quyidagi so‘rovga aylanadi:

```
PATCH /users/7312/update
{"name":"peter"}
```

Siz ushbu so‘rovga **access\_level** parametrini qo‘shib ko‘rishingiz mumkin:

```
POST /myaccount
name=peter","access_level":"administrator
```

Agar foydalanuvchi kiritmalari server tomonidagi JSON ma’lumotlariga to‘g‘ri tekshirilmasdan yoki sanitizatsiya qilinmasdan qo‘shilsa, quyidagi ko‘rinishdagi so‘rov yuzaga keladi:

```
PATCH /users/7312/update
{name="peter","access_level":"administrator"}
```

Natijada, **peter** foydalanuvchisiga administrator huquqlari berilishi mumkin.

---

**Tegishli sahifalar**
Query string ichiga kiritishingiz mumkin bo‘lgan yashirin parametrlarni aniqlash haqida ma’lumot olish uchun **Finding hidden parameters** bo‘limiga qarang.

