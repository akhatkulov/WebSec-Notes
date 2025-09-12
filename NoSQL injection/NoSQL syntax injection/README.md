### NoSQL sintaksis injeksiyasi 

NoSQL injeksiyasini aniqlash uchun soʻrov sintaksisini buzishga harakat qilasiz. Buning uchun har bir kirishni tizimli ravishda test qilib, fuzz satrlar va maxsus belgilar yuboring — agar ular ilova tomonidan yetarlicha tozalab yoki filtrlanmagan boʻlsa, bu bazadan xato yoki boshqa aniqlanadigan xulq (behavior)ni keltirib chiqaradi.

Agar maqsadli maʼlumotlar bazasining API tili maʼlum boʻlsa, shu tilga mos maxsus belgilar va fuzz satrlaridan foydalaning. Aks holda, bir nechta API tillarini nishonga oladigan turli fuzz satrlarini sinab koʻring.

#### MongoDB da sintaksis injeksiyasini aniqlash

Masalan, mahsulotlarni turli kategoriyalarda koʻrsatadigan shopping ilovasini olaylik. Foydalanuvchi “Fizzy drinks” kategoriyasini tanlaganda, brauzeri quyidagi URL ga soʻrov yuboradi:

```
https://insecure-website.com/product/lookup?category=fizzy
```

Bu ilova MongoDB dagi `product` kollektsiyasidan mos mahsulotlarni olish uchun quyidagi JSON soʻrovini yuboradi (misol):

```
this.category == 'fizzy'
```

Kirish maydoni zaif boʻlishi mumkinligini tekshirish uchun, `category` parametrining qiymatiga fuzz satr yuboring. MongoDB uchun misol fuzz satri:

```
'"`{
;$Foo}
$Foo \xYZ
```

Ushbu fuzz satrdan foydalanib quyidagi hujumni qurishingiz mumkin:

```
https://insecure-website.com/product/lookup?category='%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00
```

Agar bu soʻrov dastlabki javobdan oʻzgarish keltirib chiqarsa, bu foydalanuvchi kiritishi toʻgʻri filtrlanmagan yoki tozalanmaganligini koʻrsatishi mumkin.

**Eslatma**
NoSQL injeksiyalari turli kontekstlarda yuz berishi mumkin — fuzz satrlaringizni shu kontekstga moslashtirishingiz kerak. Aks holda, siz shunchaki validatsiya xatolarini chaqirib, ilova soʻrovingizni hech qachon bajarilmasligiga olib kelishingiz mumkin.

Bu misolda biz fuzz satrni URL orqali in'ektsiya qilayapmiz, shuning uchun satr URL-kodlangan. Baʼzi ilovalarda payloadni JSON xossasi (property) orqali yuborish kerak boʻladi. Shu holatda payload quyidagicha koʻrinishga ega boʻladi: `'"`{\r;\$Foo}\n\$Foo \xYZ\u0000\`.

#### Qaysi belgilar qay tarzda qayta ishlanishini aniqlash

Qaysi belgilar ilova tomonidan sintaksis sifatida talqin qilinishini aniqlash uchun yakka belgilarni in'ektsiya qilishingiz mumkin. Masalan, `'` belgisi yuborilganda quyidagi MongoDB soʻrovi hosil boʻlishi mumkin:

```
this.category == '''
```

Agar bu dastlabki javobdan oʻzgarish keltirib chiqarsa, demak `'` belgisi soʻrov sintaksisini buzib, sintaksis xatosiga olib kelgan boʻlishi mumkin. Buni iqtibosni qochirish (escaping) orqali ham tekshirishingiz mumkin, masalan:

```
this.category == '\''
```

Agar bu sintaksis xatosiga olib kelmasa, ilova injection hujumiga moyil boʻlishi mumkinligini koʻrsatadi.

#### Shartli xulqni (conditional behavior) tasdiqlash

Zaiflik aniqlangach, keyingi qadam — NoSQL sintaksisi orqali boolean shartlarga taʼsir oʻtkaza olish-olmasligingizni aniqlash.

Buni tekshirish uchun ikki xil soʻrov yuboring — biri notoʻgʻri (false) shart bilan, biri toʻgʻri (true) shart bilan. Masalan, quyidagi shartlardan foydalanishingiz mumkin: `' && 0 && 'x` va `' && 1 && 'x`, shu tarzda:

```
https://insecure-website.com/product/lookup?category=fizzy'+%26%26+0+%26%26+'x
https://insecure-website.com/product/lookup?category=fizzy'+%26%26+1+%26%26+'x
```

Agar ilova turlicha xulq qilsa, demak `false` shart soʻrov mantiqiga taʼsir koʻrsatmoqda, `true` shart esa yoʻq. Bu turdagi sintaksis in'ektsiyasi server tomonidagi soʻrovga taʼsir qilayotganligini bildiradi.

#### Mavjud shartlarni bekor qilish (overriding existing conditions)

Boolean shartlarga taʼsir oʻtkaza olishni aniqlaganingizdan soʻng, mavjud shartlarni bekor qilib ekspluatatsiya qilishga urinib koʻrishingiz mumkin. Masalan, har doim `true` boʻladigan JavaScript shartini in'ektsiya qilish: `'||'1'=='1`:

```
https://insecure-website.com/product/lookup?category=fizzy%27%7c%7c%27%31%27%3d%3d%27%31
```

Bu quyidagi MongoDB soʻroviga olib keladi:

```
this.category == 'fizzy'||'1'=='1'
```

Kiritilgan shart har doim `true` boʻlgani uchun, oʻzgartirilgan soʻrov barcha elementlarni qaytaradi. Bu sizga har qanday kategoriyadagi (hatto yashirin yoki nomaʼlum) barcha mahsulotlarni koʻrish imkonini beradi.

**Ogohlantirish**
Har doim `true` boʻladigan shartni NoSQL soʻroviga in'ektsiya qilishda ehtiyot boʻling. Dastlabki kontekstda bu zararli boʻlmasligi mumkin, lekin ko‘pincha ilovalar bitta soʻrovdan olingan maʼlumotni bir nechta joyda qayta ishlaydi. Masalan, agar shu maʼlumot `update` yoki `delete` soʻrovlarida ishlatilsa, bu maʼlumot yoʻqolishiga yoki boshqa noxush oqibatlarga olib kelishi mumkin.

Siz shuningdek `category` qiymatidan soʻng null belgisi (`\u0000`) qoʻshishingiz mumkin. MongoDB null belgidan keyingi barcha belgilarni eʼtiborsiz qoldirishi mumkin. Bu esa qoʻshimcha shartlarni bekor qiladi. Masalan, soʻrovda qoʻshimcha `this.released` cheklovi mavjud boʻlishi mumkin:

```
this.category == 'fizzy' && this.released == 1
```

`this.released == 1` faqat chiqarilgan mahsulotlarni koʻrsatish uchun ishlatiladi. Chiqarilmagan mahsulotlar uchun `this.released == 0` boʻlishi mumkin.

Bu holatda xujumchi quyidagi tarzda hujum qurishi mumkin:

```
https://insecure-website.com/product/lookup?category=fizzy'%00
```

Bu quyidagi NoSQL soʻroviga aylanadi:

```
this.category == 'fizzy'\u0000' && this.released == 1
```

Agar MongoDB null belgidan keyingi barcha belgilarni eʼtiborsiz qoldirsa, bu `released == 1` talabini olib tashlaydi. Natijada `fizzy` kategoriyasidagi barcha mahsulotlar, jumladan chiqarilmagan mahsulotlar ham, koʻrinadi.
