Fayl yuklashdagi zaifliklar — bu veb-server foydalanuvchilarga fayllarni tizimga yuklash imkonini berganda, ularning nomi, turi, mazmuni yoki hajmini yetarlicha tekshirmaslik holatlaridir. Cheklovlarni to‘g‘ri qo‘llamaslik natijasida hatto oddiygina rasm yuklash funksiyasi ham istalgan, hatto xavfli fayllarni yuklash uchun ishlatilishi mumkin. Bunga server tomonida bajariladigan skript fayllari ham kiradi, ular masofadan kodni ishlatish (remote code execution) imkonini berishi mumkin.

Ba’zi hollarda, faylni yuklashning o‘ziyoq zarar yetkazishi mumkin. Boshqa hujumlarda esa odatda keyingi HTTP so‘rovi orqali faylni chaqirish, ko‘pincha uni server tomonidan bajarilishini qo‘zg‘atish talab qilinadi.

Qanday qilib fayl yuklash zaifliklari yuzaga keladi?
Haqiqiy xavflar juda ravshan bo‘lgani uchun veb-saytlarda hech qanday cheklovlar bo‘lmasligi kam uchraydi. Ko‘proq holatlarda dasturchilar o‘ylaganlaricha mustahkam tekshiruvlar joriy qilishadi, lekin ular tabiatan nuqsonli bo‘ladi yoki osonlikcha aylanib o‘tiladi.

Masalan, ular xavfli fayl turlarini qora ro‘yxatga olishga harakat qilishi mumkin, ammo fayl kengaytmasini tekshirishda tahlil (parsing) farqlarini hisobga olmay qolishadi. Har qanday qora ro‘yxat kabi, kam mashhur yoki noan’anaviy fayl turlarini tasodifan unutib qo‘yish ham oson.

Boshqa hollarda veb-sayt fayl turini tekshirish uchun osongina hujumchi tomonidan o‘zgartirilishi mumkin bo‘lgan xususiyatlarni tekshiradi — masalan, Burp Proxy yoki Repeater kabi vositalar bilan manipulyatsiya qilinishi mumkin.

Oxir-oqibat, hatto nisbatan qat’iy tekshiruv choralari ham veb-saytni tashkil etuvchi xostlar va kataloglar tarmog‘ida bir xil qo‘llanilmasligi mumkin; bu esa ekspluatatsiya qilish uchun farqlar (diskrepansiyalar) paydo bo‘lishiga olib keladi.


Serverda web shell joylashtirish uchun cheklovlarsiz fayl yuklashni ekspluatatsiya qilish
Xavfsizlik nuqtai nazaridan eng yomon holat — veb-sayt sizga PHP, Java yoki Python kabi server tomonida bajariladigan skriptlarni yuklashga ruxsat berishi va server ularni kod sifatida bajariladigan qilib sozlangan bo‘lishi. Bunday vaziyatda serverga o‘z web shell’ingizni joylashtirish juda osonlashadi.

Web shell
Web shell — bu hujumchiga faqatgina to‘g‘ri endpoint’ga HTTP so‘rov jo‘natish orqali masofadagi veb-serverda istalgan buyruqlarni bajarish imkonini beruvchi zararli skriptdir.

Agar siz web shell’ni muvaffaqiyatli yuklay olsangiz, amalda server ustidan to‘liq nazoratga ega bo‘lasiz. Bu demak, fayllarni o‘qish va yozish, sezgir ma’lumotlarni o‘g‘irlash va hatto serverni ichki infratuzilma yoki tarmoqdan tashqaridagi boshqa serverlarga qarshi hujumlarda pivot (o‘tkazish) uchun ishlatish imkoniyati mavjud bo‘ladi. Masalan, quyidagi PHP bir qatorli kod server fayl tizimidagi istalgan faylni o‘qish uchun ishlatilishi mumkin:

```php
<?php echo file_get_contents('/path/to/target/file'); ?>
```

Yuklanganidan so‘ng, ushbu zararli faylga so‘rov yuborish javobda maqsad faylning mazmunini qaytaradi.

Ko‘proq funksional web shell quyidagicha bo‘lishi mumkin:

```php
<?php echo system($_GET['command']); ?>
```

Ushbu skript orqali siz quyidagi kabi so‘rov bilan istalgan tizim buyruğini (system command) query parametri orqali o‘tkazishingiz mumkin:

GET /example/exploit.php?command=id HTTP/1.1

Fayl yuklashning noto‘g‘ri tekshiruvini ekspluatatsiya qilish
Amaliyotda oldingi laboratoriyada ko‘rib chiqqanimizdek, fayl yuklash hujumlariga qarshi umuman himoya yo‘q bo‘lgan veb-sayt topish ehtimoli kam. Ammo himoya choralari mavjudligi ularning mustahkam ekanligini anglatmaydi. Ba’zan ushbu mexanizmlardagi kamchiliklardan foydalanib, masofadan kodni bajarish (remote code execution) uchun web shell olish mumkin.

Fayl turini noto‘g‘ri tekshirish
HTML formalar yuborilganda, brauzer odatda yuborilgan ma’lumotni `application/x-www-form-urlencoded` kontent-turi bilan POST so‘rovi sifatida jo‘natadi. Bu ism yoki manzil kabi oddiy matnlarni jo‘natish uchun yetarli. Biroq, butun rasm fayli yoki PDF hujjat kabi katta miqdorda ikkilik (binary) ma’lumotlarni yuborish uchun bu mos emas. Bunday holatda `multipart/form-data` kontent-turi afzal hisoblanadi.

Rasm yuklash, uning tavsifi va foydalanuvchi nomi uchun maydonlari bo‘lgan forma haqida o‘ylang. Bunday forma yuborilganda so‘rov quyidagicha ko‘rinishga ega bo‘lishi mumkin:

```http
POST /images HTTP/1.1
Host: normal-website.com
Content-Length: 12345
Content-Type: multipart/form-data; boundary=---------------------------012345678901234567890123456

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="image"; filename="example.jpg"
Content-Type: image/jpeg

[...binary content of example.jpg...]

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="description"

This is an interesting description of my image.

---------------------------012345678901234567890123456
Content-Disposition: form-data; name="username"

wiener
---------------------------012345678901234567890123456--
```

Ko‘rib turganingizdek, xabar tanasi formaning har bir kirish maydoni uchun alohida bo‘laklarga bo‘lingan. Har bir bo‘lak unga tegishli kirish maydoni haqida asosiy ma’lumotni beruvchi `Content-Disposition` sarlavhasini o‘z ichiga oladi. Ushbu bo‘laklarda serverga yuborilgan ma’lumotning MIME turini bildiruvchi o‘zining `Content-Type` sarlavhasi ham bo‘lishi mumkin.

Veb-saytlar fayl yuklashni tekshirishga urinishlaridan biri — bu ushbu kirish maydoniga xos `Content-Type` sarlavhasi kutilgan MIME turiga mos kelishini tekshirishdir. Masalan, agar server faqat rasm fayllarini kutayotgan bo‘lsa, u faqat `image/jpeg` yoki `image/png` turlariga ruxsat berishi mumkin. Muammolar server ushbu sarlavhaning qiymatiga ko‘r-ko‘rona ishonib qolganida yuzaga keladi. Agar faylning mazmuni haqiqatan ham ko‘rsatilgan MIME turiga mos kelishini aniqlash uchun qo‘shimcha tekshiruv o‘tkazilmasa, bunday himoyani Burp Repeater kabi vositalardan foydalanib osonlikcha aylanib o‘tish mumkin.
