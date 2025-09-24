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

