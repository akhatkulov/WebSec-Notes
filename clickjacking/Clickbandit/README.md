

**Clickbandit**
Yuqorida tavsiflanganidek, clickjacking bo‘yicha proof-of-conceptni (PoC) qo‘lda yaratish mumkin bo‘lsa-da, amalda bu juda charchatuvchi va vaqt talab qiladigan ish bo‘lishi mumkin. “Wild” (haqiqiy) saytlarni test qilayotganda, Burp Suite’ning **Clickbandit** vositasidan foydalanishni tavsiya qilamiz.

Bu vosita sizga brauzer orqali frame-lanadigan sahifadagi kerakli harakatlarni bajarishga imkon beradi, so‘ngra mos clickjacking overlay’ini o‘z ichiga olgan HTML fayl yaratadi. Shu yo‘l bilan siz **biror HTML yoki CSS yozmasdan**, interaktiv proof-of-conceptni bir necha soniya ichida yaratishingiz mumkin.

---

**Oldindan to‘ldirilgan form input bilan clickjacking**
Ba’zi veb-saytlar formani to‘ldirish va yuborishni talab qiladi, lekin ular **GET parametrlaridan foydalangan holda form inputlarini oldindan to‘ldirish**ga ruxsat beradi. Boshqa saytlar esa yuborishdan oldin matn kiritishni talab qilishi mumkin.

GET qiymatlari URL tarkibiga kiradiganligi sababli, maqsadli URLni hujumchining istagan qiymatlarini qo‘shish uchun o‘zgartirish mumkin. Shundan so‘ng, shaffof “submit” tugmasi aldov saytining ustiga joylashtiriladi, xuddi oddiy clickjacking misolida bo‘lgani kabi.

