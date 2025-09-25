

### Server tarafidagi prototip ifloslanishi

JavaScript dastlab brauzerlarda bajariladigan mijoz (client)-tomon tili sifatida yaratilgan. Biroq, Node.js kabi juda mashhur server-tomon muhitlar paydo bo‘lishi bilan JavaScript endi serverlar, API’lar va boshqa back-end ilovalarini yaratishda keng foydalanilmoqda. Mantiqan, server-tomon kontekstlarda ham prototip ifloslanishi zaifliklari paydo bo‘lishi mumkin.

Asosiy tushunchalar ko‘pchilik hollarda o‘xshash bo‘lsa-da, server-tomon prototip ifloslanishini aniqlash va uni ishlaydigan ekspluatatsiyaga aylantirish jarayoni bir qancha qo‘shimcha qiyinchiliklarni tug‘diradi.

Ushbu bo‘limda siz server-tomon prototip ifloslanishini qora quti (black-box) usulida aniqlash uchun bir nechta texnikalarni o‘rganasiz. Biz buni samarali va zararsiz (non-destructive) usullarda qanday sinashni ko‘rsatamiz, so‘ngra prototip ifloslanishidan masofadan kod ishga tushirish (RCE) ga qanday o‘tish mumkinligini ko‘rsatadigan maqsadli zaif laboratoriyalar orqali amaliy misollarni ko‘ramiz.

#### Nima uchun server-tomon prototip ifloslanishini aniqlash qiyinroq?

Bir necha sababga ko‘ra, server-tomon prototip ifloslanishini aniqlash odatda mijoz-tomon variantga nisbatan qiyinroq:

* **Kodga kirish yo‘qligi** — Mijoz-tomon zaifliklarda bo‘lgani kabi, siz ko‘pincha zaif JavaScript kodiga kirish imkoniga ega emassiz. Bu qaysi "sink"lar mavjudligini yoki potensial gadget xususiyatlarini aniqlashni qiyinlashtiradi.
* **Developerlarga mo‘ljallangan asboblar yo‘qligi** — JavaScript masofaviy tizimda ishlayotganligi uchun, brauzer DevTools kabi vositalar bilan obyektlarni ish vaqtida tekshira olmaysiz. Bu esa prototip ifloslanganini aniqlashni qiyinlashtiradi — odatda bu faqat sayt xulqida sezilarli o‘zgarish bo‘lganda ko‘rinadi. (Bu cheklov white-box testlashga taalluqli emas.)
* **DoS muammosi** — Server-tomon muhitda haqiqiy xususiyatlar bilan muvaffaqiyatli tarzda prototipni ifloslash ilova funksionalligini buzishi yoki butun serverni o‘chirib qo‘yishi mumkin. Ishlab chiqishda tasodifan xizmatni to‘xtatib qo‘yish (DoS) oson. Hatto agar zaiflik aniqlansa ham, agar siz saytni buzib yuborgan bo‘lsangiz, uni ekspluatatsiyaga aylantirish ham murakkab bo‘ladi.
* **Ifloslanish saqlanib qolishi** — Brauzerda sinashda siz barcha o‘zgarishlarni sahifani yangilab tozalashingiz mumkin. Server-tomon prototipni ifloslaganingizda esa bu o‘zgarish Node jarayonining umr bo‘yi davomida saqlanadi va sizda uni qayta tiklash imkoniyati yo‘q.

Keyingi bo‘limlarda biz ushbu cheklovlarga qaramay server-tomon prototip ifloslanishini xavfsiz sinashga imkon beruvchi bir qancha zararsiz usullarni ko‘rib chiqamiz.

---

### Ifloslangan xususiyatlarni aks ettirish orqali server-tomon prototip ifloslanishini aniqlash

Dasturchilar uchun oson tuzuk — JavaScript `for...in` tsikli obyektning barcha enumerable (sana-satr) xususiyatlari orqali aylanishini unutib qo‘yishlari mumkin; shu jumladan meros orqali kelgan (prototype zanjiri orqali olingan) xususiyatlar ham kiradi.

> Eslatma
> Bu natijada JavaScriptning ichki konstruktorlari tomonidan o‘rnatilgan built-in xususiyatlar kiritilmaydi, chunki ular sukut bo‘yicha non-enumerable hisoblanadi.

Quyidagicha misol qilib tekshirib ko‘rishingiz mumkin:

