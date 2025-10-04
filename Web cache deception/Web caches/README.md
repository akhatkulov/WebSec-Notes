Web keshlar
**Web kesh** – bu tizim bo‘lib, u foydalanuvchi va manba serveri (origin server) o‘rtasida joylashadi. Mijoz (client) statik resurs so‘raganida, so‘rov avval keshga yuboriladi. Agar keshda bu resursning nusxasi mavjud bo‘lmasa (bunga *cache miss* deyiladi), so‘rov manba serveriga uzatiladi, u so‘rovni qayta ishlaydi va javob qaytaradi. Bu javob foydalanuvchiga yuborilishidan oldin keshlanadi. Kesh oldindan belgilangan qoidalarga asoslanib, javobni saqlash-yo‘qligini hal qiladi.

Keyinchalik xuddi shu statik resursga so‘rov yuborilsa, kesh undan oldin saqlangan javob nusxasini bevosita foydalanuvchiga yetkazadi (*cache hit* deyiladi).

---

### Keshlash xulq-atvori va Web cache deception

Keshlash – veb-kontentni yetkazib berishda keng qo‘llanadigan muhim usuldir. Ayniqsa **CDN (Content Delivery Network)** keng ishlatiladi. CDN butun dunyo bo‘ylab tarqatilgan serverlarda kontent nusxalarini saqlaydi. Bu foydalanuvchiga eng yaqin serverdan xizmat ko‘rsatadi va ma’lumotning uzoqqa bormasligini ta’minlab, yuklanish vaqtini tezlashtiradi.

---

### Cache key (kesh kaliti)

Kesh HTTP so‘rovini olganda, mavjud keshlangan javobni berish yoki so‘rovni manba serveriga yuborish haqida qaror qilishi kerak bo‘ladi. Buning uchun **cache key** yaratiladi. Cache key odatda URL manzili va query parametrlarini o‘z ichiga oladi, lekin boshqa elementlar ham qo‘shilishi mumkin (masalan, headers yoki content type).

Agar kelayotgan so‘rovning cache key’ i avvalgi so‘rovniki bilan mos tushsa, kesh ularni bir xil deb hisoblaydi va avvalgi javob nusxasini foydalanuvchiga beradi.

📌 **Izoh**
Cache key manipulyatsiyasi orqali keshga zararli kontent joylash mumkin. Buni o‘rganish uchun *Web cache poisoning* mavzusiga qarang.

---

### Cache qoidalari

Cache qoidalari – qaysi ma’lumot saqlanishi va qancha vaqtgacha saqlanishini belgilaydi. Ular odatda **statik resurslar**ni (masalan, rasm, CSS, JS) saqlash uchun ishlatiladi, chunki ular tez-tez o‘zgarmaydi va ko‘plab sahifalarda qayta ishlatiladi.

**Dinamik kontent** esa odatda keshlanmaydi, chunki unda sezgir ma’lumot bo‘lishi mumkin va foydalanuvchilar har doim yangilangan natijani serverdan olishlari kerak.

**Web cache deception hujumlari** – keshlash qoidalaridan noto‘g‘ri foydalanilishini ekspluatatsiya qilish orqali amalga oshiriladi. Shuning uchun quyidagi qoidalarni bilish muhim:

* **Statik fayl kengaytmalari qoidalari** – masalan, `.css` (stylesheetlar uchun), `.js` (JavaScript fayllar uchun).
* **Statik katalog qoidalari** – masalan, `/static` yoki `/assets` bilan boshlanadigan barcha yo‘llar.
* **Fayl nomi qoidalari** – masalan, `robots.txt` yoki `favicon.ico` kabi universal va kamdan-kam o‘zgaradigan fayllar.

Ba’zi keshlarda qo‘shimcha maxsus qoidalar ham bo‘lishi mumkin, masalan URL parametrlariga yoki dinamik tahlil natijalariga asoslangan.
