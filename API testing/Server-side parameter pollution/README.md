Server-side parameter pollution
Ba’zi tizimlarda internet orqali bevosita kira olmaydigan ichki API’lar mavjud bo‘ladi. **Server-side parameter pollution** (server tomonida parametr ifloslanishi) shunda yuzaga keladiki, veb-sayt foydalanuvchi kiritgan qiymatni yetarlicha kodlashsiz ichki API’ga yuboriladigan server so‘roviga qo‘shib yuboradi. Bu esa hujumchiga quyidagi imkoniyatlarni berishi mumkin:

* Mavjud parametrlarni o‘zgartirish.
* Ilovaning xatti-harakatini o‘zgartirish.
* Ruxsatsiz ma’lumotlarga kirish.

Har qanday foydalanuvchi kiritishini parametr ifloslanishiga tekshirish mumkin. Masalan, query parametrlar, formadagi maydonlar, header’lar va URL path parametrlarining barchasi zaif bo‘lishi mumkin.

### Server-side parameter pollution misol

**Eslatma**
Ushbu zaiflik ba’zida *HTTP parameter pollution* deb ham ataladi. Biroq bu atama ko‘pincha veb-ilova firewall’ini (WAF) chetlab o‘tish texnikasiga nisbatan ham ishlatiladi. Shuning uchun chalkashlik bo‘lmasligi uchun bu mavzuda biz faqat *server-side parameter pollution* atamasidan foydalanamiz.

Shuningdek, nomi o‘xshash bo‘lsa-da, ushbu zaiflik sinfi *server-side prototype pollution* bilan deyarli bog‘liq emas.