```javascript
const myObject = { a: 1, b: 2 };

// prototipga tasodifiy xususiyat qo'shish
Object.prototype.foo = 'bar';

// myObject o'zining foo xususiyatiga ega emasligini tasdiqlash
myObject.hasOwnProperty('foo'); // false

// myObject xususiyat nomlarini ro'yxatlash
for(const propertyKey in myObject){
    console.log(propertyKey);
}

// Chiqish: a, b, foo
```

Bu xatti-harakat massivlar (arrays) ga ham taalluqli: `for...in` sikli avval indekslar (aslida raqamli xususiyatlar) bo‘yicha, so‘ngra meros orqali kelgan xususiyatlar bo‘yicha aylanish qiladi.

```javascript
const myArray = ['a','b'];
Object.prototype.foo = 'bar';

for(const arrayKey in myArray){
    console.log(arrayKey);
}

// Chiqish: 0, 1, foo
```

Har ikki holatda ham, agar ilova keyinchalik qaytgan xususiyatlarni javobga (response) qo‘shsa, bu server-tomon prototip ifloslanishini sinash uchun oddiy yo‘l bo‘lishi mumkin.

JSON ma’lumot yuboradigan POST yoki PUT so‘rovlari bunday xatti-harakat uchun ayniqsa mos keladi, chunki serverlar ko‘pincha yangilangan yoki yangi obyektning JSON ko‘rinishini qaytaradi. Bunday holatda siz global `Object.prototype`ni quyidagicha ifloslashni sinab ko‘rishingiz mumkin:

```
POST /user/update HTTP/1.1
Host: vulnerable-website.com
...
{
    "user":"wiener",
    "firstName":"Peter",
    "lastName":"Wiener",
    "__proto__":{
        "foo":"bar"
    }
}
```

Agar sayt zaif bo‘lsa, yuborgan xususiyatingiz yangilangan obyekt ichida javobda paydo bo‘ladi:

```
HTTP/1.1 200 OK
...
{
    "username":"wiener",
    "firstName":"Peter",
    "lastName":"Wiener",
    "foo":"bar"
}
```

Ba'zi kam hollarda, veb-sayt bu xususiyatlardan dinamik HTML yaratishda ham foydalanishi mumkin — natijada kiritilgan xususiyat brauzeringizda ko‘rsatilishi mumkin.

Server-tomon prototip ifloslanishi mumkinligini aniqlagach, ekspluatatsiya uchun foydalanish mumkin bo‘lgan potensial gadgetlarni izlashni boshlashingiz mumkin. Foydalanuvchi ma’lumotlarini yangilash bilan bog‘liq har qanday funksiyalarni tekshirishga arziydi, chunki ular ko‘pincha kelayotgan ma’lumotni ilovadagi foydalanuvchini ifodalovchi mavjud obyektga birlashtirishni (merge) o‘z ichiga oladi. Agar o‘z foydalanuvchingizga istalgan xususiyatlarni qo‘shsangiz, bu bir qator zaifliklarga, jumladan huquq (privilegiyalar)ni oshirishga olib kelishi mumkin.


Quyidagicha — so‘ralgan matnning o‘zbekcha tarjimasi:

---

### Ifloslangan xususiyatlar aks etmasdan server-tomon prototip ifloslanishini aniqlash

Ko‘pincha, server-tomon prototip obyektini muvaffaqiyatli ifloslaganingizda ham, o‘zgartirilgan xususiyatni javobda ko‘rmaysiz. Konsolda obyektni tekshira olmasligingiz hisobga olinsa, in'ektsiyangiz ish berganligini qanday aniqlash muammo tug‘diradi.

Yondashuvlardan biri — server konfiguratsiya opsiyalariga mos kelishi mumkin bo‘lgan xususiyatlarni in'ektsiya qilib ko‘rishdir. Keyin in'ektsiyadan oldingi va keyingi server xatti-harakatlarini solishtirib, bu konfiguratsiya o‘zgarishi amalga oshgan-yo‘qligini tekshirishingiz mumkin. Agar o‘zgarish sezilsa, bu server-tomon prototip ifloslanishini topganingizning kuchli ko‘rsatkichidir.

Ushbu bo‘limda quyidagi texnikalarni ko‘rib chiqamiz:

* Status kodini bekor qilish (Status code override)
* JSON bo‘sh joy (spaces) ni bekor qilish (JSON spaces override)
* Charset ni bekor qilish (Charset override)

