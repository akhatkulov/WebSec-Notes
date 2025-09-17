

### SameSite cookie cheklovlarini chetlab o‘tish

**SameSite** — bu brauzer xavfsizlik mexanizmi bo‘lib, boshqa veb-saytlardan yuborilgan so‘rovlar tarkibiga cookie’larning qachon kiritilishini belgilaydi. SameSite cookie cheklovlari CSRF, cross-site leak (ma’lumot oqishi) va ayrim CORS ekspluatlari kabi turli cross-site hujumlarga qisman himoya taqdim etadi.

2021-yildan beri Chrome, agar veb-sayt cookie uchun o‘z cheklov darajasini aniq belgilamagan bo‘lsa, **Lax SameSite** cheklovini sukut bo‘yicha qo‘llaydi. Bu taklif qilingan standart bo‘lib, boshqa yirik brauzerlar ham kelajakda uni qabul qilishi kutilmoqda. Shuning uchun bu cheklovlarning qanday ishlashini hamda qanday qilib ularni chetlab o‘tish mumkinligini yaxshi tushunish muhimdir. Faqatgina shundagina cross-site hujum vektorlarini to‘liq tekshirish mumkin bo‘ladi.

---

### SameSite cookie’lari kontekstida “site” nima?

SameSite cookie cheklovlari kontekstida **site** — bu yuqori darajadagi domen (TLD), masalan `.com` yoki `.net`, va unga qo‘shilgan yana bitta daraja. Bu ko‘pincha **TLD+1** deb ataladi.

So‘rovning same-site yoki cross-site ekanini aniqlashda **URL sxemasi (http/https)** ham hisobga olinadi. Demak, `http://app.example.com` dan `https://app.example.com` ga havola yuborish ko‘pchilik brauzerlarda **cross-site** sifatida ko‘riladi.

---

### SameSite cookie uchun site nima?

Ba’zan siz **“effective top-level domain” (eTLD)** atamasiga duch kelishingiz mumkin. Bu aslida ko‘p bo‘lakli domen qo‘shimchalarini ham yuqori darajadagi domen sifatida hisoblash usulidir. Masalan, `.co.uk`.

---

### SameSite qanday ishlaydi?

SameSite mexanizmi kiritilishidan oldin, brauzerlar cookie’larni doimiy ravishda, hatto butunlay aloqasi yo‘q bo‘lgan uchinchi tomon saytlaridan kelgan so‘rovlar uchun ham yuborar edi.

SameSite mexanizmi brauzerlarga va sayt egalariga cookie’larning qaysi cross-site so‘rovlarda yuborilishi mumkinligini cheklash imkonini beradi. Bu foydalanuvchilarni **CSRF hujumlari**dan himoya qilishda yordam beradi. CSRF odatda qurbon brauzerini autentifikatsiya cookie’sini ishlatgan holda zararli so‘rov yuborishga majbur qiladi. Agar cookie yuborilmasa, hujum muvaffaqiyatsiz bo‘ladi.

Hozirda barcha yirik brauzerlar quyidagi SameSite cheklov darajalarini qo‘llab-quvvatlaydi:

* **Strict**
* **Lax**
* **None**

Dasturchilar cookie yaratishda **SameSite atributini** qo‘shib, har bir cookie uchun mos cheklov darajasini qo‘lda sozlashlari mumkin. Masalan:

```
Set-Cookie: session=0F8tgdOhi9ynR1M9wa3ODa; SameSite=Strict
```

---

### SameSite darajalari

#### Strict

Agar cookie `SameSite=Strict` bilan yaratilgan bo‘lsa, u **hech qanday cross-site so‘rovga yuborilmaydi**. Ya’ni, agar so‘rov yuborilayotgan sayt brauzer adres satrida ko‘rinayotgan saytga mos kelmasa, cookie yuborilmaydi.
Bu eng xavfsiz variant bo‘lsa-da, cross-site funksionallikka ehtiyoj bo‘lgan holatlarda foydalanuvchi tajribasiga salbiy ta’sir qilishi mumkin.

---

#### Lax

**Lax SameSite** cheklovida cookie faqat quyidagi shartlar bajarilganda yuboriladi:

1. So‘rov **GET** metodi orqali yuborilgan bo‘lsa.
2. So‘rov foydalanuvchi tomonidan amalga oshirilgan **top-level navigatsiya** (masalan, havolaga bosish) orqali bo‘lsa.

Bu esa POST so‘rovlarda cookie yuborilmasligini anglatadi. POST odatda ma’lumotlarni o‘zgartirish yoki xavfliroq amallar uchun ishlatilgani sababli, bu CSRF hujumlarini cheklashda muhim rol o‘ynaydi.

Cookie shuningdek **skript, iframe, rasm yoki boshqa resurslar orqali** yuboriladigan fon so‘rovlarda ham qo‘shilmaydi.

---

#### None

Agar cookie `SameSite=None` atributi bilan yaratilgan bo‘lsa, **SameSite cheklovlari butunlay o‘chirib qo‘yiladi**. Cookie barcha so‘rovlarda yuboriladi, hatto uchinchi tomon saytlaridan kelgan so‘rovlarda ham.

Shu bois Chrome bundan mustasno, boshqa yirik brauzerlar **SameSite atributi belgilanmagan cookie**larga sukut bo‘yicha shunday munosabatda bo‘ladi.

Lekin, `SameSite=None` ishlatilganda cookie faqat **HTTPS orqali** yuborilishi uchun `Secure` atributi ham qo‘shilishi shart:

```
Set-Cookie: trackingId=0F8tgdOhi9ynR1M9wa3ODa; SameSite=None; Secure
```
