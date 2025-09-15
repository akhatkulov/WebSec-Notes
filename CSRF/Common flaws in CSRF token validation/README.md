CSRF tokenlarini noto‘g‘ri tekshirishdagi umumiy xatoliklar

CSRF zaifliklari odatda CSRF tokenlarini noto‘g‘ri tekshirish tufayli yuzaga keladi. Quyida hujumchilarga bu himoyalarni aylanib o‘tish imkonini beruvchi eng keng tarqalgan muammolar keltirilgan.

### CSRF tokenini tekshirish so‘rov metodiga bog‘liq bo‘lishi

Ba’zi ilovalar tokenni POST metodi ishlatilganda to‘g‘ri tekshiradi, lekin GET metodi ishlatilganda tekshiruvni o'tkazib yuboradi.

Bu holatda hujumchi tekshiruvni aylanib o‘tish uchun GET metodiga o‘tishi va CSRF hujumini yetkazishi mumkin:

```
GET /email/change?email=pwned@evil-user.net HTTP/1.1
Host: vulnerable-website.com
Cookie: session=2yQIDcpia41WrATfjPqvm9tOkDvkMvLm
```

### CSRF tokeni mavjudligiga bog‘liq tekshiruv

Ba’zi ilovalar token mavjud bo‘lganda uni to‘g‘ri tekshiradi, lekin token olib tashlangan (ya’ni parametr butunlay jo‘natilmagan) holatda tekshiruvni o'tkazib yuboradi.

Bu holatda hujumchi tokenni o‘z ichiga olgan parameterni (faqat qiymatini emas, balki butun parametrni) olib tashlab CSRF hujumini amalga oshirishi mumkin:

```
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 25
Cookie: session=2yQIDcpia41WrATfjPqvm9tOkDvkMvLm

email=pwned@evil-user.net
```

### CSRF tokeni foydalanuvchi sessiyasiga bog‘lanmagan

Ba’zi ilovalar tokenning so‘rovni yuborgan foydalanuvchining sessiyasiga tegishli ekanligini tekshirmaydi. Buning o‘rniga ilova chiqarilgan tokenlarning global havzasini saqlaydi va ushbu havzada mavjud bo‘lgan har qanday tokenni qabul qiladi.

Bu holatda hujumchi o‘z hisobiga kirib, haqiqiy token olishi va so‘ngra bu tokenni qurbonga yetkazib, CSRF hujumini amalga oshirishi mumkin.

### CSRF tokeni sessiya cookie’siga emas, boshqa cookie’ga bog‘langan

Oldingi zaiflikning bir varianti sifatida, ba’zi ilovalar CSRF tokenini cookie bilan bog‘laydi, lekin sessiyalarni kuzatishda ishlatiladigan cookie bilan emas. Bu, masalan, sessiya boshqaruvi va CSRF himoyasi uchun turli framework’lar ishlatilganda va ular bir-biri bilan integratsiyalashmagan bo‘lsa sodir bo‘lishi mumkin:

```
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Cookie: session=pSJYSScWKpmC60LpFOAHKixuFuM4uXWF; csrfKey=rZHCnSzEp8dbI6atzagGoSYyqJqTz5dv

csrf=RhV7yQDO0xcq9gLEah2WVbmuFqyOq7tY&email=wiener@normal-user.com
```

Bu holatni ekspluatatsiya qilish qiyinroq, lekin u hali ham zaif. Agar saytda hujumchiga qurbonning brauzerida cookie o‘rnatishga imkon beruvchi xatti-harakat bo‘lsa, hujum amalga oshishi mumkin. Hujumchi o‘z hisobiga kirib haqiqiy token va unga mos cookie oladi, cookie o‘rnatish funksiyasidan foydalanib o‘z cookie’sini qurbonning brauzerida o‘rnatadi va tokenini qurbonga yuboradi.

**Eslatma:** cookie o‘rnatish funksiyasi CSRF zaifligi mavjud bo‘lgan bir xil web-ilovada bo‘lishi shart emas. Umumiy DNS domen ichidagi har qanday boshqa ilova cookie’larni o‘rnatish uchun ishlatilishi mumkin, agar boshqarilayotgan cookie mos scope (domen/yo‘l) bilan bo‘lsa. Masalan, `staging.demo.normal-website.com` dagi cookie o‘rnatish funksiyasi `secure.normal-website.com` ga yuboriladigan cookie’ni joylashtirish uchun foydalanilishi mumkin.

### CSRF tokeni oddiygina cookie ichida takrorlanadi

Yana bir varianti — ba’zi ilovalar chiqarilgan tokenlarning server tomonida yozuvini saqlamaydi, balki tokenni cookie va so‘rov parametri ichida takrorlaydi. So‘nggi so‘rov tekshirilayotganda, ilova so‘rov parametrida jo‘natilgan token cookie qiymati bilan mos kelishini tekshiradi. Bu ba’zida CSRF ga qarshi "double submit" (ikki marta yuborish) himoyasi deb ataladi — sodda va server tarafida holat (state) talab qilmaydi, shuning uchun qo‘llanadi:

```
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 68
Cookie: session=1DQGdzYbOJQzLP7460tfyiv3do7MjyPw; csrf=R8ov2YBfTYmzFyjit8o2hKBuoIjXXVpa

csrf=R8ov2YBfTYmzFyjit8o2hKBuoIjXXVpa&email=wiener@normal-user.com
```

Bu holatda, agar saytda cookie o‘rnatish funksiyasi mavjud bo‘lsa, hujumchi CSRF hujumini amalga oshirishi mumkin. Hujumchi o‘z tokenini (zarur formatda bo‘lsa — formatga mos keluvchi) ixtiyoriy ravishda yaratadi, cookie o‘rnatish xatti-harakatidan foydalanib o‘z cookie’sini qurbonning brauzeriga joylashtiradi va so‘rov parametriga shu tokenni yuboradi.
