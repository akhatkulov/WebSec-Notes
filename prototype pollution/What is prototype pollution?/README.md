### Prototype Pollution nima?

**Prototype pollution** — bu JavaScript’dagi zaiflik bo‘lib, xakerlarga global obyektlarning prototiplariga ixtiyoriy xususiyatlar qo‘shishga imkon beradi. Keyinchalik bu xususiyatlar foydalanuvchi yaratgan obyektlar tomonidan meros qilib olinishi mumkin.

Masalan, konfiguratsiya obyektini prototype pollution orqali “ifloslash” mumkin. Bu zaiflik o‘zi mustaqil ravishda ko‘p hollarda ekspluatatsiya qilinmaydi, ammo u orqali dastur obyektlarida boshqarib bo‘lmaydigan xususiyatlarga ta’sir o‘tkazish mumkin bo‘ladi. Agar dastur keyinchalik bu xususiyatlarni noto‘g‘ri ishlatsa, boshqa zaifliklar bilan birlashtirib ekspluatatsiya qilish mumkin bo‘ladi.

* **Client-side (brauzer ichida)** JavaScript’da bu ko‘pincha **DOM XSS** ga olib keladi.
* **Server-side** prototype pollution esa hatto **masofadan kod bajarish (RCE)** ga sabab bo‘lishi mumkin.

---

### JavaScript’da obyekt nima?

JavaScript’dagi **obyekt** bu — **kalit\:qiymat (key\:value)** juftliklar to‘plami. Masalan, foydalanuvchini ifodalovchi obyekt:

```javascript
const user = {
    username: "wiener",
    userId: 01234,
    isAdmin: false
}
```

Xususiyatlarga murojaat qilish:

```javascript
user.username     // "wiener"
user['userId']    // 01234
```

Obyekt xususiyatlari faqat ma’lumot bo‘lmasdan, **funksiya (metod)** ham bo‘lishi mumkin:

```javascript
const user = {
    username: "wiener",
    userId: 01234,
    exampleMethod: function(){
        // nimadir bajaradi
    }
}
```

Bunday obyektni **object literal** deyiladi (ya’ni to‘g‘ridan-to‘g‘ri `{}` orqali yaratilgan obyekt). Aslida esa, JavaScript’da deyarli hamma narsa obyekt sifatida ko‘riladi. Shu sababli bu materiallarda “obyekt” atamasi nafaqat object literal, balki barcha JavaScript entitilarini anglatadi.

---

### JavaScript’da prototip nima?

JavaScript’dagi har bir obyekt boshqa bir obyekt bilan bog‘langan bo‘ladi. Bu obyekt **prototip** deyiladi.

* Masalan, stringlar avtomatik ravishda `String.prototype` ga ulanadi.

```javascript
let myObject = {};
Object.getPrototypeOf(myObject);    // Object.prototype

let myString = "";
Object.getPrototypeOf(myString);    // String.prototype

let myArray = [];
Object.getPrototypeOf(myArray);     // Array.prototype

let myNumber = 1;
Object.getPrototypeOf(myNumber);    // Number.prototype
```

Obyekt o‘zida yo‘q bo‘lgan xususiyatlarni prototipidan oladi. Shu orqali yangi obyektlar mavjud metodlardan foydalanishi mumkin bo‘ladi.

Masalan:

* `String.prototype` da `toLowerCase()` metodi bor.
* Shuning uchun barcha stringlar `toLowerCase()` dan foydalana oladi.

---

### JavaScript’da obyekt merosxo‘rligi qanday ishlaydi?

Agar siz obyektning xususiyatiga murojaat qilsangiz, JS avvalo uni obyektning o‘zida qidiradi. Agar topmasa, uning **prototipida** qidiradi.

```javascript
let myObject = {};
```

Konsolda `myObject.` deb yozsangiz, hech qanday xususiyat aniqlanmagan bo‘lsa ham, sizga `Object.prototype` dan meros olingan metodlar ko‘rinadi.

---

### Prototiplar zanjiri (Prototype chain)

Prototipning o‘zi ham obyekt bo‘lgani uchun, u ham boshqa prototipga ega bo‘ladi. Bu jarayon **Object.prototype** ga borib tugaydi, uning prototipi esa `null`.

Shunday qilib, obyekt faqat o‘z prototipidan emas, balki **butun prototip zanjiridan** meros oladi.

---

### `__proto__` orqali prototipga murojaat qilish

Har bir obyekt maxsus `__proto__` xususiyatiga ega bo‘lib, u orqali obyektning prototipini o‘qish yoki o‘zgartirish mumkin.

```javascript
username.__proto__                   // String.prototype
username.__proto__.__proto__         // Object.prototype
username.__proto__.__proto__.__proto__ // null
```

---

### Prototiplarni o‘zgartirish

JavaScript’da hatto **built-in** prototiplarni ham o‘zgartirish mumkin. Bu odatda yomon amaliyot hisoblanadi, ammo ba’zi hollarda ishlatiladi.

Masalan, `trim()` paydo bo‘lishidan oldin, developerlar `String.prototype` ga o‘zlari metod qo‘shishardi:

```javascript
String.prototype.removeWhitespace = function(){
    // boshidagi va oxiridagi bo‘sh joylarni olib tashlash
}
```

Natijada barcha stringlar undan foydalana olar edi:

```javascript
let searchTerm = "  example ";
searchTerm.removeWhitespace();   // "example"
```


### Prototype pollution zaifligi qanday yuzaga keladi?

