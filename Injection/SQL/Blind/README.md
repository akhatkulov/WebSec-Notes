Masalan, **Users** nomli jadval bo‘lib, unda **Username** va **Password** ustunlari mavjud, va **Administrator** nomli foydalanuvchi bo‘lsin. Siz ushbu foydalanuvchining parolini belgilangan usulda, belgilarni bittadan tekshirish orqali aniqlashingiz mumkin.

Buning uchun quyidagi kiritmadan boshlaysiz:

```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 'm
```

Bu so‘rovga javoban tizim **"Welcome back"** xabarini qaytarsa, bu shuni anglatadiki, kiritilgan shart **rost** va parolning birinchi belgisi **m dan kattaroq**.

Keyin quyidagi kiritmani yuboramiz:

```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) > 't
```

Agar tizim **"Welcome back"** xabarini qaytarmasa, bu shuni anglatadiki, shart **yolg‘on** va parolning birinchi belgisi **t dan kattamas**.

Oxir-oqibat quyidagi so‘rovni yuborsak va **"Welcome back"** xabarini olsak, bu parolning birinchi belgisi **s** ekanini tasdiqlaydi:

```
xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's
```

Shunday qilib, biz bu jarayonni davom ettirib, **Administrator** foydalanuvchisining parolini to‘liq aniqlashimiz mumkin.

**Eslatma:**
`SUBSTRING` funksiyasi ayrim ma’lumotlar bazalarida `SUBSTR` deb nomlanadi. Batafsil ma’lumot uchun **SQL injection cheat sheet**ga qarang.
