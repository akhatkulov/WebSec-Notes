REST yo‘llarida server-side parameter pollution (SSPP) test qilish
RESTful API ba’zan parametr nomlari va qiymatlarini query string o‘rniga URL yo‘lida joylashtiradi. Masalan, quyidagi yo‘lni ko‘rib chiqing:

```
/api/users/123
```

Bu URL yo‘li quyidagicha bo‘linadi:

* `/api` — asosiy API endpoint.
* `/users` — resursni bildiradi, bu yerda foydalanuvchilar (users).
* `/123` — parametr, bu yerda aniq foydalanuvchining identifikatori.

Endi tasavvur qiling, dastur foydalanuvchi nomiga qarab ularning profilini tahrirlash imkonini beradi. So‘rovlar quyidagi endpointga yuboriladi:

```
GET /edit_profile.php?name=peter
```

Bu esa server tomonida quyidagi so‘rovni keltirib chiqaradi:

```
GET /api/private/users/peter
```

Hujumchi API’dan foydalanib, server tomonidagi URL yo‘l parametrlarini manipulyatsiya qilishi va ekspluatatsiya qilishi mumkin. Ushbu zaiflikni test qilish uchun parametrlarni o‘zgartirishda **path traversal** ketma-ketliklarini qo‘shing va dasturning javobini kuzating.

Masalan, siz `peter/../admin` qiymatini URL-encoded shaklda yuborishingiz mumkin:

```
GET /edit_profile.php?name=peter%2f..%2fadmin
```

Bu esa server tomonida quyidagi so‘rovni keltirib chiqarishi mumkin:

```
GET /api/private/users/peter/../admin
```

Agar server tomoni yoki back-end API ushbu yo‘lni **normalize** qilsa, u quyidagicha qayta ishlanishi mumkin:

```
/api/private/users/admin
```

