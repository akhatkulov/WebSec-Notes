CSRF hujumini qanday qurish

CSRF eksploitini qo'lda yozish juda ko'p parametrlar bo'lganda yoki so'rovda boshqa nozik jihatlar mavjud bo'lganda noqulay bo'lishi mumkin. CSRF eksploitini qurishning eng oson yo'li — Burp Suite Professional ichida mavjud bo'lgan CSRF PoC generatoridan foydalanish:

1. Burp Suite Professional ichida sinamoqchi yoki eksploit qilmoqchi bo'lgan so'rovni tanlang.
2. O'ng tugma menyusidan Engagement tools / Generate CSRF PoC ni tanlang.
3. Burp Suite tanlangan so'rovni ishga tushiruvchi HTML generatsiya qiladi (cookie-lar bundan mustasno; ular maqsadli foydalanuvchining brauzeri tomonidan avtomatik qo'shiladi).
4. CSRF PoC generatoridagi turli opsiyalarni sozlab, hujumning ayrim jihatlarini noziklash mumkin. Ba'zi g'alati so'rov holatlarida buni qilish kerak bo'lishi mumkin.
5. Yaratilgan HTML ni veb-sahifaga nusxalab joylang, u sahifani zaif veb-saytga tizimga kirgan brauzerda oching va kerakli so'rov yuborilayotganini hamda maqsad qilingan harakat bajarilayotganini sinab ko'ring.

CSRF eksploitini qanday yetkazish

Cross-site request forgery (CSRF) hujumlarini yetkazish usullari asosan reflected XSS hujumlaridagi kabi ishlaydi. Odatda, hujumchi zararli HTML kodini o‘ziga tegishli bo‘lgan saytga joylaydi va qurbonlarni o‘sha saytga tashrif buyurishga majbur qiladi. Buni foydalanuvchiga elektron pochta yoki ijtimoiy tarmoq orqali havola yuborib amalga oshirish mumkin. Agar hujum mashhur saytga joylashtirilgan bo‘lsa (masalan, foydalanuvchi kommentariyasiga), hujumchi shunchaki foydalanuvchilarning saytga kirishini kutadi.

E’tibor bering, ayrim oddiy CSRF eksploitlari GET metodidan foydalanadi va faqat bitta URL orqali to‘liq amalga oshirilishi mumkin. Bu holda hujumchiga tashqi sayt kerak bo‘lmaydi, u to‘g‘ridan-to‘g‘ri zaif domenda joylashgan zararli URL ni qurbonlarga yuborishi mumkin. Masalan, agar elektron pochta manzilini o‘zgartirish GET metodi bilan bajarilsa, unda hujum quyidagicha ko‘rinishda bo‘ladi:

```html
<img src="https://vulnerable-website.com/email/change?email=pwned@evil-user.net">
```
