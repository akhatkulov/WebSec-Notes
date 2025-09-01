Clickjacking hujumlaridan himoyalanish
Biz brauzer tomonida keng qo‘llaniladigan himoya mexanizmlaridan biri — **frame busting** skriptlarini muhokama qildik. Biroq, hujumchi ko‘pincha bunday himoyani chetlab o‘tishi oson bo‘ladi. Shu sababli, brauzerda iframe ishlatilishini cheklaydigan va clickjacking hujumlarini kamaytiradigan **server tomonidan boshqariladigan protokollar** ishlab chiqilgan.

Clickjacking brauzer tomonida sodir bo‘ladigan xatti-harakat bo‘lib, uning muvaffaqiyati brauzer funksionalligiga, amaldagi veb-standartlarga va eng yaxshi amaliyotlarga rioya qilishga bog‘liq. Clickjacking’ga qarshi server tomonida himoya esa iframe kabi komponentlardan foydalanishga cheklovlarni belgilash va ularni brauzerga yetkazish orqali amalga oshiriladi. Ammo himoya mexanizmlarining ishlashi brauzerning ularni to‘liq qo‘llashiga bog‘liq. Server tomonidan clickjacking’ga qarshi ikki asosiy mexanizm mavjud: **X-Frame-Options** va **Content Security Policy (CSP)**.

---

### X-Frame-Options

X-Frame-Options dastlab Internet Explorer 8’da norasmiy javob sarlavhasi sifatida joriy etilgan va tezda boshqa brauzerlar tomonidan ham qabul qilingan. Bu header veb-sayt egasiga iframe yoki object orqali sahifani ramkaga joylashtirishni nazorat qilish imkonini beradi. Masalan:

* Sahifani butunlay ramkaga joylashtirishni taqiqlash:

  ```
  X-Frame-Options: deny
  ```

* Faqatgina o‘sha saytdagi (bir xil domenli) ramkalarga ruxsat berish:

  ```
  X-Frame-Options: sameorigin
  ```

* Faqat ma’lum bir sayt uchun ruxsat berish:

  ```
  X-Frame-Options: allow-from https://normal-website.com
  ```

Biroq X-Frame-Options barcha brauzerlarda bir xil qo‘llanilmaydi (masalan, `allow-from` Chrome 76 va Safari 12’da qo‘llab-quvvatlanmaydi). Shunga qaramay, **Content Security Policy** bilan birgalikda ko‘p qatlamli himoya strategiyasining bir qismi sifatida to‘g‘ri qo‘llansa, clickjacking hujumlariga qarshi samarali himoya bo‘la oladi.

---

### Content Security Policy (CSP)

**Content Security Policy (CSP)** — bu XSS va clickjacking kabi hujumlarga qarshi aniqlash va oldini olish mexanizmi. CSP odatda veb-serverda javob headeri sifatida qo‘llanadi:

```
Content-Security-Policy: policy
```

Bu yerda `policy` — nuqta-vergul bilan ajratilgan siyosat direktivalari qatoridir. CSP brauzerga qaysi manbalardan resurslarni yuklash mumkinligini ko‘rsatib beradi va zararli xatti-harakatlarni aniqlash va to‘sishga yordam beradi.

#### Clickjacking’ga qarshi CSP

Clickjacking’ga qarshi tavsiya etilgan usul — **frame-ancestors** direktivasidan foydalanish.

* `frame-ancestors 'none'` → `X-Frame-Options: deny` bilan bir xil.
* `frame-ancestors 'self'` → `X-Frame-Options: sameorigin` bilan deyarli bir xil.

Masalan, faqat o‘z domeningizga ruxsat berish:

```
Content-Security-Policy: frame-ancestors 'self';
```

Yoki faqat ma’lum sayt uchun ruxsat berish:

```
Content-Security-Policy: frame-ancestors normal-website.com;
```

CSP samarali bo‘lishi uchun ularni ehtiyotkorlik bilan ishlab chiqish, to‘g‘ri joriy qilish va sinovdan o‘tkazish zarur. Bundan tashqari, CSP’ni **ko‘p qatlamli himoya strategiyasi**ning bir qismi sifatida qo‘llash tavsiya etiladi.
