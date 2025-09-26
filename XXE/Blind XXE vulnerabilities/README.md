

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
