Server-side parameter pollution
Ba’zi tizimlarda internet orqali bevosita kira olmaydigan ichki API’lar mavjud bo‘ladi. **Server-side parameter pollution** (server tomonida parametr ifloslanishi) shunda yuzaga keladiki, veb-sayt foydalanuvchi kiritgan qiymatni yetarlicha kodlashsiz ichki API’ga yuboriladigan server so‘roviga qo‘shib yuboradi. Bu esa hujumchiga quyidagi imkoniyatlarni berishi mumkin:

* Mavjud parametrlarni o‘zgartirish.
* Ilovaning xatti-harakatini o‘zgartirish.
* Ruxsatsiz ma’lumotlarga kirish.

Har qanday foydalanuvchi kiritishini parametr ifloslanishiga tekshirish mumkin. Masalan, query parametrlar, formadagi maydonlar, header’lar va URL path parametrlarining barchasi zaif bo‘lishi mumkin.

### Server-side parameter pollution misol

**Eslatma**
Ushbu zaiflik ba’zida *HTTP parameter pollution* deb ham ataladi. Biroq bu atama ko‘pincha veb-ilova firewall’ini (WAF) chetlab o‘tish texnikasiga nisbatan ham ishlatiladi. Shuning uchun chalkashlik bo‘lmasligi uchun bu mavzuda biz faqat *server-side parameter pollution* atamasidan foydalanamiz.

Shuningdek, nomi o‘xshash bo‘lsa-da, ushbu zaiflik sinfi *server-side prototype pollution* bilan deyarli bog‘liq emas.

### Query string’da server-side parameter pollution’ni tekshirish

Query string’da server-side parameter pollution’ni tekshirish uchun input qiymatingizga `#`, `&`, va `=` kabi query sintaksis belgilarini qo‘shib, ilovaning qanday javob qaytarishini kuzating.

Faraz qilaylik, zaif ilova foydalanuvchilarning username’iga qarab qidirish imkonini beradi. Siz qidiruv bajarganingizda, brauzer quyidagi so‘rovni yuboradi:

```
GET /userSearch?name=peter&back=/home
```

Server foydalanuvchi ma’lumotini olish uchun ichki API’ga quyidagi so‘rovni yuboradi:

```
GET /users/search?name=peter&publicProfile=true
```

---

### Query string’ni kesish (Truncating)

Siz URL-encoded `#` belgisidan foydalanib, server tomonidagi so‘rovni kesishga urinib ko‘rishingiz mumkin. Natijani tushunishga yordam berish uchun `#` belgisidan keyin matn qo‘shishingiz ham mumkin.

Masalan, query string’ni quyidagicha o‘zgartirasiz:

```
GET /userSearch?name=peter%23foo&back=/home
```

Frontend quyidagi URL’ni chaqirishga urinadi:

```
GET /users/search?name=peter#foo&publicProfile=true
```

**Eslatma:** `#` belgisini URL-encode qilish muhim. Aks holda frontend uni fragment identifikatori sifatida talqin qiladi va ichki API’ga uzatilmaydi.

Javobni ko‘rib chiqing va query kesilgan-kesilmaganini aniqlang. Masalan:

* Agar javobda foydalanuvchi **peter** qaytsa, ehtimol query kesilgan bo‘lishi mumkin.
* Agar **Invalid name** xatosi qaytsa, demak `foo` foydalanuvchi nomining bir qismi sifatida qabul qilingan va so‘rov kesilmagan.

Agar siz server-side so‘rovni kesishga muvaffaq bo‘lsangiz, bu `publicProfile=true` maydonining shart emasligini anglatadi. Natijada siz maxfiy (non-public) profillarga kirishingiz mumkin bo‘ladi.

---

### Yaroqsiz parametrlarni kiritish

Siz URL-encoded `&` belgisidan foydalanib, server so‘roviga qo‘shimcha parametr qo‘shishga urinib ko‘rishingiz mumkin.

Masalan:

```
GET /userSearch?name=peter%26foo=xyz&back=/home
```

Bu ichki API’ga quyidagi so‘rovni yuborishga olib keladi:

```
GET /users/search?name=peter&foo=xyz&publicProfile=true
```

Javobni tahlil qiling:

* Agar javob o‘zgarmasa, demak parametr injeksiya qilingan, lekin ilova uni e’tiborsiz qoldirgan bo‘lishi mumkin.

To‘liq tasavvurga ega bo‘lish uchun qo‘shimcha testlar o‘tkazish zarur.

---

### Yaroqli parametrlarni kiritish

Agar siz query string’ni o‘zgartirishga muvaffaq bo‘lsangiz, server so‘roviga qo‘shimcha **yaroqli** parametr qo‘shishga urinib ko‘rishingiz mumkin.

Masalan, siz **email** parametrini topgan bo‘lsangiz, quyidagicha qo‘shasiz:

```
GET /userSearch?name=peter%26email=foo&back=/home
```

Natijada server quyidagi so‘rovni yuboradi:

```
GET /users/search?name=peter&email=foo&publicProfile=true
```

Javobdan qo‘shimcha parametr qanday tahlil qilinganini aniqlash mumkin.

---

### Mavjud parametrlarni almashtirish

Ilova server-side parameter pollution’ga zaifligini aniqlash uchun siz mavjud parametrni **almashtirib ko‘rishingiz** mumkin. Buning uchun bir xil nomdagi ikkinchi parametrni qo‘shasiz.

Masalan:

```
GET /userSearch?name=peter%26name=carlos&back=/home
```

Bu server tomonidagi ichki API’ga quyidagi so‘rovni yuboradi:

```
GET /users/search?name=peter&name=carlos&publicProfile=true
```

Endi ichki API ikkita `name` parametrini ko‘radi. Natija ilova ishlayotgan texnologiyaga bog‘liq:

* **PHP** → faqat oxirgi parametrni o‘qiydi → qidiruv `carlos` bo‘yicha bajariladi.
* **ASP.NET** → ikkala parametrni birlashtiradi → qidiruv `peter,carlos` bo‘yicha bajariladi → `Invalid username` xatosi bo‘lishi mumkin.
* **Node.js / Express** → faqat birinchi parametrni o‘qiydi → qidiruv `peter` bo‘yicha bajariladi → natija o‘zgarmaydi.

Agar siz asl parametrni almashtirishga muvaffaq bo‘lsangiz, bundan foydalanib hujum qilishingiz mumkin. Masalan:

```
name=administrator
```

ni qo‘shib yuborsangiz, **administrator** foydalanuvchisi sifatida tizimga kirish imkoniga ega bo‘lishingiz mumkin.
