### Yashirin parametrlarni aniqlash

Mass assignment obyekt maydonlaridan parametrlar yaratgani uchun siz ko‘pincha API qaytargan obyektlarni qo‘lda ko‘rib chiqish orqali yashirin parametrlarni aniqlashingiz mumkin.

Masalan, `PATCH /api/users/` so‘rovi foydalanuvchilarga username va email yangilash imkonini beradi va quyidagi JSON’ni o‘z ichiga oladi:

```json
{
    "username": "wiener",
    "email": "wiener@example.com"
}
```

Shu bilan birga, `GET /api/users/123` so‘rovi quyidagi JSON’ni qaytaradi:

```json
{
    "id": 123,
    "name": "John Doe",
    "email": "john@example.com",
    "isAdmin": "false"
}
```

Bu esa yashirin `id` va `isAdmin` parametrlarining ham ichki foydalanuvchi obyektiga username va email bilan birga bog‘langanidan dalolat berishi mumkin.

---

### Mass assignment zaifliklarini sinash

`isAdmin` parametrini o‘zgartirish mumkinligini tekshirish uchun uni `PATCH` so‘roviga qo‘shing:

```json
{
    "username": "wiener",
    "email": "wiener@example.com",
    "isAdmin": false
}
```

Bundan tashqari, `isAdmin` uchun noto‘g‘ri qiymat yuborib ko‘ring:

```json
{
    "username": "wiener",
    "email": "wiener@example.com",
    "isAdmin": "foo"
}
```

Agar ilova boshqacha harakat qilsa, bu noto‘g‘ri qiymat so‘rov mantiqiga ta’sir qilishi mumkinligini bildiradi, ammo to‘g‘ri qiymat ta’sir qilmaydi. Bu parametr foydalanuvchi tomonidan muvaffaqiyatli yangilanishi mumkinligidan darak beradi.

Keyin `isAdmin` qiymatini `true` qilib yuboring va zaiflikdan foydalanishga urinib ko‘ring:

```json
{
    "username": "wiener",
    "email": "wiener@example.com",
    "isAdmin": true
}
```

Agar `isAdmin` qiymati etarli darajada tekshirilmasdan va tozalashsiz foydalanuvchi obyektiga bog‘lansa, `wiener` foydalanuvchisi noto‘g‘ri tarzda admin huquqlariga ega bo‘lishi mumkin. Buni tekshirish uchun `wiener` sifatida tizimga kiring va admin funksiyalaridan foydalanish mumkinligini sinab ko‘ring.
