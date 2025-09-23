Referer-ga asoslangan CSRF himoyasini aylanib oʻtish

CSRF tokenlardan foydalanadigan himoyalardan tashqari, baʼzi ilovalar CSRF hujumlariga qarshi kurashish maqsadida HTTP Referer sarlavhasidan foydalanadi — odatda soʻrov ilovaning oʻz domenidan kelganligini tekshirish orqali. Bunday yondashuv odatda kamroq samarali boʻlib, koʻpincha aylanib oʻtilishi mumkin.

Referer sarlavhasi

HTTP Referer sarlavhasi (HTTP spetsifikatsiyasida tasodifan notoʻgʻri imlolangan) — talab ichiga kiritiluvchi ixtiyoriy sarlavha boʻlib, soʻralayotgan resursga havola qilgan veb-sahifaning URL manzilini oʻz ichiga oladi. Brauzerlar odatda foydalanuvchi HTTP soʻrovi ishga tushirganida (masalan, havolani bosganda yoki formani yuborishda) uni avtomatik qoʻshadi. Havola beruvchi sahifa Referer sarlavhasining qiymatini yashirish yoki oʻzgartirishga imkon beruvchi turli usullar mavjud. Koʻpincha bunday amallar maxfiylik sabablariga koʻra amalga oshiriladi.

Referer tekshiruvi sarlavha mavjud bo‘lishiga bog‘liq

Baʼzi ilovalar so‘rovlarda Referer sarlavhasi mavjud bo‘lsa uni tekshiradi, lekin agar sarlavha yo‘q bo‘lsa tekshiruvni o‘tkazib yuboradi.

Bunday vaziyatda hujumchi CSRF eksploitini shunday qilib tayyorlaydiki, qurbon foydalanuvchining brauzeri so‘rov yuborilganda Referer sarlavhasini olib tashlaydi. Buni amalga oshirishning turli usullari mavjud, eng osonlaridan biri — CSRF hujumi joylashgan HTML sahifaga quyidagi META tegini qo‘yish:

```html
<meta name="referrer" content="never">
```

Referer tekshiruvidan aylanib o‘tish mumkin

Baʼzi ilovalar Referer sarlavhasini sodda, xato usulda tekshiradi va bu aylanib o‘tishga imkon beradi. Masalan, ilova Referer ichidagi domen kutilgan qiymatdan boshlanishini tekshirsa, hujumchi quyidagi kabi o‘z domenining subdomeni sifatida kerakli qiymatni joylashtirishi mumkin:

```
http://vulnerable-website.com.attacker-website.com/csrf-attack
```

Xuddi shunday, agar ilova Referer ichida o‘z domen nomi mavjudligini oddiygina tekshirsa, hujumchi kerakli qiymatni URL ning boshqa qismiga joylashtirishi mumkin:

```
http://attacker-website.com/csrf-attack?vulnerable-website.com
```

Eslatma
Burp kabi vositalarda bunday xulq-atvorni aniqlashingiz mumkin, lekin ko‘pincha brauzerda proof-of-conceptni sinab ko‘rganingizda bu usul ishlamay qoladi. Maxfiy maʼlumotlarning shunday yo‘l bilan sizilish xavfini kamaytirish maqsadida ko‘pgina brauzerlar Referer sarlavhasidan so‘rov qatori (query string) ni sukut bo‘yicha olib tashlaydi.

Siz bu xulq-atvorni o‘zgartirish uchun ekspluitni yuboruvchi javobga quyidagi sarlavhani qo‘yishingiz mumkin:

```
Referrer-Policy: unsafe-url
```

(izoh: bu yerda “Referrer” so‘zi to‘g‘ri imlolangan — shunchaki eʼtiboringizni qaratish uchun). Bu sarlavha to‘liq URL, ayniqsa query string ham yuborilishini taʼminlaydi.
