### WebSockets xavfsizlik zaifliklarini sinash

Ushbu bo‘limda biz WebSocket xabarlarini va ulanishlarini qanday manipulyatsiya qilishni, WebSockets bilan bog‘liq qanday xavfsizlik zaifliklari paydo bo‘lishi mumkinligini va WebSockets zaifliklarini ekspluatatsiya qilish misollarini tushuntiramiz.

---

### WebSockets

WebSockets zamonaviy veb-ilovalarda keng qo‘llaniladi. Ular HTTP orqali ishga tushiriladi va ikki tomonga asinxron xabar almashinishga ega bo‘lgan uzoq muddatli ulanishlarni ta’minlaydi.

WebSockets turli maqsadlarda ishlatiladi, jumladan foydalanuvchi harakatlarini bajarish va sezgir ma’lumotlarni uzatish uchun. Amalda, oddiy HTTP bilan yuzaga keladigan deyarli har qanday veb-xavfsizlik zaifligi WebSockets orqali ham paydo bo‘lishi mumkin.

---

### Qo‘shimcha o‘qish

**WebSockets nima?**
**WebSockets laboratoriyalari**
Agar siz WebSockets zaifliklarining asosiy tushunchalarini bilsangiz va ularni haqiqiy, qasddan zaif maqsadlarda ekspluatatsiya qilishni mashq qilmoqchi bo‘lsangiz, ushbu mavzudagi barcha laboratoriyalarga quyidagi havola orqali kirishingiz mumkin.

**Barcha WebSockets laboratoriyalarini ko‘rish**

---

### WebSocket trafikini manipulyatsiya qilish

WebSockets xavfsizlik zaifliklarini topishda ularni dastur kutmagan tarzda manipulyatsiya qilish talab etiladi. Buni Burp Suite yordamida amalga oshirish mumkin.

Burp Suite yordamida quyidagilarni qilishingiz mumkin:

* WebSocket xabarlarini ushlash va o‘zgartirish.
* WebSocket xabarlarini qayta o‘tkazish va yangi xabarlar yaratish.
* WebSocket ulanishlarini manipulyatsiya qilish.

---

### WebSocket xabarlarini ushlash va o‘zgartirish

WebSocket xabarlarini Burp Proxy yordamida ushlash va o‘zgartirish mumkin, quyidagicha:

1. Burp’ning brauzerini oching.
2. WebSockets ishlatiladigan ilova funksiyasiga o‘tib, WebSockets Proxy tarixida yozuvlar paydo bo‘layotganini tekshiring.
3. Burp Proxy’ning Intercept (Ushlash) oynasida interception yoqilganligiga ishonch hosil qiling.
4. Brauzer yoki server xabar yuborganida u Intercept oynasida ko‘rinadi — uni ko‘rib chiqib yoki o‘zgartirib Forward tugmasi bilan yuboring.

> **Eslatma:** Burp Proxy’da mijoz→server yoki server→mijoz xabarlarini qaysi biri ushlanishini sozlashingiz mumkin. Buni Settings → WebSocket interception rules sozlamalarida bajarish mumkin.

---

### Xabarlarni qayta o‘tkazish va yangi xabarlar yaratish

WebSocket xabarlarini real-vaqtda ushlashdan tashqari, alohida xabarlarni qayta o‘tkazish va yangi xabarlar yaratish ham mumkin. Buni Burp Repeater yordamida bajarish mumkin:

1. Burp Proxy’da WebSockets tarixidan yoki Intercept oynasidan xabarni tanlab, kontekst menyusidan **Send to Repeater** ni tanlang.
2. Burp Repeater’da tanlangan xabarni tahrirlashingiz va uni qayta-qayta yuborishingiz mumkin.
3. Yangi xabar kiritib, uni mijoz yoki serverga yuborishingiz mumkin.
4. Burp Repeater’ning **History** panelida WebSocket ulanishi davomida yuborilgan barcha xabarlar (siz yaratganlari va brauzer/server yuborganlari) ko‘rsatiladi.
5. Tarix panelidagi har qanday xabarni tahrirlab qayta yubormoqchi bo‘lsangiz, xabarni tanlab **Edit and resend** ni tanlang.

---

### WebSocket ulanishlarini manipulyatsiya qilish

Xabarlarni manipulyatsiya qilishdan tashqari, ba’zida WebSocket qo‘l siqishni (handshake) ham manipulyatsiya qilish kerak bo‘ladi.

Bunday hollarda manipulyatsiya qilish kerak bo‘lishi mumkin, masalan:

* Qo‘shimcha attack surface ga erishish.
* Ba’zi hujumlar ulanishni tushirib qo‘yishi va siz yangi ulanish o‘rnatishingiz kerak bo‘lishi.
* Dastlabki qo‘l siqish so‘rovidagi tokenlar yoki boshqa ma’lumotlar eskirgan bo‘lishi mumkin.

Burp Repeater yordamida WebSocket qo‘l siqishni quyidagicha manipulyatsiya qilishingiz mumkin:

