
### Brauzer API’lari orqali prototip ifloslanishi

Hayron qolasizki, brauzerlar tomonidan taqdim etiladigan keng tarqalgan JavaScript API’larida bir qator umumiy *prototype pollution* (prototip ifloslanishi) gadjetlari mavjud. Ushbu bo‘limda ularni DOM XSS uchun qanday ekspluatatsiya qilish mumkinligini ko‘rsatamiz — bu, ayniqsa, ishlab chiquvchilar tomonidan amalga oshirilgan zaif prototip ifloslanishi himoyalarini aylanib o‘tishda foydali bo‘lishi mumkin.

#### `fetch()` orqali prototip ifloslanishi

Fetch API JavaScript’da HTTP so‘rovlarini yuborishning oddiy usulini taqdim etadi. `fetch()` metodi ikki argument qabul qiladi:

1. So‘rov yuboriladigan URL.
2. So‘rovning method, headers, body va shunga o‘xshash qismlarini nazorat qiluvchi `options` obyekti.

Quyida `fetch()` bilan POST so‘rov yuborish misoli keltirilgan:

```js
fetch('https://normal-website.com/my-account/change-email', {
    method: 'POST',
    body: 'user=carlos&email=carlos%40ginandjuice.shop'
})
```

Ko‘rib turganingizdek, biz `method` va `body` xususiyatlarini aniq belgiladik, lekin boshqa bir qancha mumkin bo‘lgan xususiyatlarni belgilamay qoldirdik. Agar hujumchi mos keladigan manbani topsa, u `Object.prototype` ga o‘zining `headers` xususiyatini ifloslantirishi (pollute) mumkin. Bu keyin `fetch()` ga uzatilgan `options` obyekti orqali meros qilib olinib, so‘rovni yaratishda ishlatilishi ehtimoli bor.

Bu bir qancha muammolarga olib kelishi mumkin. Masalan, quyidagi kod prototip ifloslanishi orqali DOM XSS ga moyil bo‘lishi mumkin:

```js
fetch('/my-products.json',{method:"GET"})
    .then((response) => response.json())
    .then((data) => {
        let username = data['x-username'];
        let message = document.querySelector('.message');
        if(username) {
            message.innerHTML = `My products. Logged in as <b>${username}</b>`;
        }
        let productList = document.querySelector('ul.products');
        for(let product of data) {
            let product = document.createElement('li');
            product.append(product.name);
            productList.append(product);
        }
    })
    .catch(console.error);
```

Buni ekspluatatsiya qilish uchun hujumchi `Object.prototype` ni quyidagicha `headers` xususiyati bilan ifloslantirishi mumkin:

```
?__proto__[headers][x-username]=<img/src/onerror=alert(1)>
```

Faraz qilaylikki, server tomonida ushbu header qaytarilgan JSON faylda `x-username` qiymatini o‘rnatishda ishlatiladi. Yuqoridagi zaif mijozdagi (client-side) kodda bu `username` o‘zgaruvchisiga tayinlanadi va keyin `innerHTML` sinkiga uzatiladi — natijada DOM XSS yuz beradi.

**Eslatma:** Ushbu texnikani `fetch()` ga uzatilgan `options` obyekti uchun aniqlanmagan istalgan xususiyatni nazorat qilish uchun ishlatishingiz mumkin. Masalan, so‘rovga zararli `body` qo‘shish imkoniyati paydo bo‘lishi mumkin.

#### `Object.defineProperty()` orqali prototip ifloslanishi

Prototip ifloslanishini biroz biladigan ishlab chiquvchilar potentsial gadjetlarni bloklash uchun `Object.defineProperty()` metodidan foydalanishga harakat qilishlari mumkin. Bu orqali ta’sirlangan obyektda `configurable: false` va `writable: false` qilib, xususiyatni to‘g‘ridan-to‘g‘ri o‘rnatish mumkin:

```js
Object.defineProperty(vulnerableObject, 'gadgetProperty', {
    configurable: false,
    writable: false
})
```

Bu dastlab prototip orqali zararlangan versiyaning meros qilib olinishining oldini olganidek tuyulishi mumkin. Ammo bu yondashuv ildizdan xato.

`fetch()` misolida bo‘lgani kabi, `Object.defineProperty()` ham — «descriptor» deb ataladigan — options obyektini qabul qiladi. Yuqoridagi misolda ham shuni ko‘rish mumkin. Ishlab chiquvchilar faqat bu xususiyatni prototip ifloslanishidan himoya qilish maqsadida belgilashsa va hech qanday boshlang‘ich (`value`) qiymatini bermasa, hujumchi `Object.prototype` ga zararli `value` xususiyatini ifloslantirib, descriptor orqali meros qilib olinishi va oxir-oqibat `gadgetProperty` ga tayinlanishiga erishishi mumkin.
