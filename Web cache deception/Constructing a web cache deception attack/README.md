# Veb-kesh aldov (web cache deception) hujumini qurish

Umuman olganda, oddiy bir veb-kesh aldov hujumini qurish quyidagi bosqichlarni oʻz ichiga oladi:

1. **Maqsadli endpointni aniqlash** — dinamik javob qaytaradigan va sezgir maʼlumotlarni oʻz ichiga olishi mumkin bo‘lgan endpointni toping. Burp-dagi javoblarni tekshiring, chunki baʼzi sezgir maʼlumotlar sahifada ko‘rinmasligi mumkin. GET, HEAD yoki OPTIONS metodlarini qo‘llab-quvvatlaydigan endpointlarga eʼtibor bering — odatda server holatini oʻzgartiruvchi soʻrovlar (POST, PUT va hokazo) keshga olinmaydi.

2. **Kesh va origin server URL yo‘lini qanday tahlil qilishi orasidagi tafovutni aniqlash** — bunday tafovut quyidagilardan biri bo‘lishi mumkin:

   * URL-larni resurslarga xaritalashdagi farq.
   * Delimiter (ajratgich) belgilarini qayta ishlashdagi farq.
   * Yoʻlni normalizatsiya qilishdagi farq.

3. **Zararli URL yaratish** — keshni dinamik javobni saqlashga majburlaydigan yo‘lni (yuqoridagi tafovutni foydalangan holda) yasang. Vaqt oʻtib, jabrlanuvchi ushbu URL-ga kirganda, ularning javobi keshga yoziladi. Keyin Burp orqali ayni shu URL-ga soʻrov yuborib, jabrlanuvchining maʼlumotlarini oʻz ichiga olgan keshlangan javobni olish mumkin. Buni brauzerda bevosita bajarishdan saqlaning — baʼzi ilovalar sessiyasiz foydalanuvchilarni boshqa yerga yoʻnaltirishi yoki lokal maʼlumotlarni bekor qilishi mumkin, bu esa zaiflikni yashirishi mumkin.

Quyida veb-kesh aldov hujumini qurish uchun bir nechta yondashuvlarni koʻrib chiqamiz.

## Kesh-baster (cache buster) dan foydalanish

Tafovutlarni tekshirish va web cache deception ekspluatatsiyasini yasashda, yuborayotgan har bir soʻrovingiz alohida kesh kalitiga ega boʻlishiga eʼtibor bering. Aks holda, sizga oldindan keshlangan javob qaytarilishi mumkin va bu test natijalariga taʼsir qiladi.

Kesh kaliti odatda URL yoʻli va soʻrov parametrlarini oʻz ichiga oladi — shuning uchun yo‘lga sorov qatori (query string) qo‘shib, har safar uni oʻzgartirish orqali kalitni yangilashingiz mumkin. Buni avtomatlashtirish uchun Param Miner kengaytmasidan foydalaning. Kengaytmani oʻrnatgach, Param miner > Settings menyusiga kiring, keyin **Add dynamic cachebuster** ni tanlang. Endi Burp har bir soʻrovingizga noyob query string qoʻshadi. Qoʻshilgan query stringlarni Logger tabida koʻrishingiz mumkin.

## Keshlangan javoblarni aniqlash

Test davomida keshlangan javoblarni aniqlay olish juda muhim. Buni qilish uchun javob headerlari va javob vaqtiga eʼtibor bering.

Baʼzi javob headerlari keshdan xizmat ko‘rsatilganini koʻrsatishi mumkin. Masalan:

* **X-Cache** headeri javobning keshdan ekanligini bildiradi. Odatdagi qiymatlar:

  * `X-Cache: hit` — javob keshdan servis qilingan.
  * `X-Cache: miss` — keshda kalit uchun javob yo‘q edi, shuning uchun origin serverdan olindi. Ko‘p hollarda bu javob keyin keshlanadi. Buni tasdiqlash uchun so‘rovni qayta yuboring va qiymat `hit`ga oʻtayaptimi tekshiring.
  * `X-Cache: dynamic` — origin server dinamik tarzda kontent yaratgan. Odatda bu javob keshga mos emasligini anglatadi.
  * `X-Cache: refresh` — keshdagi kontent muddati oʻtgan va yangilanishi (revalidate) talab qilingan.
* **Cache-Control** headerida `public` va `max-age` 0 dan katta boʻlgan direktiva boʻlishi mumkin. Bu resurs keshga olinishi mumkinligini taklif qiladi. Ammo bu har doim ham keshlanganini anglatmaydi — baʼzan kesh origin headerini oʻz qarori bilan eʼtiborsiz qoldirishi mumkin.
* Bir xil soʻrov uchun javob vaqtlari orasida katta farqni sezsangiz, tezroq javob keshdan kelayotgan boʻlishi mumkin.

