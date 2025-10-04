Quyidagi matnni o‘zbek (lotin) tiliga tarjima qildim.

---

**Delimetr (ajratgich) dekodlashidagi nomuvofiqliklar**
Veb-saytlar URL ichida maxsus maʼnoga ega bo‘lgan belgilar — masalan, delimetrlar — bo‘lishi mumkin bo‘lgan maʼlumotlarni yuborishi kerak bo‘ladi. Ushbu belgilar maʼlumot sifatida to‘g‘ri talqin qilinishini taʼminlash uchun odatda kodlanadi. Biroq, baʼzi parserlar URLni qayta ishlashdan oldin ayrim belgilarni dekodlab olishadi. Agar delimetr belgisi dekodlash natijasida asl delimetrga aylansa, u holda URL yo‘lini truncatsiya (qisqartirish) qiluvchi delimetr sifatida qabul qilinishi mumkin.

Kesh serveri va asosiy (origin) server qaysi delimetr belgilarni dekodlaydi — bunga bog‘liq farqlar — ular URL yo‘lini qanday talqin qilishlarida nomuvofiqliklarga olib kelishi mumkin, hatto ikkalasi ham bir xil belgilarni delimetr sifatida ishlatsa ham. Masalan, `/profile%23wcd.css` URLida `%23` bilan kodlangan `#` belgisi ishlatilgan:

* Asosiy server `%23`ni `#` ga dekodlaydi. U `#`ni delimetr sifatida ishlatadi, shuning uchun yo‘lni `/profile` deb talqin qiladi va profil maʼlumotini qaytaradi.
* Kesh esa `%23`ni dekodlamaydi, lekin u ham `#`ni delimetr sifatida ko‘radi. U esa yo‘lni `/profile%23wcd.css` deb talqin qiladi. Agar `.css` kengaytmasi uchun kesh qoidasi mavjud bo‘lsa, u javobni keshga saqlaydi.

Bundan tashqari, baʼzi kesh serverlari URLni dekodlab, keyin so‘rovni dekodlangan holda keyingi serverga yuborishi mumkin. Boshqalar esa avval kodlangan URL asosida kesh qoidalarini qo‘llaydi, so‘ng URLni dekodlab keyingi serverga yuboradi. Bu xatti-harakatlar ham kesh va asosiy serverlar URL yo‘lini talqin qilishda nomuvofiqliklarga olib kelishi mumkin. Masalan, `/myaccount%3fwcd.css` misolini ko‘rib chiqing:

* Kesh server kodlangan yo‘l — `/myaccount%3fwcd.css` — asosida kesh qoidalarini qo‘llaydi va `.css` kengaytmasi uchun qoidalar mavjudligi sababli javobni saqlashga qaror qiladi. Keyin u `%3f`ni `?` ga dekodlab, qayta yozilgan so‘rovni origin serverga yuboradi.
* Origin server `/myaccount?wcd.css` so‘rovini oladi. U `?` belgini delimetr sifatida ishlatadi, shuning uchun yo‘lni `/myaccount` deb talqin qiladi.

**Delimetr dekodlashdagi nomuvofiqliklardan foydalanish (ekspluatatsiya qilish)**
Agar kesh va origin serverlar orasida dekodlashdagi nomuvofiqlik mavjud bo‘lsa, siz kodlangan delimetrni ishlatib, kesh tomonidan ko‘riladigan yo‘lga statik kengaytma qo‘shishingiz mumkin, lekin origin server bu kengaytmani ko‘rmasligi mumkin.

Delimetr nomuvofiqliklarini aniqlash va ekspluatatsiya qilish uchun ishlatgan sinov metodologiyangizni davom ettiring, lekin kodlangan belgilar diapazonini sinab chiqing. Ayniqsa kodlangan no-chop etiladigan belgilarni — `%00`, `%0A` va `%09` kabi — sinab ko‘ring. Agar ushbu belgilar dekodlangan bo‘lsa, ular ham URL yo‘lini truncatsiya qilishi mumkin.

