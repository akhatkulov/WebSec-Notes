**Avtomatlashtirilgan vositalar bilan test qilish**

Burp’da server-side parameter pollution (SSPP) zaifliklarini aniqlashga yordam beradigan avtomatlashtirilgan vositalar mavjud.

**Burp Scanner** audit vaqtida shubhali input transformatsiyalarini avtomatik ravishda aniqlaydi. Bunday holatlar dastur foydalanuvchi kiritmalarini qabul qilib, uni qandaydir tarzda o‘zgartirganda va keyin natijani qayta ishlaganda sodir bo‘ladi. Bu xatti-harakat har doim ham zaiflikni anglatmaydi, shuning uchun yuqorida keltirilgan **qo‘lda test qilish texnikalari** yordamida qo‘shimcha tekshiruv o‘tkazishingiz kerak bo‘ladi. Qo‘shimcha ma’lumot uchun **Suspicious input transformation issue definition** bo‘limiga qarang.

Bundan tashqari, siz **Backslash Powered Scanner BApp** vositasidan server-side injeksiya zaifliklarini aniqlash uchun foydalanishingiz mumkin. Skanner kiritmalarni **zerikarli (boring)**, **qiziqarli (interesting)** yoki **zaif (vulnerable)** sifatida tasniflaydi. Qiziqarli kiritmalarni yuqorida keltirilgan **qo‘lda test qilish texnikalari** yordamida o‘zingiz tekshirishingiz kerak bo‘ladi. Qo‘shimcha ma’lumot uchun **Backslash Powered Scanning: hunting unknown vulnerability classes** oq qog‘ozini (whitepaper) ko‘rib chiqing.