Ushbu barcha in'ektsiyalar zararsiz (non-destructive) bo‘lib, lekin muvaffaqiyatli bo‘lganda server xatti-harakatida doimiy va o‘ziga xos o‘zgarish hosil qiladi. Ushbu bo‘limdagi har qanday texnikadan birini tegishli laboratoriyani yechishda ishlatishingiz mumkin.

---

### Status kodini bekor qilish

Express kabi server-tomon JavaScript ramkalarida dasturchilar maxsus HTTP javob statuslarini belgilashlari mumkin. Xatoliklar holatida JavaScript server umumiy HTTP javobini qaytarishi mumkin, ammo javob tanasida JSON formatidagi xato obyekti ham bo‘ladi. Bu xatoning nima sababdan yuz berganiga oid qo‘shimcha ma’lumot berishning bir usuli bo‘lib, oddiy HTTP statusdan aniq ko‘rinmasligi mumkin.

Garchi biroz adashtiruvchi bo‘lsa-da, ba’zan 200 OK javobi olinadi, lekin javob tanasida boshqa statusni ko‘rsatadigan xato obyekti bo‘ladi:

```
HTTP/1.1 200 OK
...
{
    "error": {
        "success": false,
        "status": 401,
        "message": "You do not have permission to access this resource."
    }
}
```

Node'ning `http-errors` moduli bunday xato javobini yaratish uchun quyidagi funksiyani o‘z ichiga oladi:

```javascript
function createError () {
    //...
    if (type === 'object' && arg instanceof Error) {
        err = arg
        status = err.status || err.statusCode || status
    } else if (type === 'number' && i === 0) {
    //...
    if (typeof status !== 'number' ||
    (!statuses.message[status] && (status < 400 || status >= 600))) {
        status = 500
    }
    //...
```

Birinchi ta'kidlangan qatorda funksiya argumenti sifatida o‘tgan obyektning `status` yoki `statusCode` xususiyatini o‘qish orqali `status` o‘zgaruvchisiga qiymat berishga harakat qilinadi. Agar sayt ishlab chiquvchilari xatoga `status` xususiyatini aniq belgilamagan bo‘lsa, siz quyidagicha prototip ifloslanishini tekshirish uchun buni ishlatishingiz mumkin:

1. Xato javobini qanday chiqarishni toping va sukutdagi (default) status kodini qayd etib oling.
2. Prototipni o‘z `status` xususiyatingiz bilan ifloslashga harakat qiling. Boshqa hech qanday sabab bilan ishlatilishi ehtimoli kam bo‘lgan noyob (obscure) status kodidan foydalanishga e’tibor bering.
3. Xato javobini yana chaqiring va status kodini muvaffaqiyatli o‘zgartira olganingizni tekshiring.

**Eslatma**
`status` kodini 400–599 oralig‘ida tanlashingiz kerak. Aks holda, yuqorida ikkinchi ta'kidlangan qatorda ko‘rsatilganidek, Node sukut bo‘yicha `status`ni 500 ga sozlaydi, shuning uchun prototipni ifloslaganingizni aniqlay olmaysiz.

---

### JSON `spaces` ni bekor qilish

Express ramkasi `json spaces` opsiyasini taqdim etadi — bu javobdagi har qanday JSON ma’lumotni nechta bo‘shliq bilan indentatsiya qilishni sozlash imkonini beradi. Ko‘p hollarda dasturchilar ushbu xususiyatni aniqlamagan holda sukut bo‘yicha qiymat bilan mamnun bo‘ladilar, shuning uchun u prototip zanjiri orqali ifloslanishga moyil bo‘ladi.

Agar sizda har qanday JSON javobiga kirish bo‘lsa, prototipni o‘z `json spaces` xususiyatingiz bilan ifloslashni sinab ko‘ring, so‘ng tegishli so‘rovni qayta yuboring va JSON indentatsiyasi shu qadar oshganligini tekshiring. Xuddi shunday qadamlarni indentatsiyani olib tashlash uchun ham bajarib, zaiflikni tasdiqlashingiz mumkin.

Bu ayniqsa foydali texnika — chunki u ma’lum bir xususiyatning javobda aks etishiga bog‘liq emas. Shuningdek juda xavfsiz, chunki siz aslida ifloslanishni sukutdagi qiymatga qaytarib o‘chirib yoqishingiz mumkin.

Eslatib o‘tish joizki, Expressdagi prototip ifloslanishi 4.17.4 versiyada tuzatilgan, ammo yangilamagan saytlarda hanuz zaiflik bo‘lishi mumkin.

