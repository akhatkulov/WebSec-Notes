SSRF nima?
Server-side request forgery (SSRF) — bu veb-xavfsizlikdagi zaiflik bo‘lib, u hujumchiga server tomondagi dastur orqali kutilmagan joylarga so‘rov yuborishga imkon beradi.

Oddiy SSRF hujumida hujumchi serverni tashkilot infratuzilmasidagi faqat ichki foydalanish uchun mo‘ljallangan xizmatlarga ulanishga majbur qilishi mumkin. Boshqa hollarda esa hujumchi serverni tashqi tizimlarga ulanishga majburlashi mumkin. Bu esa avtorizatsiya ma’lumotlari kabi maxfiy ma’lumotlarning oshkor bo‘lishiga olib kelishi ehtimoli bor.

SSRF hujumlari — serverga qarshi
Serverga qarshi SSRF hujumida hujumchi ilovani o‘zi joylashgan serverga, uning loopback tarmoq interfeysi orqali HTTP so‘rovi yuborishga majbur qiladi. Bu odatda hostname sifatida 127.0.0.1 (loopback adapterni ko‘rsatadigan rezerv IP manzili) yoki localhost (shu adapter uchun keng qo‘llaniladigan nom) kabi qiymat berilgan URL taqdim etishni o‘z ichiga oladi.

Masalan, foydalanuvchiga ma’lum do‘konda mahsulot zaxirada bor-yo‘qligini ko‘rsatadigan xarid ilovasini tasavvur qiling. Zaxira ma’lumotini ta’minlash uchun ilova turli back-end REST API-larni so‘raydi. Buni qiladi front-end orqali tegishli back-end API endpoint manzilini URL sifatida berib. Foydalanuvchi mahsulotning zaxira holatini ko‘rganida, ularning brauzeri quyidagi so‘rovni yuboradi:

```
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://stock.weliketoshop.net:8080/product/stock/check%3FproductId%3D6%26storeId%3D1
```

Bu serverni ko‘rsatilgan URL ga so‘rov yuborib, zaxira holatini olib, foydalanuvchiga qaytarishga majbur qiladi.

Ushbu misolda hujumchi so‘rovni o‘zgartirib, serverga mahalliy (local) URL ni ko‘rsatishi mumkin:

```
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://localhost/admin
```

Server `/admin` URL manzilining mazmunini olib, foydalanuvchiga qaytaradi.

Hujumchi aslida `/admin` sahifasiga tashqaridan kira olmaydi, chunki ma’muriy funksiyalar odatda faqat autentifikatsiyadan o‘tgan foydalanuvchilarga ochiq. Bu shuni anglatadiki, oddiy holatda hujumchi hech qanday qiziqarli ma’lumot ko‘rolmaydi. Biroq, agar `/admin` ga yuborilgan so‘rov mahalliy mashinadan (localhost) kelgan bo‘lsa, odatiy kirish nazoratlari aylanib o‘tiladi. Ilova so‘rovni ishonchli manbadan kelgandek qabul qilib, ma’muriy funksiyalarga to‘liq kirish huquqini beradi.

Nega ilovalar bunday yo‘l tutadi va mahalliy mashinadan kelgan so‘rovlarga bevosita ishonadi? Bu turli sabablarga ko‘ra yuzaga kelishi mumkin:

* Kirish nazoratini tekshirish ilova serveri oldida joylashgan boshqa komponentda amalga oshirilgan bo‘lishi mumkin. Serverga qayta ulanilganda, bu tekshiruv aylanib o‘tiladi.
* Favqulodda tiklash (disaster recovery) maqsadida, ilova mahalliy mashinadan kirayotgan foydalanuvchiga autentifikatsiyasiz ma’muriy kirish huquqini berishi mumkin. Bu tizimni tiklash uchun administrator o‘z hisob ma’lumotlarini yo‘qotgan taqdirda foyda beradi. Bu shuni taxmin qiladiki, faqat to‘liq ishonchli foydalanuvchi bevosita serverdan kiradi.
* Ma’muriy interfeys asosiy ilovadan boshqa portda ishlashi va foydalanuvchilar tomonidan bevosita yetib bo‘lmasligi mumkin.

Shu kabi ishonch munosabatlari — ya’ni mahalliy mashinadan kelgan so‘rovlar oddiy so‘rovlardan boshqacha ko‘rib chiqilishi — SSRF zaifligini ko‘pincha **jiddiy xavfga** aylantiradi.

SSRF hujumlari — boshqa back-end tizimlarga qarshi
Ba’zi hollarda ilova serveri foydalanuvchilar tomonidan bevosita yetib bo‘lmaydigan back-end tizimlari bilan aloqada bo‘lishi mumkin. Bu tizimlar ko‘pincha yo‘naltirilmaydigan (non-routable) xususiy IP manzillarga ega bo‘ladi. Back-end tizimlar odatda tarmoq topologiyasi tomonidan himoyalangan, shuning uchun ularning xavfsizlik holati ko‘pincha zaifroq bo‘ladi. Ko‘p hollarda ichki back-end tizimlarda autentifikatsiyasiz har qanday foydalanuvchi tomonidan foydalanilsa bo‘ladigan sezgir funksiyalar mavjud bo‘ladi.

Oldingi misolni davom ettirsak, back-endda `https://192.168.0.68/admin` manzilida ma’muriy interfeys bor deb tasavvur qiling. Hujumchi SSRF zaifligidan foydalanish uchun quyidagi so‘rovni yuborishi va ma’muriy interfeysga kira olishi mumkin:

```
POST /product/stock HTTP/1.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 118

stockApi=http://192.168.0.68/admin
```