1. Avval aytilganidek, WebSocket xabarini Burp Repeater’ga yuboring.
2. Burp Repeater’da WebSocket URL yonidagi qalam (pencil) ikonkasini bosing. Bu sizga mavjud bog‘langan WebSocket’ga ulanish, bog‘langan WebSocket’ni klonlash yoki uzilgan WebSocket’ga qayta ulanish imkonini beruvchi vedio (wizard) oynasini ochadi.
3. Agar siz klonlash yoki qayta ulanishni tanlasangiz, vedio qo‘l siqish so‘rovining to‘liq tafsilotlarini ko‘rsatadi va ularni qo‘l siqish bajarilishidan oldin tahrirlash imkonini beradi.
4. **Connect** ni bosganingizda, Burp sozlangan qo‘l siqishni bajarishga harakat qiladi va natijani ko‘rsatadi. Agar yangi WebSocket ulanishi muvaffaqiyatli o‘rnatilsa, uni Burp Repeater orqali yangi xabarlar yuborishda ishlatishingiz mumkin.

---

### WebSockets xavfsizlik zaifliklari

Nazariy jihatdan, WebSockets bilan bog‘liq deyarli har qanday veb xavfsizlik zaifligi paydo bo‘lishi mumkin:

* Foydalanuvchi tomonidan kiritilgan ma’lumot server tarafida xavfsiz bo‘lmagan tarzda qayta ishlansa, SQL injection yoki XML external entity injection kabi zaifliklar paydo bo‘lishi mumkin.
* Ba’zi blind (ko‘rinmas) zaifliklar faqat out-of-band (OAST) texnikalari orqali aniqlanishi mumkin.
* Agar hujumchi nazoratidagi ma’lumotlar WebSockets orqali boshqa foydalanuvchilarga uzatilsa, bu XSS yoki boshqa mijoz tarafdagi zaifliklarga olib kelishi mumkin.

---

### Zaifliklarni ekspluatatsiya qilish uchun WebSocket xabarlarini manipulyatsiya qilish

WebSockets’ga taalluqli input-asoslangan zaifliklarning ko‘pchiligi xabar mazmunini buzish orqali topiladi va ekspluatatsiya qilinadi.

Masalan, chat ilovasi WebSockets orqali chat xabarlarini yuborsa, foydalanuvchi xabarini serverga quyidagi kabi xabar yuborilishi mumkin:

```json
{"message":"Hello Carlos"}
```

Bu xabar server orqali boshqa chat foydalanuvchisiga uzatiladi va brauzerda quyidagicha render qilinishi mumkin:

```html
<td>Hello Carlos</td>
```

Agar boshqa hech qanday input tekshiruvlari yoki himoyalar mavjud bo‘lmasa, hujumchi quyidagi WebSocket xabarini yuborib XSS PoC (proof-of-concept) bajarishi mumkin:

```json
{"message":"<img src=1 onerror='alert(1)'>"}
```

---

### WebSocket qo‘l siqishni manipulyatsiya qilib zaifliklarni ekspluatatsiya qilish

Ba’zi WebSockets zaifliklari faqat qo‘l siqishni manipulyatsiya qilish orqali topilishi mumkin. Bunday zaifliklar ko‘proq dizayn xatoliklariga bog‘liq bo‘ladi, masalan:

* HTTP headerlariga nisbatan noto‘g‘ri ishonch (masalan `X-Forwarded-For`) orqali xavfsizlik qarorlarini qabul qilish.
* Sessiya boshqaruvining xatolari, chunki WebSocket xabarlarining qanday sessiya kontekstida qayta ishlanishi odatda qo‘l siqish so‘rovi sessiya kontekstiga bog‘liq bo‘ladi.
* Ilova tomonidan ishlatiladigan maxsus HTTP headerlar tufayli paydo bo‘ladigan attack surface.

---

### Cross-site WebSockets orqali ekspluatatsiya qilish

Ba’zi WebSockets xavfsizlik zaifliklari hujumchi boshqaradigan veb-saytdan cross-domain WebSocket ulanishini amalga oshirishda paydo bo‘ladi. Buni **cross-site WebSocket hijacking** (CSWSH) deb atashadi va u WebSocket qo‘l siqishidagi CSRF zaifligidan foydalanishni o‘z ichiga oladi. Ushbu hujum ko‘pincha jiddiy oqibatlarga olib keladi: hujumchi qurbon foydalanuvchi nomidan imtiyozli harakatlarni bajarishi yoki qurbonning ko‘ra oladigan sezgir ma’lumotlarni egallashi mumkin.

**Qo‘shimcha o‘qish:** Cross-site WebSockets hijacking

---

### WebSocket ulanishini qanday himoyalash kerak

WebSockets bilan bog‘liq xavfsizlik xatarlarini kamaytirish uchun quyidagi tavsiyalarni bajaring:

* Har doim **wss\://** (TLS orqali) protokolidan foydalaning.
* WebSocket endpoint’ining URL manzilini kod ichiga (hard code) yozib qo‘ying va unga foydalanuvchi boshqaradigan ma’lumotlarni qo‘shmang.
* WebSocket qo‘l siqish so‘rovini CSRF dan himoyalang, shunda cross-site WebSocket hijacking zaifligi paydo bo‘lmaydi.
* WebSocket orqali olingan ma’lumotni ikki tomonda ham ishonchsiz (untrusted) deb hisoblang. Server va mijoz tomonida ma’lumotlarni xavfsiz tarzda qayta ishlang, shu bilan SQL injection va XSS kabi input-asoslangan zaifliklarning oldini oling.
