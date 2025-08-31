### Frame busting skriptlar

Clickjacking hujumlari veb-saytlarni **freym** (iframe) ichida ochish mumkin bo‘lganda yuz beradi. Shu sababli, oldini olish texnikalari asosan saytlarni freymlash imkoniyatini cheklashga asoslanadi. Brauzer orqali amalga oshiriladigan keng tarqalgan mijoz (client)-tomon himoya usullaridan biri **frame busting** yoki **frame breaking** skriptlaridan foydalanishdir. Bular maxsus JavaScript qo‘shimchalari yoki kengaytmalari (masalan, NoScript) yordamida ham joriy etilishi mumkin.
Skriptlar odatda quyidagi xatti-harakatlarni bajarishga mo‘ljallanadi:

* joriy ilova oynasi asosiy yoki yuqori darajadagi (top window) oyna ekanligini tekshirish va majburiy qilish,
* barcha freymlarni ko‘rinadigan qilish,
* ko‘rinmaydigan freymlarda bosishni oldini olish,
* ehtimoliy clickjacking hujumlarini ushlab qolish va foydalanuvchiga ogohlantirish.

---

### Frame busting skriptlar – Davomi

Frame busting texnikalari ko‘pincha brauzer va platformaga xos bo‘ladi, va HTML juda moslashuvchan bo‘lgani sababli hujumchilar ularni ko‘pincha aylanib o‘tishlari mumkin. Frame busterlar JavaScript asosida bo‘lgani uchun brauzer xavfsizlik sozlamalari ularning ishlashiga to‘sqinlik qilishi mumkin yoki brauzer umuman JavaScriptni qo‘llamasligi mumkin.

Hujumchilar uchun frame busterlarni aylanib o‘tishning samarali yo‘li — **HTML5 iframe sandbox atributidan** foydalanishdir. Agar sandbox atributiga `allow-forms` yoki `allow-scripts` qiymatlari berilib, lekin `allow-top-navigation` qiymati tashlab ketilsa, frame buster skriptlari **zararsizlantiriladi**, chunki iframe o‘zining yuqori darajadagi oyna ekanligini tekshira olmaydi:

```html
<iframe id="victim_website" src="https://victim-website.com" sandbox="allow-forms"></iframe>
```

`allow-forms` va `allow-scripts` qiymatlari iframe ichida belgilangan amallarni bajarishga ruxsat beradi, lekin **yuqori darajadagi navigatsiya** taqiqlanadi. Bu frame busting mexanizmlarini bloklaydi, lekin nishonga olingan saytning funksionalligini saqlab qoladi.

