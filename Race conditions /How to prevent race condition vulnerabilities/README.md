

## Race condition zaifliklarini oldini olish

Agar bitta so‘rov dasturni ko‘rinmas sub-holatlarga (sub-states) o‘tkazishi mumkin bo‘lsa, uning xatti-harakatini tushunish va bashorat qilish nihoyatda qiyin bo‘ladi. Bu esa mudofaani amaliy jihatdan murakkablashtiradi. Ilovani to‘g‘ri himoya qilish uchun, biz barcha sezgir endpointlardan sub-holatlarni olib tashlashni va quyidagi strategiyalarni qo‘llashni tavsiya qilamiz:

* Turli saqlash joylarida (storage) mavjud bo‘lgan ma’lumotlarni aralashtirmang.
* Sezgir endpointlarda holat o‘zgarishlarini atomik (atomic) qiling — buning uchun ma’lumotlar omborining (datastore) konkuren­siya (concurrency) imkoniyatlaridan foydalaning. Masalan, to‘lov summasi kart qiymatiga mos kelishini tekshirish va buyurtmani tasdiqlash uchun bitta ma’lumotlar bazasi transaksiyasidan (transaction) foydalaning.
* Mudofaa qatlamini kuchaytirish maqsadida, ma’lumotlar omborining yaxlitlik va izchillik (integrity and consistency) xususiyatlaridan foydalaning — masalan, ustun darajasidagi (column) noyoblik cheklovlari (uniqueness constraints).
* Bir saqlash qatlamini (storage layer) boshqa bir qatlamni himoya qilish uchun ishlatishga urinmang. Masalan, sessiyalar (sessions) ma’lumotlar bazasidagi limitlarni oshirib yuborishni oldini olish uchun ishonchli himoya vositasi emas.
* Sessiyalarni boshqarish ramkasi (session handling framework) sessiyalarning ichki yaxlitligini ta’minlasin. Sessiya o‘zgaruvchilarini alohida-alohida yangilash (individual updates) tezlashtirish uchun jozibador bo‘lishi mumkin, lekin bu juda xavfli. Bu ORM (Object-Relational Mapper) lar uchun ham xuddi shunday — agar ORM transaksiyalar kabi tushunchalarni yashirib qo‘yayotgan bo‘lsa, ularning to‘liq javobgarligini qabul qilayotganini unutmaslik kerak.
* Ba’zi arxitekturalarda server tomonidagi holatni (server-side state) umuman ishlatmaslik maqbul bo‘lishi mumkin. Buning o‘rniga holatni mijoz tomoniga (client-side) shifrlash orqali surish mumkin — masalan, JWT (JSON Web Token) larni ishlatish. Biroq, buning ham o‘z xavflari bor — bu mavzu JWT hujumlari bo‘yicha biz ilgari kengroq muhokama qilgan xavflardan biridir.

