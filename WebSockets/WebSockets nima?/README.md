### WebSockets nima?

**WebSockets** – bu ikki tomonlama, to‘liq dupleks aloqani ta’minlaydigan protokoldir, u dastlab **HTTP orqali ishga tushiriladi**. U zamonaviy veb-ilovalarda oqimli ma’lumot uzatish va boshqa asinxron trafik uchun keng qo‘llaniladi.

Quyida biz HTTP va WebSockets o‘rtasidagi farqlarni tushuntiramiz, WebSocket ulanishlari qanday o‘rnatilishini ko‘rib chiqamiz va WebSocket xabarlari qanday ko‘rinishda bo‘lishini bayon qilamiz.

---

### HTTP va WebSockets o‘rtasidagi farq nima?

Ko‘pgina brauzer va sayt o‘rtasidagi aloqa **HTTP** orqali amalga oshadi. HTTP’da mijoz (client) so‘rov yuboradi va server javob qaytaradi. Odatda javob darhol keladi va tranzaksiya tugaydi. Tarmoqqa ulanish ochiq qolgan taqdirda ham, keyingi aloqalar alohida so‘rov va javob shaklida bo‘ladi.

Ba’zi zamonaviy veb-saytlar esa **WebSockets** dan foydalanadi. WebSocket ulanishlari HTTP orqali ishga tushadi va odatda uzoq muddat ochiq turadi. Xabarlarni har ikki tomondan xohlagan paytda yuborish mumkin va ular tranzaksiyaviy emas. Ulanish odatda mijoz yoki server xabar yuborguncha ochiq va faol bo‘ladi.

WebSockets ayniqsa past kechikish (low-latency) yoki server tashabbusi bilan yuboriladigan xabarlar kerak bo‘lgan holatlarda foydali, masalan **real vaqt rejimidagi moliyaviy ma’lumot oqimlari**da.

---

### WebSocket ulanishlari qanday o‘rnatiladi?

WebSocket ulanishlari odatda mijoz tomonda JavaScript orqali yaratiladi:

```javascript
var ws = new WebSocket("wss://normal-website.com/chat");
```

> **Eslatma:**
>
> * **wss** – TLS orqali shifrlangan WebSocket ulanishini bildiradi.
> * **ws** – shifrlanmagan oddiy ulanishni bildiradi.

Ulanishni o‘rnatish uchun brauzer va server **WebSocket qo‘l siqish** (handshake) jarayonini HTTP orqali bajaradi.

Brauzer so‘rov yuboradi:

```
GET /chat HTTP/1.1
Host: normal-website.com
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: wDqumtseNBJdhkihL6PW7w==
Connection: keep-alive, Upgrade
Cookie: session=KOsEJNuflw4Rd9BDNrVmvwBF9rEijeE2
Upgrade: websocket
```

Agar server qabul qilsa, javob qaytaradi:

```
HTTP/1.1 101 Switching Protocols
Connection: Upgrade
Upgrade: websocket
Sec-WebSocket-Accept: 0FFP+2nmNIf/h+4BP36k9uzrYGk=
```

Shundan so‘ng, tarmoq ulanishi ochiq qoladi va WebSocket xabarlari har ikki tomonga yuborilishi mumkin.

> **Muhim nuqtalar:**
>
> * `Connection` va `Upgrade` headerlari bu WebSocket qo‘l siqish ekanini bildiradi.
> * `Sec-WebSocket-Version` mijoz foydalanmoqchi bo‘lgan protokol versiyasini ko‘rsatadi (odatda 13).
> * `Sec-WebSocket-Key` – Base64 formatida random qiymat bo‘lib, har bir so‘rovda qayta yaratiladi.
> * `Sec-WebSocket-Accept` – mijoz yuborgan kalitga maxsus satr qo‘shilib, hash hosil qilinadi. Bu noto‘g‘ri sozlangan server yoki caching-proxy tufayli yuzaga keladigan noto‘g‘ri javoblarning oldini oladi.

---

### WebSocket xabarlari qanday ko‘rinadi?

WebSocket ulanishi o‘rnatilgandan so‘ng, xabarlarni mijoz ham, server ham asinxron tarzda yuborishi mumkin.

Oddiy xabar yuborish misoli:

```javascript
ws.send("Peter Wiener");
```

Amalda, WebSocket xabarlari istalgan formatdagi ma’lumotni o‘z ichiga olishi mumkin. Zamonaviy ilovalarda odatda **JSON** ishlatiladi, chunki u tuzilmali ma’lumot uzatishda qulay.

Masalan, chat-bot ilovasida xabar quyidagicha bo‘lishi mumkin:

```json
{"user":"Hal Pline","content":"Men bolaligimda Playstation bo‘lishni xohlardim, sizning bemaza savollaringizga javob beradigan qurilma emas"}
```

