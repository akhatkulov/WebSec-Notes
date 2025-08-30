Agar ilova SQL so‘rovi bajarilganda yuzaga keladigan xatoliklarni ushlab, ularni to‘g‘ri qayta ishlasa, ilova javobida hech qanday farq bo‘lmaydi. Bu esa shuni anglatadiki, oldingi — shartli xatoliklarni chaqirish usuli ishlamaydi.

Bunday vaziyatda, ko‘pincha, blind SQL injection zaifligini ekspluatatsiya qilish uchun shartga qarab vaqt kechiktirishlarni qo‘zg‘atish mumkin bo‘ladi. SQL so‘rovlari odatda ilova tomonidan sinxron tarzda qayta ishlangani sababli, so‘rovni bajarishda yuzaga keltirilgan kechikish HTTP javobining ham kechikishiga olib keladi. Shu orqali, HTTP javobining qancha vaqt ichida kelishiga qarab, kiritilgan shartning rost yoki yolg‘on ekanligini aniqlash mumkin bo‘ladi.


Vaqt kechiktirishni qo‘zg‘atish texnikalari ishlatilayotgan **ma’lumotlar bazasi turiga** bog‘liq. Masalan, **Microsoft SQL Server** da quyidagi ifodalar yordamida shartni tekshirib, natijaga qarab kechikishni qo‘zg‘atish mumkin:

```
'; IF (1=2) WAITFOR DELAY '0:0:10'--
'; IF (1=1) WAITFOR DELAY '0:0:10'--
```

* Birinchi kiritma kechikishni qo‘zg‘atmaydi, chunki `1=2` sharti noto‘g‘ri.
* Ikkinchi kiritma esa **10 soniyalik kechikishni** qo‘zg‘atadi, chunki `1=1` sharti rost.

Ushbu texnika yordamida biz ma’lumotlarni **har bir belgini alohida tekshirish orqali** olishimiz mumkin:

```
'; IF (SELECT COUNT(Username) FROM Users 
      WHERE Username = 'Administrator' 
      AND SUBSTRING(Password, 1, 1) > 'm') = 1 
   WAITFOR DELAY '0:0:{delay}'--
```
