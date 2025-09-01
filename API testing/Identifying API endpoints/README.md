### API endpointlarni aniqlash

Siz API dan foydalanadigan ilovalarni ko‘rib chiqish orqali ham ko‘p ma’lumot to‘plashingiz mumkin. Bu ishni API hujjatlari mavjud bo‘lsa ham qilish foydali bo‘ladi, chunki ba’zida hujjatlar noto‘g‘ri yoki eskirgan bo‘lishi mumkin.

Burp Scanner yordamida ilovani crawl qilib, keyin Burp’ning brauzeri orqali qiziqarli hujum yuzalarini qo‘lda tekshirishingiz mumkin.

Ilovani ko‘rib chiqayotganda URL tuzilishida **/api/** kabi API endpointlarni bildiradigan naqshlarga e’tibor bering. Shuningdek, JavaScript fayllariga ham qarang. Bu fayllarda brauzer orqali to‘g‘ridan-to‘g‘ri ishga tushirmagan bo‘lsangiz ham API endpointlarga ishoralar bo‘lishi mumkin. Burp Scanner crawl jarayonida ayrim endpointlarni avtomatik aniqlaydi, lekin yanada kengroq aniqlash uchun **JS Link Finder BApp** dan foydalanishingiz mumkin. Shuningdek, Burp’da JavaScript fayllarini qo‘lda ham ko‘rib chiqishingiz mumkin.

---

### API endpointlar bilan ishlash

Endpointlarni aniqlaganingizdan so‘ng, ularni **Burp Repeater** va **Burp Intruder** orqali sinab ko‘ring. Bu sizga API xatti-harakatlarini kuzatish va qo‘shimcha hujum yuzalarini topish imkonini beradi. Masalan, HTTP metodini yoki media turini o‘zgartirishga API qanday javob berishini tekshirishingiz mumkin.

API endpointlar bilan ishlayotganda, xatolik xabarlari va boshqa javoblarni diqqat bilan kuzating. Ba’zan ular orqali to‘g‘ri HTTP so‘rovini tuzishda yordam beradigan ma’lumotlarga ega bo‘lishingiz mumkin.

---

### Qo‘llab-quvvatlanadigan HTTP metodlarni aniqlash

HTTP metodi resurs ustida bajariladigan amalni belgilaydi. Masalan:

* **GET** – resursdan ma’lumot olish.
* **PATCH** – resursga qisman o‘zgartirish kiritish.
* **OPTIONS** – resursda foydalanish mumkin bo‘lgan metodlar haqida ma’lumot olish.

API endpoint turli metodlarni qo‘llab-quvvatlashi mumkin. Shu sababli, endpointlarni o‘rganayotganda barcha ehtimoliy metodlarni sinab ko‘rish muhimdir. Bu orqali siz qo‘shimcha funksionallikni topib, hujum yuzasini kengaytirishingiz mumkin.

Masalan, **/api/tasks** endpointi quyidagi metodlarni qo‘llab-quvvatlashi mumkin:

* `GET /api/tasks` – vazifalar ro‘yxatini olish.
* `POST /api/tasks` – yangi vazifa yaratish.
* `DELETE /api/tasks/1` – bitta vazifani o‘chirish.

Burp Intruder’dagi o‘rnatilgan **HTTP verbs** ro‘yxatidan foydalanib, turli metodlarni avtomatik ravishda sinab ko‘rishingiz mumkin.

---

### Qo‘llab-quvvatlanadigan kontent turlarini aniqlash

API endpointlar odatda ma’lumotni aniq bir formatda kutadi. Shu sababli, ular so‘rovda ko‘rsatilgan **kontent turi** ga qarab turlicha ishlashi mumkin. Kontent turini o‘zgartirish orqali siz:

* Foydali ma’lumotlarni oshkor qiladigan xatoliklarni chaqirishingiz mumkin.
* Noto‘g‘ri himoya mexanizmlarini chetlab o‘tishingiz mumkin.
* Qayta ishlash mantiqidagi farqlardan foydalanishingiz mumkin.
  Masalan, API JSON ma’lumotlarini qayta ishlashda xavfsiz bo‘lishi mumkin, lekin XML bilan ishlaganda **injection hujumlariga** zaif bo‘lishi ehtimoli bor.

Kontent turini o‘zgartirish uchun `Content-Type` headerini tahrirlash va so‘rov body qismini shunga mos formatga keltirish kerak. **Content type converter BApp** yordamida so‘rovlar ichidagi ma’lumotlarni XML va JSON formatlari o‘rtasida avtomatik konvertatsiya qilish mumkin.

---

### Eslatma

Turli HTTP metodlarni sinab ko‘rayotganda, **past-prioritetli obyektlarni** tanlang. Bu sizning kutilmagan oqibatlardan (masalan, muhim obyektlarni o‘zgartirib yuborish yoki keraksiz yozuvlar yaratish) saqlanishingizga yordam beradi.
