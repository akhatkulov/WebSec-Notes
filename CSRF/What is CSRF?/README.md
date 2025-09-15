

### CSRF nima?

Cross-site request forgery (CSRF) — saytlararo so‘rovlarni soxtalashtirish — bu veb-xavfsizlikdagi zaiflik bo‘lib, hujumchiga foydalanuvchini o‘zi xohlamagan harakatlarni bajarishga majbur qilish imkonini beradi. Bu hujum turida hujumchi turli saytlar bir–biriga aralashmasligi uchun mo‘ljallangan **bir xil manba siyosati**ni qisman chetlab o‘tadi.

### CSRF hujumining ta’siri nima?

Muvaffaqiyatli CSRF hujumida hujumchi zarar ko‘rgan foydalanuvchini ixtiyoridan tashqari biror harakatni bajarishga majbur qiladi. Masalan: akkauntdagi elektron pochta manzilini o‘zgartirish, parolni almashtirish yoki pul o‘tkazmasi amalga oshirish. Harakatning xususiyatiga qarab hujumchi foydalanuvchining akkaunti ustidan to‘liq nazoratni qo‘lga kiritishi mumkin. Agar zaif tizimdagi foydalanuvchi vazifasi yuqori (masalan, admin bo‘lsa), hujumchi butun ilova ma’lumotlari va funksiyalarini to‘liq egallashi mumkin.

### CSRF qaysi holatlarda ishlaydi?

CSRF hujumi mumkin bo‘lishi uchun quyidagi uchta shart bo‘lishi kerak:

1. **Maqbul amal**. Ilovada hujumchining foydasiga bo‘ladigan amal mavjud bo‘lishi kerak. Bu o‘z ichiga yuqori huquqli amalni (masalan, boshqa foydalanuvchilarning huquqlarini o‘zgartirish) yoki foydalanuvchiga tegishli ma’lumotlarga taalluqli amalni oladi (masalan, foydalanuvchining parolini o‘zgartirish).
2. **Kukiga asoslangan sessiya boshqaruvi.** Amal bajarilishi bir yoki bir nechta HTTP so‘rovlarni jo‘natishni talab qilishi va ilova faqat sessiya kukilari (session cookies) yordamida foydalanuvchini identifikatsiyalashi kerak. So‘rovlarni tekshirish yoki autentifikatsiya uchun boshqa mexanizmlar mavjud bo‘lmasligi kerak.
3. **Noaniq (bashorat qilib bo‘lmaydigan) so‘rov parametrlarining yo‘qligi.** Amalni bajaruvchi so‘rovlar hujumchi bilmasdan yoki taxmin qila olmasdan parametrlarni o‘zni o‘z ichiga olmasligi kerak. Masalan, parolni o‘zgartirish funksiyasi hujumchidan mavjud parolni bilishni talab qilsa, CSRF bo‘lmaydi.

### Misol (email manzilini o‘zgartirish)

Faraz qilaylik, ilovada foydalanuvchining email manzilini o‘zgartirish funksiyasi bor. Foydalanuvchi ushbu amalni bajarganda quyidagi kabi HTTP so‘rov yuboriladi:

```
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Cookie: session=yvthwsztyeQkAPzeQ5gHgTvlyxHfsAfE

email=wiener@normal-user.com
```

Bu holat CSRF uchun zarur shartlarni qanoatlantiradi:

* Email manzilini o‘zgartirish hujumchi uchun foydali bo‘lgan amal (masalan, keyin parolni tiklash orqali akkauntni egallash mumkin).
* Ilova foydalanuvchini sessiya kukisi orqali identifikatsiyalaydi; boshqa qo‘shimcha tokenlar yoki tekshiruvlar yo‘q.
* Zarur so‘rov parametrlarini (email qiymati) hujumchi osonlik bilan belgilashi mumkin.

Shunda hujumchi mana bunday HTML sahifa yaratishi mumkin:

```html
<html>
    <body>
        <form action="https://vulnerable-website.com/email/change" method="POST">
            <input type="hidden" name="email" value="pwned@evil-user.net" />
        </form>
        <script>
            document.forms[0].submit();
        </script>
    </body>
</html>
```

Agar foydalanuvchi hujumchining sahifasiga tashrif buyursa, quyidagi sodir bo‘ladi:

1. Huquqbuzar sahifasi zaif saytga HTTP so‘rov yuboradi.
2. Agar foydalanuvchi zaif saytga avvaldan tizimga kirgan bo‘lsa, brauzer avtomatik ravishda sessiya kukisini so‘rovga qo‘shadi (agar `SameSite` xususiyatiga ega kukilar ishlatilmagan bo‘lsa).
3. Zaif sayt so‘rovni normal tarzda qayta ishlaydi, so‘rovni foydalanuvchi tomonidan yuborilgan deb hisoblab, emailni o‘zgartiradi.

### Eslatma

Garchi CSRF odatda kukiga asoslangan sessiya boshqaruvi kontekstida tasvirlansa ham, u shuningdek ilova avtomatik ravishda ba’zi foydalanuvchi kredensiallarini so‘rovlarga qo‘shgan boshqa holatlarda ham yuz berishi mumkin — masalan, HTTP Basic autentifikatsiyasi yoki sertifikatga asoslangan autentifikatsiya.