**Eslatma**
Agar siz bu texnikani Burp’da sinayotgan bo‘lsangiz, xabar muharriridagi *Raw* (xom) tabga o‘ting. Aks holda, standart go‘zal (prettified) ko‘rinish indentatsiya o‘zgarishini normallashtirib ko‘rsatadi va siz farqni ko‘rolmaysiz.

---

### Charset (belgilangan kodlash) ni bekor qilish

Express serverlari ko‘pincha so‘rovlarni tegishli handler funksiyasiga o‘tishdan oldin oldindan qayta ishlash imkonini beruvchi “middleware” modullarini ishlatadi. Masalan, `body-parser` moduli kiruvchi so‘rov tanasini (`req.body`) tahlil qilish uchun keng qo‘llaniladi. Bu erda yana bir gadget mavjud bo‘lib, u server-tomon prototip ifloslanishini tekshirish uchun ishlatilishi mumkin.

Quyidagi kod `read()` funksiyasiga opsiyalar obyektini uzatayotganiga e’tibor bering — bu funksiya so‘rov tanasini o‘qib, uni tahlil qilish uchun ishlatiladi. Ushbu opsiyalardan biri — `encoding`, qaysi belgilash kodlashdan foydalanganini belgilaydi. Bu qiymat `getCharset(req)` funksiyasi orqali so‘rovdan olinadi yoki sukut bo‘yicha UTF-8 ga o‘rnatiladi.

```javascript
var charset = getCharset(req) or 'utf-8'

function getCharset (req) {
    try {
        return (contentType.parse(req).parameters.charset || '').toLowerCase()
    } catch (e) {
        return undefined
    }
}

read(req, res, next, parse, debug, {
    encoding: charset,
    inflate: inflate,
    limit: limit,
    verify: verify
})
```

Agar `getCharset()` funksiyasiga diqqat qilsangiz, ishlab chiquvchilar `Content-Type` headerida aniq `charset` atributi bo‘lmasligi mumkinligini hisobga olgan va bunday holatlarda bo‘sh satrga (`''`) qaytish mexanizmini qo‘ygan. Muhimi — bu qiymat prototip ifloslanishi orqali boshqarilishi mumkin bo‘ladi.

Agar javobda aks etadigan xususiyatlari bo‘lgan obyektni topsangiz, bu orqali manbalarni (sources) tekshirishingiz mumkin. Quyidagi misolda biz UTF-7 kodlashidan va JSON manbasidan foydalanamiz.

Avvalo, javobda aks etadigan xususiyatga UTF-7 bilan kodlangan ixtiyoriy satr qo‘shing. Masalan, `foo` UTF-7 da `+AGYAbwBv-` ga to‘g‘ri keladi.

```json
{
    "sessionId":"0123456789",
    "username":"wiener",
    "role":"+AGYAbwBv-"
}
```

So‘rovni yuboring. Serverlar sukut bo‘yicha UTF-7 dan foydalanishmaydi, shuning uchun bu satr javobda kodlangan holatda paydo bo‘ladi.
Endi prototipni `content-type` xususiyati bilan ifloslashga harakat qiling — u aniq UTF-7 kodlashni belgilasin:

```json
{
    "sessionId":"0123456789",
    "username":"wiener",
    "role":"default",
    "__proto__":{
        "content-type": "application/json; charset=utf-7"
    }
}
```

Birinchi so‘rovni takrorlang. Agar siz prototipni muvaffaqiyatli ifloslagan bo‘lsangiz, UTF-7 bilan kodlangan satr hozir javobda dekodlangan holda ko‘rinadi:

```json
{
    "sessionId":"0123456789",
    "username":"wiener",
    "role":"foo"
}
```

Node'ning `_http_incoming` modulidagi bir xatolik tufayli bu usul haqiqiy so‘rovning `Content-Type` headerida o‘zining `charset` atributi mavjud bo‘lsa ham ishlaydi. So‘rovda takroriy (duplikat) headerlar mavjud bo‘lganda, `_addHeaderLine()` funksiyasi IncomingMessage obyektiga xususiyatlarni o‘tkazishdan oldin shu kalit bilan hech qanday xususiyat mavjud emasligini tekshiradi — agar mavjud bo‘lsa, qayta ishlanayotgan header tashlab yuboriladi:

