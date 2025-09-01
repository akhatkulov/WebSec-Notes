### API hujjatlari (API documentation)

API’lar odatda ishlab chiquvchilar ularni qanday ishlatishni va integratsiya qilishni bilishlari uchun **hujjatlashtiriladi**.

---

#### Inson o‘qiy oladigan va mashina o‘qiy oladigan hujjatlar

* **Inson uchun o‘qilishi mumkin bo‘lgan hujjatlar** — ishlab chiquvchilar API’dan qanday foydalanishni tushunishi uchun yoziladi. Ular batafsil tushuntirishlar, misollar va foydalanish ssenariylarini o‘z ichiga olishi mumkin.
* **Mashina uchun o‘qilishi mumkin bo‘lgan hujjatlar** — dasturiy ta’minot tomonidan qayta ishlanishi uchun yoziladi, masalan, API integratsiyasi va tekshiruvlarni avtomatlashtirish uchun. Ular odatda **JSON** yoki **XML** kabi tuzilgan formatlarda yoziladi.

API hujjatlari ko‘pincha ommaga ochiq bo‘ladi, ayniqsa agar API tashqi ishlab chiquvchilar foydalanishi uchun mo‘ljallangan bo‘lsa. Shu sababli, rekognitsiyani (recon) boshlashda avvalo hujjatlarni ko‘rib chiqish kerak.

---

#### API hujjatlarini topish

Agar API hujjatlari ochiq bo‘lmasa ham, uni API’dan foydalanuvchi ilovalarni ko‘zdan kechirish orqali topish mumkin.

Buning uchun siz:

* **Burp Scanner** yordamida API’ni crawl qilish mumkin.
* Yoki **Burp browser** orqali ilovani qo‘lda ko‘zdan kechirish mumkin.

Hujjatlarga ishora qilishi mumkin bo‘lgan endpointlarga e’tibor bering, masalan:

```
/api
/swagger/index.html
/openapi.json
```

Agar biror resurs endpoint topilsa, uning **base path** qismini ham tekshirish kerak. Masalan, agar siz:

```
/api/swagger/v1/users/123
```

endpointini topsangiz, quyidagilarni ham tekshirish lozim:

```
/api/swagger/v1
/api/swagger
/api
```

Mashina tomonidan o‘qiladigan hujjatlardan foydalanish
Siz topgan har qanday mashina tomonidan o‘qiladigan API hujjatlarini tahlil qilish uchun turli avtomatlashtirilgan vositalardan foydalanishingiz mumkin.

Siz **Burp Scanner** yordamida OpenAPI hujjatlarini yoki JSON yoki YAML formatidagi boshqa hujjatlarni ko‘rib chiqishingiz va audit qilishingiz mumkin. Shuningdek, OpenAPI hujjatlarini **OpenAPI Parser BApp** orqali ham tahlil qilishingiz mumkin.

Bundan tashqari, hujjatlashtirilgan endpointlarni sinovdan o‘tkazish uchun **Postman** yoki **SoapUI** kabi maxsus vositalardan ham foydalanish imkoniyati mavjud.


Bundan tashqari, **Intruder** yordamida keng tarqalgan path’lar ro‘yxatini tekshirib hujjatlarni topish mumkin.