**Prototype pollution** zaifliklari odatda shu holatda paydo bo‘ladi: JavaScript funksiyasi foydalanuvchi boshqaruvida bo‘lgan xususiyatlarni o‘z ichiga olgan obyektni rekursiv tarzda mavjud obyektga birlashtiradi (merge qiladi), lekin avval kalitlarni (keys) tozalamaydi (sanitize). Bu xakerga `__proto__` kabi maxsus kalitni va unga tegishli ixtiyoriy ichki (nested) xususiyatlarni yuborish imkonini beradi.

`__proto__` JavaScript kontekstida maxsus ma’no kasb etgani sababli, merge operatsiyasi qiymatlarni maqsadli (target) obyektga emas, balki uning prototipiga tayinlashi mumkin. Natijada hujumchi prototipni zararli qiymatlar bilan “ifloslashi” va keyinchalik ilova tomonidan xavfli tarzda ishlatilishi mumkin bo‘lgan xususiyatlarni kiritishi mumkin.

Har qanday prototip ifloslanishi mumkin bo‘lsa-da, bu odatda global `Object.prototype` bilan sodir bo‘ladi.

Muvaffaqiyatli ekspluatatsiya uchun kerakli asosiy komponentlar:

* **Prototype pollution source (manba)** — bu prototip obyektlarini ixtiyoriy xususiyatlar bilan ifloslash imkonini beruvchi har qanday foydalanuvchi-kiritilgan input.
* **Sink** — ya’ni arbitrary code execution (ixtiyoriy kod bajarilishiga) olib keladigan JavaScript funksiyasi yoki DOM elementi.
* **Exploitable gadget** — bu sinkga filtrlanmagan yoki sanitatsiyalanmagan tarzda uzatiladigan va ekspluatatsiya qilish mumkin bo‘lgan xususiyat.

---

### Prototype pollution manbalari

Prototype pollution manbai — bu foydalanuvchi tomonidan boshqariladigan, prototip obyektlariga ixtiyoriy xususiyatlar qo‘shishga imkon beruvchi har qanday input. Eng keng tarqalgan manbalar:

* URL (query yoki fragment/hash qismi orqali)
* JSON asosidagi input
* Web messages (postMessage va h.k.)

---

### URL orqali prototype pollution

Quyidagi URLni ko‘rib chiqing — u hujumchi tomonidan qurilgan query stringni o‘z ichiga oladi:

```
https://vulnerable-website.com/?__proto__[evilProperty]=payload
```

Agar query stringni kalit\:qiymat juftliklariga ajratsangiz, URL parser `__proto__` ni oddiy satr (string) deb talqin qilishi mumkin. Ammo keyinchalik bu kalitlar va qiymatlar mavjud obyektga merge qilinganda nima sodir bo‘lishiga e’tibor bering.

Siz `__proto__` va uning ichidagi `evilProperty` ni quyidagi kabi maqsadli obyektga oddiygina qo‘shildi, deb o‘ylashingiz mumkin:

```javascript
{
    existingProperty1: 'foo',
    existingProperty2: 'bar',
    __proto__: {
        evilProperty: 'payload'
    }
}
```

Ammo haqiqiy holatda bunday bo‘lmaydi. Rekursiv merge operatsiyasi bir nuqtada `evilProperty` qiymatini quyidagi kabi tayinlashi mumkin:

```javascript
targetObject.__proto__.evilProperty = 'payload';
```

Bu tayinlash jarayonida JavaScript dvigateli `__proto__` ni prototipga qaytaruvchi getter sifatida ko‘radi. Natijada `evilProperty` qiymati maqsadli obyektga emas, uning prototipiga tayinlanadi. Agar maqsadli obyekt default `Object.prototype` dan foydalansa, endi JavaScript runtime’dagi barcha obyektlar (o‘zlarida shu nomdagi xususiyat bo‘lmasa) `evilProperty` ni meros qilib olishadi.

Amaliyotda `evilProperty` nomli xususiyatni qo‘shish ko‘pincha hech qanday ta’sir qilmaydi. Biroq hujumchi shu usul bilan ilova yoki import qilingan kutubxonalar tomonidan ishlatiladigan xususiyatlarni prototipga kiritishi mumkin.

---

### JSON input orqali prototype pollution

Foydalanuvchi boshqaruvidagi obyektlar ko‘pincha `JSON.parse()` bilan JSON satridan olingan obyektlardan olinadi. Qiziq tomoni shuki, `JSON.parse()` ham JSON obyektdagi har qanday kalitni oddiy satr sifatida qabul qiladi, shu jumladan `__proto__` ni ham. Bu yana bir potentsial vektor hisoblanadi.

Masalan, hujumchi quyidagi zararli JSONni yuborsa (masalan, web message orqali):

```json
{
    "__proto__": {
        "evilProperty": "payload"
    }
}
```

Agar bu `JSON.parse()` orqali JavaScript obyektiga aylanadigan bo‘lsa, hosil bo‘lgan obyekt haqiqatan ham `__proto__` kalitiga ega bo‘ladi:

```javascript
const objectLiteral = {__proto__: {evilProperty: 'payload'}};
const objectFromJson = JSON.parse('{"__proto__": {"evilProperty": "payload"}}');

objectLiteral.hasOwnProperty('__proto__');     // false
objectFromJson.hasOwnProperty('__proto__');    // true
```

Agar `JSON.parse()` yordamida yaratilgan obyekt keyinchalik avvalgi misoldagi kabi sanitatsiya qilinmagan holda mavjud obyektga merge qilinsa, bu ham prototype pollution ga olib keladi, URL misolida ko‘rib chiqilganidek.

