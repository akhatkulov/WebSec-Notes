**Xato asosidagi SQL injeksiya**

Xato asosidagi SQL injeksiya — bu siz ma’lumotlar bazasidan sezgir ma’lumotlarni olish yoki taxmin qilish uchun xato xabarlaridan foydalana oladigan holatlardir, hatto ko‘r (blind) kontekstlarda ham. Bu imkoniyatlar ma’lumotlar bazasining konfiguratsiyasi va siz qo‘zg‘ata oladigan xato turlariga bog‘liq:

* Siz ilovani mantiqiy ifodaning natijasiga qarab ma’lum bir xato javobini qaytarishga majbur qilishingiz mumkin. Buni biz oldingi bo‘limda ko‘rib chiqqan shartli javoblarni ekspluatatsiya qilish kabi usulda ishlatish mumkin. Batafsilroq ma’lumot uchun qarang: **Shartli xatolarni qo‘zg‘atish orqali ko‘r SQL injeksiyasidan foydalanish**.
* Siz so‘rovdan qaytgan ma’lumotlarni chiqaradigan xato xabarlarini qo‘zg‘atishingiz mumkin. Bu esa aslida ko‘r SQL injeksiya zaifliklarini ko‘rinadigan zaifliklarga aylantiradi. Batafsilroq ma’lumot uchun qarang: **Batafsil SQL xato xabarlari orqali sezgir ma’lumotlarni ajratib olish**.
