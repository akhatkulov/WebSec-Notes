# Ajratgich (delimiter) tafovutlari — oʻzbekcha tarjima

Ajratgichlar URL ichidagi turli elementlar orasidagi chegaralarni belgilaydi. Belgilar va satrlar ajratgich sifatida ishlatilishi odatda standartlashtirilgan: masalan, `?` odatda URL yoʻli bilan query stringni ajratadi. Biroq, URI RFC juda ruxsat beruvchi (permissive) boʻlgani uchun turli ramkalar va texnologiyalar orasida farqlar uchrab turadi.

Kesh (cache) va origin server ajratgichlarni qanday ishlatishi bo‘yicha tafovutlar web cache deception zaifliklariga olib kelishi mumkin. Misol uchun `/profile;foo.css` ni koʻrib chiqing:

* Java Spring ramkasi `;` belgisi yordamida **matrix variables** deb ataluvchi parametrlarni qoʻshadi. Java Spring ishlaydigan origin server `;` ni ajratgich sifatida talqin qiladi — yo‘lni `/profile` da kesadi va profil maʼlumotlarini qaytaradi.
* Ko‘pgina boshqa ramkalar `;` ni ajratgich sifatida ishlatmaydi. Shunday ekan, Java Spring ishlamaydigan kesh `;` va undan keyingi hamma narsani yo‘lning bir qismi deb hisoblashi mumkin. Agar kesh `.css` bilan tugaydigan yo‘llar uchun javoblarni saqlash qoidalariga ega boʻlsa, u profil maʼlumotlarini CSS fayli sifatida keshlab, keyinchalik shu URL orqali xizmat qilishi mumkin.

Xuddi shu muammo boshqa belgilar bilan ham yuz beradi — ramkalar yoki texnologiyalar orasida bir xil belgining turlicha ishlatilishi mumkin. Ruby on Rails misolidagi so‘rovlarni koʻrib chiqing — Rails `.` ni javob formatini belgilovchi ajratgich sifatida ishlatadi:

* `/profile` — bu so‘rov standart HTML format bo‘yicha qayta ishlanadi va foydalanuvchi profil maʼlumotlari qaytadi.
* `/profile.css` — bu so‘rov CSS kengaytmasi sifatida tan olinadi. Rails-da CSS formatlovchi yo‘qligi sababli so‘rov qabul qilinmaydi va xato qaytadi.
* `/profile.ico` — `.ico` kengaytmasi Rails tomonidan tan olinmaydi; shuning uchun standart HTML formatter so‘rovni bajaradi va profil maʼlumotlarini qaytaradi. Agar kesh `.ico` bilan tugaydigan so‘rovlarga javoblarni saqlasa, u profile maʼlumotlarini statik fayl sifatida keshlab xizmat qilishi mumkin.

Kodlangan (encoded) belgilar ham baʼzan ajratgich sifatida ishlatilishi mumkin. Masalan: `/profile%00foo.js`

* OpenLiteSpeed serveri kodlangan null `%00` belgısını ajratgich sifatida ishlatadi. OpenLiteSpeed ishlaydigan origin server yo‘lni `/profile` deb talqin qiladi.
* Ko‘pgina boshqa ramkalar `%00` ni URL ichida koʻrsa xato bilan javob beradi. Ammo agar kesh Akamai yoki Fastly kabi tizimdan foydalansa, u `%00` va undan keyingi hammani yo‘lning bir qismi deb hisoblashi mumkin.

## Ajratgich tafovutlaridan foydalanish (eksploitatsiya)

Ajratgich tafovutidan foydalanib, kesh tomonidan koʻriladigan, lekin origin server tomonidan eʼtiborga olinmaydigan statik kengaytmani yo‘lga qoʻshishingiz mumkin. Buning uchun origin server tomonidan ajratgich sifatida ishlatiladigan, lekin kesh tomonidan ishlatilmaydigan belgini topishingiz kerak.

1. **Origin server ishlatadigan ajratgichlarni aniqlash**
   Maqsadli endpoint URL-ga ixtiyoriy bir satr qo‘shib boshlang. Masalan, `/settings/users/list` ni `/settings/users/listaaa` ga oʻzgartiring. Bu javobni asos (reference) sifatida saqlaysiz.

   * Agar javob asliga teng boʻlsa — bu yo‘l redirect qilinmoqda degani; boshqa endpoint tanlang.

2. **Ajratgichni sinash**
   Endi asl yo‘l bilan ixtiyoriy satr orasiga ehtimoliy ajratgich belgini qo‘shing, masalan `/settings/users/list;aaa`:

   * Agar javob asosiy javobga teng boʻlsa, bu `;` belgisi ajratgich sifatida ishlatiladi va origin server yo‘lni `/settings/users/list` deb talqin qiladi.
   * Agar javob `listaaa` bilan olingan javobga mos kelsa, `;` ajratgich emas va origin server yo‘lni `/settings/users/list;aaa` deb talqin qiladi.

3. **Keshning ajratgichdan foydalanishini sinash**
   Origin server ajratgichlarni ishlatayotganini aniqlagach, kesh ham shunday ajratgichni ishlatayotganini yoki yo‘qligini tekshiring. Buning uchun yo‘l oxiriga statik kengaytma qo‘shing (masalan `.js`, `.css`, `.ico`, `.exe`). Agar javob keshlansa, bu quyidagilarga ishora qiladi:

   * Kesh ajratgichni ishlatmaydi va to‘liq URL yo‘lini statik kengaytma bilan birga talqin qiladi.
   * Keshda `.js` kabi kengaytmalar uchun javoblarni saqlash qoidasi mavjud.

Sinovlaringizda barcha ASCII belgilarini va keng tarqalgan kengaytmalarni tekshirish foydali bo‘ladi. Laboratoriyalarimizda Web cache deception lab delimiter ro‘yxatini berilgan — shu ro‘yxatdan foydalaning. Burp Intruder yordamida bu belgilarni tezda test qilishingiz mumkin. Burp Intruder delimiter belgilarini avtomatik kodlamasligi uchun Payload encoding bo‘limidagi avtomatik belgilar kodlashni o‘chirib qo‘ying.

Keyin siz static extension kesh qoidalarini trigger qiluvchi exploit yaratishingiz mumkin. Masalan: `/settings/users/list;aaa.js` payloadi:

* Kesh bu yo‘lni `/settings/users/list;aaa.js` deb talqin qiladi.
* Origin server esa `;` ni ajratgich deb hisoblab yo‘lni `/settings/users/list` deb talqin qiladi.
* Origin dinamik profil maʼlumotlarini qaytaradi — va bu javob keshga yoziladi.

Chunki ajratgichlar odatda har bir server ichida izchil ishlatiladi, shu hujumni koʻpincha bir nechta endpointlarda qo‘llash mumkin.

**Eslatma**
Baʼzi ajratgich belgilar jabrlanuvchining brauzeri tomonidan keshga yuborilishdan oldin qayta ishlanishi mumkin. Bu baʼzi ajratgichlarni exploitda ishlatib bo‘lmasligini anglatadi. Masalan, brauzerlar `{`, `}`, `<`, `>` kabi belgilarni URL-encode qiladi va `#` belgisi yo‘lni kesadi. Agar kesh yoki origin server bu belgilarni dekodlasa, exploitda kodlangan (encoded) versiyasini ishlatish mumkin.
