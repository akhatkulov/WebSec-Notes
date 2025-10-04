Ko‘p-endpointli race condition’lar
Ehtimol, bu race condition turlaridan eng tushunarli bo‘lganlari — bir vaqtda bir nechta endpoint’ga so‘rovlar yuborilganda yuz beradigan holatlardir.

Onlayn do‘konlardagi klassik mantiqiy kamchilikni tasavvur qiling: mahsulotni savatga qo‘yasiz, to‘lovni amalga oshirasiz, so‘ngra buyurtma tasdiqlash sahifasiga majburlab (force-browse) o‘tishdan oldin yana mahsulot qo‘shasiz.

Eslatma
Agar bu eksploit bilan tanish bo‘lmasangiz, Business logic vulnerabilities mavzusidagi *Insufficient workflow validation* laboratoriya mashg‘ulotini ko‘rib chiqing.

To‘lovni tekshirish va buyurtmani tasdiqlash bitta so‘rov ichida bajarilganda bu zaiflikning bir varianti paydo bo‘lishi mumkin. Buyurtma holatining davlat mashinasi (state machine) taxminan quyidagicha ko‘rinishda bo‘lishi mumkin:

Savatni o‘zgartirishdagi mantiqiy kamchilikning race varianti
Bunday holatda, to‘lov tekshirilib, buyurtma oxir-oqibat tasdiqlanishi orasidagi race oynasida savatingizga yana mahsulot qo‘shishingiz mumkin bo‘ladi.

Ko‘p-endpointli race oynalarini moslashtirish
Ko‘p-endpointli race condition’larni sinovdan o‘tkazayotganda, har bir so‘rov uchun race oynalarini moslashtirish (align qilish) bilan bog‘liq muammolarga duch kelishingiz mumkin, hatto agar ularni bitta vaqtda — *single-packet* texnikasi bilan yuboradigan bo‘lsangiz ham.

Ko‘p-endpointli race oynalarini moslashtirish
Ushbu umumiy muammo asosan quyidagi ikki omil tufayli yuzaga keladi:

* Tarmoq arxitekturasi tomonidan kiritilgan kechikishlar — masalan, front-end server back-end bilan yangi aloqa o‘rnatganda kechikish bo‘lishi mumkin. Shuningdek, ishlatilayotgan protokol ham katta ta’sir ko‘rsatadi.
* Endpoint’ga xos ishlov berish tomonidan kiritilgan kechikishlar — turli endpoint’lar o‘zlarining ishlov vaqti jihatidan sezilarli darajada farq qilishi mumkin, bu nimani bajarishi bilan ham bog‘liq.

Xushbo‘lashgan ishlarni (workarounds) topish mumkin.

Connection warming
Back-end bog‘lanish kechikishlari odatda race attack’larni buzmaydi, chunki ular parallel so‘rovlarga teng darajada kechikish beradi va shu bilan so‘rovlar sinxron holatda qoladi.

Bu kechikishlarni endpoint’ga xos omillardan ajrata olish muhim. Buni aniqlashning bir yo‘li — alohida hech qanday ta’siri bo‘lmagan bir yoki bir nechta so‘rov bilan bog‘lanishni “isitish” (warming) va bu qolgan ishlov vaqtlari ustida silliqlik tug‘diradimi-yo‘qligini ko‘rishdir. Burp Repeater’da tab guruhingiz boshiga bosh sahifa uchun GET so‘rovini qo‘shib, so‘ng *Send group in sequence (single connection)* opsiyasidan foydalanib ko‘rishingiz mumkin.

Agar birinchi so‘rov hali ham uzoqroq ishlov vaqtiga ega bo‘lsa, lekin qolgan so‘rovlar endi qisqa oynada qayta ishlansa, siz bu ko‘rinayotgan kechikishni e’tiborga olmasangiz bo‘ladi va sinovlarni normal tarzda davom ettirishingiz mumkin.

Agar bitta endpoint’da ham single-packet texnikasidan foydalanganda ishlov vaqtlari barqaror bo‘lmasa, bu back-end kechikishi hujumga to‘sqinlik qilayotganidan darak beradi. Bunday vaziyatda Turbo Intruder’dan foydalanib, siz asosiy hujum so‘rovlaridan oldin bir nechta connection warming so‘rovlari yuborishingiz mumkin.

Quyidagi matnni o‘zbek tiliga tarjima qildim — asl mazmunni saqlab qoldim.


Agar **ulanishni isitish (connection warming)** hech qanday taʼsir qilmasa, bu muammoning bir nechta yechimlari mavjud.

**Turbo Intruder** yordamida mijoz tomonida (client-side) qisqa kechiktirish kiritishingiz mumkin. Biroq, bu haqiqiy hujum so‘rovlaringizni bir nechta TCP paketlariga bo‘lishni talab qilgani uchun **bir paketli hujum (single-packet attack)** texnikasidan foydalana olmaysiz. Natijada, tarmoq tebranishi yuqori bo‘lgan maqsadlarda (high-jitter), kechiktirishni qanday sozlamang ham, hujum ishonchli ishlamasligi ehtimoli katta.

### So‘rovlar orasida mijoz tomondan kechiktirish kiritish

Buning o‘rniga, siz ushbu muammoni keng tarqalgan xavfsizlik xususiyatini suiisteʼmol qilish orqali hal qilishingiz mumkin.

Veb-serverlar odatda juda tez yuborilgan ko‘p sonli so‘rovlarga ishlov berishni kechiktiradi. Ko‘p miqdorda **soxta (dummy) so‘rovlar** yuborib, sunʼiy ravishda tezlik yoki resurs cheklovini ishga tushirsangiz, server tomoni uchun mos kechiktirish hosil bo‘lishi mumkin. Bu hol server tomonidagi kechiktirishni keltirib chiqaradi va shunday qilib, kechiktirilgan bajarish zarur bo‘lgan holatlarda ham **bir paketli hujum** usulini amalga oshirish imkonini beradi.
