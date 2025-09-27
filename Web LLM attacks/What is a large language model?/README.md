Katta til modellari (LLM – Large Language Models) – bu foydalanuvchi kiritmalarini qayta ishlay oladigan va so‘zlar ketma-ketligini bashorat qilish orqali mantiqiy javoblar hosil qiladigan sun’iy intellekt algoritmlaridir. Ular juda katta ochiq va yarim-ochiq ma’lumotlar to‘plamida o‘qitilgan bo‘lib, mashinaviy o‘qitish yordamida tilning tarkibiy qismlari qanday bog‘lanishini tahlil qiladi.

LLM odatda foydalanuvchi kiritmalarini (prompt) qabul qilish uchun chat interfeysini taqdim etadi. Kiritishga ruxsat qoidalari qisman inputlarni tekshirish (input validation) orqali boshqariladi.

LLM’larning zamonaviy veb-saytlardagi qo‘llanish sohalari keng bo‘lishi mumkin:

* Mijozlarga xizmat ko‘rsatish, masalan, virtual yordamchi sifatida.
* Tarjima.
* SEO samaradorligini oshirish.
* Foydalanuvchi yaratgan kontentni tahlil qilish, masalan, sharhlardagi ohangni kuzatish.

### LLM hujumlari va prompt injection

Ko‘pgina veb LLM hujumlari **prompt injection** deb nomlangan texnikaga asoslanadi. Bunda hujumchi maxsus yozilgan promptlar orqali LLM chiqishini manipulyatsiya qiladi. Prompt injection natijasida sun’iy intellekt o‘zining asl vazifasidan tashqarida harakat qilishi mumkin, masalan, sezgir API’larni noto‘g‘ri chaqirishi yoki o‘z qo‘llanma tamoyillariga mos kelmaydigan kontentni qaytarishi mumkin.

### LLM’dagi zaifliklarni aniqlash

LLM zaifliklarini aniqlash uchun biz quyidagi metodologiyani tavsiya qilamiz:

1. LLM’ning kirish ma’lumotlarini aniqlash – to‘g‘ridan-to‘g‘ri (prompt kabi) va bilvosita (o‘quv ma’lumotlari kabi).
2. LLM qaysi ma’lumotlar va API’larga kirish imkoniga ega ekanini aniqlash.
3. Ushbu yangi hujum yuzasini zaifliklar uchun sinovdan o‘tkazish.
