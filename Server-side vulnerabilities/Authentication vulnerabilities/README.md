**Autentifikatsiya zaifliklari**

Konseptual jihatdan autentifikatsiya zaifliklarini tushunish oson. Ammo ular odatda juda muhim hisoblanadi, chunki autentifikatsiya va xavfsizlik o‘rtasida bevosita bog‘liqlik mavjud.

Autentifikatsiya zaifliklari hujumchilarga maxfiy ma’lumotlar va funksiyalarga kirish imkonini berishi mumkin. Shuningdek, ular qo‘shimcha hujum yuzasini ochib beradi va boshqa ekspluatatsiyalar uchun imkoniyat yaratadi. Shu sababli autentifikatsiya zaifliklarini aniqlash, ulardan foydalanish va keng tarqalgan himoya choralarini chetlab o‘tishni o‘rganish juda muhimdir.

Ushbu bo‘limda biz quyidagilarni tushuntiramiz:

* Veb-saytlarda qo‘llaniladigan eng keng tarqalgan autentifikatsiya mexanizmlari.
* Ushbu mexanizmlardagi mumkin bo‘lgan zaifliklar.
* Turli autentifikatsiya mexanizmlarining o‘ziga xos zaifliklari.
* Noto‘g‘ri implementatsiya tufayli yuzaga keladigan odatiy zaifliklar.
* O‘z autentifikatsiya mexanizmlaringizni imkon qadar ishonchli qilish usullari.

**Autentifikatsiya va Avtorizatsiya o‘rtasidagi farq**

🔑 **Autentifikatsiya** – foydalanuvchining o‘zini kim deb tanishtirayotganini tekshirish jarayoni.

🔒 **Avtorizatsiya** – foydalanuvchiga ma’lum bir amalni bajarishga ruxsat berilgan-berilmaganini tekshirish jarayoni.

**Misol:**

* **Autentifikatsiya**: Carlos123 nomli foydalanuvchi saytga kirishga harakat qilsa, tizim u haqiqatan ham shu akkauntni yaratgan shaxs ekanini tekshiradi.
* **Avtorizatsiya**: Carlos123 tizimga muvaffaqiyatli kirgach, uning huquqlari tekshiriladi. Masalan, u boshqa foydalanuvchilarning shaxsiy ma’lumotlariga kirishga yoki ularning akkauntini o‘chirishga ruxsatga ega bo‘lishi mumkin.

👉 Xullas: **Autentifikatsiya = "Siz kimsiz?"**, **Avtorizatsiya = "Siz nima qila olasiz?"**


**Bruteforce hujumlari**

**Bruteforce hujumi** – bu hujumchi tizimga kirish uchun amal qiluvchi foydalanuvchi ma’lumotlarini (login va parollarni) topishga urinishda sinov va xatolik usulidan foydalanadigan holatdir. Bunday hujumlar odatda foydalanuvchi nomlari va parollar ro‘yxatlari (wordlist) yordamida avtomatlashtiriladi. Jarayonni avtomatlashtirish, ayniqsa maxsus vositalardan foydalanganda, hujumchiga juda katta tezlikda juda ko‘p sonli login urinishlarini amalga oshirish imkonini beradi.

Bruteforce har doim ham foydalanuvchi nomi va parollarni butunlay tasodifiy taxmin qilishdan iborat emas. Hujumchilar oddiy mantiq yoki ochiq manbalardan olingan ma’lumotlardan foydalanib, taxminlarini ancha “aqlli” qilishlari mumkin. Bu esa bunday hujumlarning samaradorligini sezilarli darajada oshiradi. Agar veb-saytlar foydalanuvchini autentifikatsiya qilishda faqat parolga asoslangan tizimdan foydalansa va yetarli bruteforce himoyasini o‘rnatmagan bo‘lsa, juda zaif bo‘lib qoladi.


**Foydalanuvchi nomlarini bruteforce qilish**

Foydalanuvchi nomlarini taxmin qilish juda oson bo‘lishi mumkin, agar ular aniq bir andozaga asoslangan bo‘lsa, masalan, elektron pochta manzili. Masalan, ko‘plab korxonalarda login shakli **[ism.familiya@somecompany.com](mailto:ism.familiya@somecompany.com)** ko‘rinishida bo‘lishi keng tarqalgan. Hatto aniq bir andoza bo‘lmagan hollarda ham, ba’zan yuqori huquqli akkauntlar **admin** yoki **administrator** kabi oson taxmin qilinadigan foydalanuvchi nomlari bilan yaratiladi.