```javascript
IncomingMessage.prototype._addHeaderLine = _addHeaderLine;
function _addHeaderLine(field, value, dest) {
    // ...
    } else if (dest[field] === undefined) {
        // Drop duplicates
        dest[field] = value;
    }
}
```

Agar shunday bo‘lsa, qayta ishlanayotgan header amalda tashlab yuboriladi. Bu qanday amalga oshirilishiga qarab, ushbu tekshiruv (ehtimol tasodifan) prototip zanjiri orqali meros bo‘lib kelgan xususiyatlarni ham o‘z ichiga oladi. Demak, agar biz prototipni o‘zimizning `content-type` xususiyatimiz bilan ifloslasak, so‘rovdagi haqiqiy `Content-Type` headerini ifodalovchi xususiyat shu nuqtada yo‘q qilinadi va u bilan birga headerdan olingan asl qiymat ham yo‘q bo‘ladi.


Server-tomonidagi prototype pollution manbalarini skanerlash
Qo'lda manbalarni sinovdan o'tkazish zaiflikni tushunishga yordam berar ekan, amalda bu takrorlanuvchi va vaqt talab qiluvchi bo'lishi mumkin. Shu sababli, biz Burp Suite uchun Server-Side Prototype Pollution Scanner kengaytmasini yaratdik — u bu jarayonni avtomatlashtirish imkonini beradi. Asosiy ish jarayoni quyidagicha:

1. BApp Store’dan Server-Side Prototype Pollution Scanner kengaytmasini o‘rnating va u yoqilganligiga ishonch hosil qiling. Qanday o‘rnatish haqida batafsil ma’lumot uchun “Installing extensions from the BApp Store” bo‘limiga qarang.
2. Burp’ning brauzeridan foydalanib, maqsadli veb-saytni o‘rganing — iloji boricha ko‘proq kontentni xaritalang va proxy tarixida trafikni to‘plang.
3. Burp’da Proxy > HTTP history tabiga o‘ting.
4. Ro‘yxatni faqat doirada (in-scope) elementlarni ko‘rsatish uchun filtrlash.
5. Ro‘yxatdagi barcha elementlarni tanlang.
6. Tanlov ustida sichqonchaning o‘ng tugmasini bosib, Extensions > Server-Side Prototype Pollution Scanner > Server-Side Prototype Pollution menyusiga o‘ting, so‘ng scanning texnikasidan birini tanlang.
7. So‘ralganda, zarur bo‘lsa hujum (attack) konfiguratsiyasini o‘zgartiring, so‘ng Scan boshlash uchun OK tugmasini bosing.

Burp Suite Professional’da kengaytma topilgan prototype pollution manbalarini Dashboard va Target tablaridagi Issue activity panelida xabar qiladi. Agar siz Burp Suite Community Edition’dan foydalansangiz, Extensions > Installed tabiga o‘tib, kengaytmanni tanlang va uning Output tabini kuzatib boring — topilgan muammolar shu yerda ko‘rsatiladi.

Eslatma
Qaysi scan texnikasini tanlashni bilmasangiz, mavjud barcha usullar bilan scan o‘tkazadigan Full scan’ni tanlashingiz mumkin. Biroq, bu ancha ko‘p so‘rov yuborishni talab qiladi.

Server-tomonidagi prototype pollution uchun kirish (input) filtrini chetlab o‘tish
Veb-saytlar ko‘pincha **proto** kabi shubhali kalit so‘zlarni filtrlash orqali prototype pollution’ni oldini olishga harakat qilishadi. Ammo bunday kalitlarni sanitizatsiya qilish uzoq muddatli mustahkam yechim emas — chunki uni bir qancha usullar bilan chetlab o‘tish mumkin. Masalan, hujumchi:

* Ta’qiqlangan kalitlarni obfuskatsiya qilib, sanitizatsiya qilinib qolishini oldini olishi mumkin. Batafsil ma’lumot uchun “Bypassing flawed key sanitization” bo‘limiga qarang.
* **proto** o‘rniga constructor xususiyati orqali prototype’ga murojaat qilishi mumkin. Batafsil ma’lumot uchun “Prototype pollution via the constructor” bo‘limiga qarang.

Shuningdek, Node ilovalari buyruq qatori flag’lari yordamida **proto** ni o‘chirishi yoki yoniq bo‘lishini oldini olishi mumkin: --disable-proto=delete yoki --disable-proto=throw. Biroq, bu ham constructor texnikasi orqali chetlab o‘tilishi mumkin.


