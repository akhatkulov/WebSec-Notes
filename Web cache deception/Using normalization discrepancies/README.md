

# Normalizatsiyadagi nomuvofiqliklar

Normalizatsiya URL yo‘llarining turli ifodalarini standart formatga aylantirishni o‘z ichiga oladi. Bu baʼzan kodlangan belgilarni dekodlash va nuqta-segmentlarni (dot-segments) yechishni ham o‘z ichiga oladi, lekin bunday xatti-harakat parserdan parserga sezilarli darajada farq qilishi mumkin.

Kesh serveri va origin server URLni qanday normalizatsiya qilishidagi nomuvofiqliklar xakerga har bir parser tomonidan turlicha talqin qilinadigan path traversal (yo‘lni travers qilish) paylo‘dni tuzishga imkon berishi mumkin. Misol uchun `/static/..%2fprofile` ni ko‘rib chiqing:

* Slash belgilarini dekodlab, nuqta-segmentlarni hal qiluvchi origin server yo‘lni `/profile` ga normalizatsiya qiladi va profil maʼlumotini qaytaradi.
* Nuqta-segmentlarni yechmaydigan yoki slashlarni dekodlamaydigan kesh esa yo‘lni `/static/..%2fprofile` deb talqin qiladi. Agar kesh `/static` prefiksi bo‘yicha javoblarni saqlasa, u holda profil maʼlumotini keshlab (cache) saqlashi va xizmat ko‘rsatishi mumkin.

Yuqoridagi misolda ko‘rsatilgandek, yo‘lni travers qilish ketma-ketligidagi har bir nuqta-segment kodlangan bo‘lishi kerak. Aks holda, jabrlanuvchi brauzeri so‘rovni keshga yuborishdan oldin uni yechib yuboradi. Shuning uchun, ekspluatatsiya qilinadigan normalizatsiya nomuvofiqligi mavjud bo‘lishi uchun kesh yoki origin server yo‘lni travers qilish ketma-ketligidagi belgilarni dekodlashi hamda nuqta-segmentlarni yechishi kerak.

## Origin serverning normalizatsiyasini aniqlash

Origin server URL yo‘lini qanday normalizatsiya qilishini sinash uchun, path traversal ketma-ketligi bo‘lgan va keshlanmaydigan resursga so‘rov yuboring — boshlang‘ich katalog sifatida tasodifiy direktoriyani qo‘shing. Keshlanmaydigan resursni tanlash uchun POST kabi non-idempotent metodlarni qidiring. Masalan, `/profile` ni `/aaa/..%2fprofile` ga o‘zgartiring:

* Agar javob asosiy (base) javobga mos kelsa va profil maʼlumotini qaytarsa, bu yo‘l `/profile` sifatida talqin qilingani va origin server slashni dekodlab, nuqta-segmentni yechgani anglatadi.
* Agar javob mos kelmasa, masalan 404 xatolik qaytarsa, bu yo‘l `/aaa/..%2fprofile` sifatida talqin qilinganini ko‘rsatadi. Bu origin server slashni dekodlamagan yoki nuqta-segmentni yechmaganini bildiradi.

**Eslatma**
Normalizatsiyani sinashni boshlaganda, avval dot-segment ichidagi faqat ikkinchi slashni kodlashdan boshlang. Bu muhim, chunki baʼzi CDNlar static katalog prefiksi keyingi slashni moslashtiradi.

Shuningdek to‘liq path traversal ketma-ketligini kodlashni yoki slash o‘rniga nuqtani kodlashni ham sinab ko‘rishingiz mumkin. Bu baʼzan parserning ketma-ketlikni dekodlashiga taʼsir qilishi mumkin.

## Kesh serverning normalizatsiyasini aniqlash

Keshning yo‘lni qanday normalizatsiya qilishini sinash uchun bir nechta metodlardan foydalanishingiz mumkin. Avvalo potentsial static kataloglarni aniqlang. Proxy > HTTP history bo‘limida keng tarqalgan static katalog prefikslari va keshlangan javoblar bilan bo‘lgan so‘rovlarni qidiring. 2xx javoblari va script, image, CSS MIME turlari bilan filtrlash orqali static resurslarga eʼtibor qarating.

Keyin, keshlangan javobga ega bo‘lgan so‘rovni tanlab, static yo‘l boshida tasodifiy direktoriyani qo‘shib va path traversal ketma-ketligi bilan qayta yuboring. Masalan: `/aaa/..%2fassets/js/stockCheck.js`:

* Agar javob endi keshlanmagan bo‘lsa, bu kesh yo‘lni normalizatsiya qilmasligini va endpointga xaritalashdan avval normalizatsiya amalga oshirilmasligini ko‘rsatadi. Bu `/assets` prefiksi asosida kesh qoidasi mavjudligini bildiradi.
* Agar javob hali ham keshlangan bo‘lsa, bu kesh yo‘lni `/assets/js/stockCheck.js` ga normalizatsiya qilganligini ko‘rsatishi mumkin.

