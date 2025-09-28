
## LLMlarga berilgan API’larni ommaga ochiq deb hisoblang

Foydalanuvchilar LLM orqali amalda API’larni chaqirishi mumkinligi sababli, LLMga kirish imkoniyati berilgan har qanday API’ni ommaga ochiq deb hisoblang. Amaliyotda bu shuni anglatadiki, har doim chaqiriq qilish uchun autentifikatsiyani talab qilish kabi asosiy API kirish nazoratlarini joriy qilishingiz kerak.

Bundan tashqari, LLM o‘zini o‘zi tartibga solishiga umid qilish o‘rniga, har qanday kirish nazoratlarini LLM bilan muloqot qilayotgan ilovalar tomonidan boshqarilishini ta’minlang. Bu, ayniqsa, ruxsatlar bilan bog‘liq bo‘lgan va to‘g‘ridan-to‘g‘ri bo‘lmagan prompt injeksiyasi hujumlarini kamaytirishga yordam beradi.

## LLMlarga maxfiy ma’lumotlarni bermang

Mumkin bo‘lsa, siz integratsiya qilgan LLMlarga maxfiy ma’lumotlarni berishdan saqlaning. LLMga tasodifan maxfiy ma’lumot yetib borishini oldini olish uchun bir nechta choralar mavjud:

* Modelning trening ma’lumotlar to‘plamiga kuchli sanitizatsiya usullarini qo‘llang.
* Modelga faqat eng kam huquqli foydalanuvchi kira oladigan ma’lumotlarni yuboring. Bu muhim, chunki model iste’mol qilgan har qanday ma’lumot foydalanuvchiga oshkor bo‘lishi mumkin, ayniqsa fine-tuning ma’lumotlari ishlatilsa.
* Modelning tashqi ma’lumot manbalariga kirishini cheklang va butun ma’lumot yetkazib berish zanjirida mustahkam kirish nazoratlarini ta’minlang.
* Modelning maxfiy ma’lumotlarga qanchalik ega ekanligini muntazam sinab turing.

## Hujumlarga qarshi bloklash uchun faqat promptlarga tayanmang

LLM chiqishini promptlar yordamida cheklash nazariy jihatdan mumkin: masalan, modelga “bu API’lardan foydalanma” yoki “payload (ma’lumot) o‘z ichiga olgan so‘rovlarga e’tibor bermang” kabi ko‘rsatmalar berish mumkin.

Ammo bunday texnikaga tayanmaslik kerak, chunki tajribali hujumchi “qaysi API’lardan foydalanmaslik kerak” kabi ko‘rsatmalarni inkor etuvchi maxsus tuzilgan promptlar orqali buning atrofidan o‘tishi mumkin. Bunday promptlar ba’zida “jailbreaker” promptlar deb ataladi.
