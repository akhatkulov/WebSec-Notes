**Xato asosidagi SQL injeksiya**

Xato asosidagi SQL injeksiya — bu siz ma’lumotlar bazasidan sezgir ma’lumotlarni olish yoki taxmin qilish uchun xato xabarlaridan foydalana oladigan holatlardir, hatto ko‘r (blind) kontekstlarda ham. Bu imkoniyatlar ma’lumotlar bazasining konfiguratsiyasi va siz qo‘zg‘ata oladigan xato turlariga bog‘liq:

* Siz ilovani mantiqiy ifodaning natijasiga qarab ma’lum bir xato javobini qaytarishga majbur qilishingiz mumkin. Buni biz oldingi bo‘limda ko‘rib chiqqan shartli javoblarni ekspluatatsiya qilish kabi usulda ishlatish mumkin. Batafsilroq ma’lumot uchun qarang: **Shartli xatolarni qo‘zg‘atish orqali ko‘r SQL injeksiyasidan foydalanish**.
* Siz so‘rovdan qaytgan ma’lumotlarni chiqaradigan xato xabarlarini qo‘zg‘atishingiz mumkin. Bu esa aslida ko‘r SQL injeksiya zaifliklarini ko‘rinadigan zaifliklarga aylantiradi. Batafsilroq ma’lumot uchun qarang: **Batafsil SQL xato xabarlari orqali sezgir ma’lumotlarni ajratib olish**.

**Shartli xatolarni qo‘zg‘atish orqali ko‘r SQL injeksiyasidan foydalanish**

Ba’zi ilovalar SQL so‘rovlarini bajaradi, lekin so‘rov ma’lumot qaytarsa ham, qaytarmasa ham, ularning xatti-harakati o‘zgarmaydi. Oldingi bo‘limdagi usul bunday vaziyatda ishlamaydi, chunki turli mantiqiy shartlarni kiritish ilovaning javoblariga ta’sir qilmaydi.

Ko‘pincha ilovani SQL xatosi yuzaga kelgan yoki kelmaganiga qarab turlicha javob qaytarishga majbur qilish mumkin bo‘ladi. Siz so‘rovni shunday o‘zgartirishingiz mumkinki, u faqat shart **rost** bo‘lgandagina ma’lumotlar bazasida xato yuzaga kelsin. Juda ko‘p hollarda, bazadan tashlangan boshqarilmagan xato ilova javobida qandaydir farqni keltirib chiqaradi, masalan, xato xabari chiqadi. Bu esa sizga kiritilgan shartning rost yoki yolg‘onligini bilib olish imkonini beradi.

**Shartli xatolarni qo‘zg‘atish orqali ko‘r SQL injeksiyasidan foydalanish – Davomi**

Bu qanday ishlashini ko‘rish uchun tasavvur qiling, ikkita so‘rov quyidagi **TrackingId** cookie qiymatlari bilan ketma-ket yuboriladi:

```
xyz' AND (SELECT CASE WHEN (1=2) THEN 1/0 ELSE 'a' END)='a
xyz' AND (SELECT CASE WHEN (1=1) THEN 1/0 ELSE 'a' END)='a
```

Bu yerda **CASE** kalit so‘zi shartni tekshirish va shart rost yoki yolg‘onligiga qarab turlicha ifodani qaytarish uchun ishlatilgan:

* Birinchi kiritmada **CASE** ifodasi `'a'` ga teng bo‘ladi va hech qanday xato yuzaga kelmaydi.
* Ikkinchi kiritmada esa u `1/0` ga teng bo‘ladi, bu esa **nolga bo‘lish xatosini** (divide-by-zero) keltirib chiqaradi.

Agar xato ilovaning HTTP javobida qandaydir farq keltirib chiqarsa, siz shu orqali kiritilgan shart rost yoki yolg‘onligini aniqlashingiz mumkin.

Ushbu usul yordamida ma’lumotlarni bitta belgidan boshlab tekshirish orqali olish mumkin:

```
xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
```

**Eslatma:**
Shartli xatolarni qo‘zg‘atishning turli usullari mavjud va turli texnikalar turli xil ma’lumotlar bazalarida eng samarali ishlaydi. Batafsilroq ma’lumot uchun **SQL injeksiya cheat sheet** ga qarang.