Shuningdek, path traversal ketma-ketligini katalog prefiksidan keyin qo‘yishingiz mumkin. Masalan, `/assets/js/stockCheck.js` ni `/assets/..%2fjs/stockCheck.js` ga o‘zgartiring:

* Agar javob endi keshlanmasa, bu kesh nuqtalar ketma-ketligini yechib, slashni dekodlab, yo‘lni `/js/stockCheck.js` deb talqin qilayotganini ko‘rsatadi — yaʼni kesh `/assets` prefiksi bo‘yicha qoidaga ega.
* Agar javob hali ham keshlangan bo‘lsa, bu kesh slashni dekodlamagan yoki nuqta-segmentni yechmaganini bildiradi va yo‘lni `/assets/..%2fjs/stockCheck.js` deb talqin qiladi.

Eslatib o‘tish joizki, har ikkala holatda ham javob boshqa kesh qoidasi (masalan, fayl kengaytmasi asosidagi qoida) tufayli keshlangan bo‘lishi mumkin. Kesh qoidasining static katalogga asoslanganligini tasdiqlash uchun katalog prefiksidan keyingi yo‘lni tasodifiy satrga almashtiring. Masalan, `/assets/aaa`. Agar javob hali ham keshlangan bo‘lsa, bu kesh qoidasi `/assets` prefiksi asosida ekanligini tasdiqlaydi. Shuni ham yodda tutingki, agar javob keshlanmagan bo‘lib ko‘rinsa, bu static katalog qoidasi yo‘qligini qatʼiy inkor etmaydi — baʼzan 404 javoblari keshlanmaydi.

**Eslatma**
Kesh nuqta-segmentlarni dekodlash yoki URL yo‘lini dekodlashni aniq aniqlash sizga ekspluatatsiya sinovini amalga oshirmasdan imkoni bo‘lmasligi mumkin.

## Origin server normalizatsiyasidan foydalanish

Agar origin server kodlangan nuqta-segmentlarni yechsa, lekin kesh buni qilmasa, nomuvofiqlikdan foydalanish uchun quyidagi tuzilishga mos paylo‘d yaratib ko‘ring:

`/<static-directory-prefix>/..%2f<dynamic-path>`

Masalan, `/assets/..%2fprofile` paylo‘di:

* Kesh bu yo‘lni `/assets/..%2fprofile` deb talqin qiladi.
* Origin server bu yo‘lni `/profile` deb talqin qiladi.
* Origin server dinamik profil maʼlumotini qaytaradi va bu javob keshga saqlanishi mumkin.



# Kesh serverining normalizatsiyasidan foydalanish

Agar kesh server kodlangan nuqta-segmentlarni yechib tashlasa, lekin origin server buni qilmasa, nomuvofiqlikdan foydalanish uchun quyidagi tuzilishga mos paylo‘d (payload) yaratishingiz mumkin:

`/<dynamic-path>%2f%2e%2e%2f<static-directory-prefix>`

**Eslatma**
Kesh serverining normalizatsiyasidan ekspluatatsiya qilishda yo‘lni travers qilish ketma-ketligidagi barcha belgilarni kodlash kerak. Kodlangan belgilarni ishlatish delimitrlarda kutilmagan xatti-harakatlarning oldini olishga yordam beradi, va kesh dekodlashni amalga oshiradiganligi sababli static katalog prefiksidan keyin ochiq (`unencoded`) slash bo‘lishi shart emas.

Bu holatda faqat path traversal (yo‘lni travers qilish) yetarli bo‘lmaydi. Masalan, `/profile%2f%2e%2e%2fstatic` paylo‘di qanday talqin qilinishiga eʼtibor bering:

* Kesh bu yo‘lni talqin qiladi: `/static`
* Origin server bu yo‘lni talqin qiladi: `/profile%2f%2e%2e%2fstatic`

Origin server ehtimol profil maʼlumotini qaytarmasdan, xatolik (error) javobini beradi.

Nomuvofiqlikdan foydalanish uchun siz, shuningdek, origin server tomonidan ishlatiladigan, ammo kesh tomonidan ishlatilmaydigan bir ajratgichni (delimiter) aniqlashingiz kerak bo‘ladi. Mumkin bo‘lgan delimiterlarni sinash uchun ularni dynamic path (dinamik yo‘l)dan keyin paylo‘dga qo‘shing:

* Agar origin server delimiterni ishlatsa, u URL yo‘lini truncatsiya (kesadi) qiladi va dinamik maʼlumotni qaytaradi.
* Agar kesh delimiterni ishlatmasa, u yo‘lni yechiradi va javobni keshga saqlaydi.

Masalan, `/profile;%2f%2e%2e%2fstatic` paylo‘dini ko‘rib chiqing — origin server `;` ni delimiter sifatida ishlatsa:

* Kesh bu yo‘lni talqin qiladi: `/static`
* Origin server bu yo‘lni talqin qiladi: `/profile`

Origin server dinamik profil maʼlumotini qaytaradi va bu javob keshga saqlanishi mumkin. Shu sababli ushbu paylo‘d ekspluatatsiya uchun ishlatilishi mumkin.