Audit jarayonida, sayt potentsial foydalanuvchi nomlarini oshkor etayotganini tekshirish kerak. Masalan, tizimga kirmasdan turib foydalanuvchi profillariga kirish mumkinmi? Profil mazmuni yashirilgan bo‘lsa ham, profil nomi ko‘pincha login sifatida ishlatiladigan foydalanuvchi nomi bilan bir xil bo‘ladi. Shuningdek, HTTP javoblarini ham tekshirish lozim — ba’zan ularda elektron pochta manzillari ko‘rsatilgan bo‘ladi. Ayrim hollarda, bu manzillar administratorlar yoki IT qo‘llab-quvvatlash xodimlari kabi yuqori huquqli foydalanuvchilarga tegishli bo‘lishi mumkin.

**Parollarni bruteforce qilish**

Parollar ham xuddi shunday bruteforce usuli bilan buzilishi mumkin — murakkablik parolning kuchiga qarab o‘zgaradi. Ko‘plab veb-saytlar parol siyosatini (password policy) joriy qiladi, bu foydalanuvchilarga nazariy jihatdan oddiy bruteforce bilan buzilishi qiyin bo‘lgan yuqori entropiyali parollar yaratishni majbur qiladi. Odatda bu quyidagilarni majburiy qiladi:

* Kamida belgilar soni (minimal uzunlik).
* Katta va kichik harflarning aralashmasi.
* Kamida bitta maxsus belgi.


Biroq, yuqori entropiyali parollar kompyuter uchun yolg’iz qiyin bo‘lsa-da, inson xulq-atvori haqidagi oddiy bilimlardan foydalanib, foydalanuvchilar bu tizimga bexabar ravishda kiritadigan zaifliklardan foydalanish mumkin. Tasodifiy belgilar kombinatsiyasidan iborat kuchli parol o‘rniga, foydalanuvchilar ko‘pincha eslab qolishi oson bo‘lgan parolni oladi va uni parol siyosatiga moslashtirishga harakat qiladi. Masalan, agar `mypassword` ruxsat etilmasa, foydalanuvchilar `Mypassword1!` yoki `Myp4$$w0rd` kabi variantlarni sinab ko‘rishadi.

Agar siyosat foydalanuvchilardan parollarni ma’lum muddatda o‘zgartirib turishni talab qilsa, foydalanuvchilar odatda sevimli parollariga kichik, oldindan bashorat qilinadigan o‘zgarishlar kiritishadi. Masalan, `Mypassword1!` `Mypassword1?` yoki `Mypassword2!` ga aylanadi.

Ehtimoliy credential va bashorat qilinadigan naqshlar haqida bu kabi bilimlar bruteforce hujumlarini oddiygina barcha mumkin kombinatsiyalarni sinashdan ancha murakkab — va shuning uchun samaraliroq — qilishiga imkon beradi.

**Foydalanuvchi nomlarini aniqlash (Username enumeration)**

Foydalanuvchi nomlarini aniqlash — bu hujumchining ma’lum bir foydalanuvchi nomi haqiqiy yoki yo‘qligini aniqlash uchun veb-saytning xulq-atvoridagi o‘zgarishlarni kuzatishi holatidir.

Foydalanuvchi nomlarini aniqlash odatda login sahifasida yuz beradi — masalan, haqiqiy foydalanuvchi nomini kiritib, noto‘g‘ri parol kiritsangiz, tizimning javobi boshqacha bo‘lishi mumkin; yoki ro‘yxatdan o‘tish formalarida, agar kiritilgan foydalanuvchi nomi allaqachon band bo‘lsa. Bu usul hujumchiga haqiqiy foydalanuvchi nomlarining qisqa ro‘yxatini tezda hosil qilish imkonini beradi va shu bilan loginni bruteforce qilish uchun zarur vaqt va kuchni sezilarli darajada kamaytiradi.

**Ikki bosqichli autentifikatsiyani (2FA) chetlab o‘tish**

Ba’zan ikki bosqichli autentifikatsiya (2FA) noto‘g‘ri amalga oshirilgan bo‘lib, uni to‘liq chetlab o‘tish mumkin.

Agar foydalanuvchidan avval parol so‘ralib, keyin alohida sahifada tekshirish kodi kiritilishi talab qilinsa, foydalanuvchi kodni kiritishdan avvalgina «kirgan» holatda bo‘lib qolishi mumkin. Bunday vaziyatda, birinchi autentifikatsiya bosqichini tugatgandan so‘ng to‘g‘ridan-to‘g‘ri faqat «kirgan foydalanuvchilarga» mo‘ljallangan sahifalarga o‘tib bo‘ladimi, deb tekshirish maqsadga muvofiq. Ba’zan sayt ikkinchi bosqich yakunlanganini tekshirmasdan sahifani yuklaydi.
