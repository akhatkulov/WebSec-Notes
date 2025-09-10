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


**O‘xshash misolni ko‘rib chiqamiz, lekin bunda mijoz (client) tomonidan yuboriladigan foydalanuvchi kiritmalari JSON formatida bo‘ladi.**

Siz ismingizni o‘zgartirsangiz, brauzeringiz quyidagi so‘rovni yuboradi:

```
POST /myaccount
{"name": "peter"}
```

Bu esa server tomonda quyidagi ko‘rinishga aylanadi:

```
PATCH /users/7312/update
{"name":"peter"}
```

Siz so‘rovga **access\_level** parametrini quyidagicha qo‘shib ko‘rishingiz mumkin:

```
POST /myaccount
{"name": "peter\",\"access_level\":\"administrator"}
```

Agar foydalanuvchi kiritmalari dekod qilinib, lekin yetarli kodlashsiz (encoding) server tomondagi JSON ma’lumotlariga qo‘shilsa, quyidagi so‘rov hosil bo‘ladi:

```
PATCH /users/7312/update
{"name":"peter","access_level":"administrator"}
```

Bu yana **peter** foydalanuvchisiga administrator huquqlari berilishiga olib kelishi mumkin.

---

**Tuzilgan format injeksiyasi (Structured format injection)** javoblarda ham yuz berishi mumkin. Masalan, foydalanuvchi kiritmalari xavfsiz tarzda ma’lumotlar bazasida saqlansa-yu, lekin backend API tomonidan qaytarilayotgan JSON javobiga yetarlicha kodlashsiz qo‘shib yuborilsa. Bunday holatlarda siz odatda injeksiyani aniqlash va ekspluatatsiya qilishni **so‘rovdagidek** usulda amalga oshirishingiz mumkin.

---

**Eslatma**
Yuqoridagi misol **JSON** formatida, lekin server-side parameter pollution istalgan tuzilgan ma’lumot formatida yuz berishi mumkin. **XML** misoli uchun, **XML external entity (XXE) injection** mavzusidagi **XInclude attacks** bo‘limiga qarang.



**Tegishli sahifalar**
Query string ichiga kiritishingiz mumkin bo‘lgan yashirin parametrlarni aniqlash haqida ma’lumot olish uchun **Finding hidden parameters** bo‘limiga qarang.

