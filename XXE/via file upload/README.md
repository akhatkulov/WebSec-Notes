Fayl yuklash orqali XXE hujumlari
Baʼzi ilovalarga foydalanuvchilar fayl yuklashiga ruxsat beriladi va bu fayllar server tomonida qayta ishlanadi. Baʼzi keng tarqalgan fayl formatlari XML ni ishlatadi yoki XML ichki komponentlarini o‘zida saqlaydi. XML asosidagi formatlarga misol qilib ofis hujjat formatlari (masalan, DOCX) va rasm formatlari (masalan, SVG) keltirilishi mumkin.

Masalan, bir ilova foydalanuvchilarga rasmlarni yuklashga ruxsat beradi va yuklangach ularni server tomonida qayta ishlaydi yoki tekshiradi. Ilova PNG yoki JPEG formatlarini qabul qiladi deb hisoblangan bo‘lsa ham, ishlatilayotgan rasmni qayta ishlash kutubxonasi SVG rasmlarni ham qo‘llab-quvvatlashi mumkin. SVG formati XML ga asoslanganligi sababli, hujumchi zararli SVG rasm faylini yuborishi va shu orqali XXE zaifligi uchun yashirin hujum sathiga erisha olishi mumkin.


Masalan SVG Rasm yuklaymiz:
```
<?xml version="1.0" standalone="yes"?><!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/hostname" > ]><svg width="128px" height="128px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"><text font-size="16" x="0" y="16">&xxe;</text></svg>
```
