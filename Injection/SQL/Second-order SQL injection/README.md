
**Ikkinchi darajali (Second-order) SQL injeksiya**

![](https://raw.githubusercontent.com/akhatkulov/WebSec-Notes/f58775a136e63e0ed47efb896d59f61238f21a1a/Injection/SQL/Second-order%20SQL%20injection/Second-order%20SQL%20injection.svg)

**Birinchi darajali (First-order) SQL injeksiya** shunda sodir bo‘ladi, ilova foydalanuvchi kiritgan ma’lumotni **bevosita HTTP so‘rovdan** olib, uni SQL so‘roviga noto‘g‘ri tarzda qo‘shadi.

**Ikkinchi darajali (Second-order) SQL injeksiya** esa boshqacharoq ishlaydi: ilova foydalanuvchi kiritgan ma’lumotni HTTP so‘rovdan olib, keyinchalik foydalanish uchun **saqlab qo‘yadi**. Bu ko‘pincha ma’lumotlar bazasiga joylashtirish orqali amalga oshiriladi. Saqlash jarayonida hech qanday zaiflik yuzaga kelmasligi mumkin. Lekin keyinchalik boshqa HTTP so‘rovni qayta ishlash vaqtida ilova oldin saqlangan ma’lumotni olib, uni SQL so‘roviga xavfsiz bo‘lmagan tarzda qo‘shadi.

Shu sababli, **ikkinchi darajali SQL injeksiya** ba’zan **saqlangan SQL injeksiya (stored SQL injection)** deb ham ataladi.

---

### Ikkinchi darajali SQL injeksiya qanday sodir bo‘ladi?

Bu holat odatda quyidagicha yuz beradi:

* Dasturchi SQL injeksiyadan xabardor va foydalanuvchi kiritayotgan **dastlabki input** ni bazaga xavfsiz usulda joylashtiradi.
* Keyinchalik shu ma’lumot bazadan olinadi va **ishonchli deb hisoblanadi**, chunki u ilgari xavfsiz tarzda kiritilgan deb o‘ylashadi.
* Shu paytda ma’lumot SQL so‘roviga xavfsiz bo‘lmagan tarzda qo‘shiladi va injeksiya sodir bo‘ladi.

**SQL injeksiyani qanday oldini olish mumkin**

SQL injeksiyaning aksariyat holatlarini **satrlarni qo‘shib yozish (string concatenation)** o‘rniga **parametrlashtirilgan so‘rovlar** (parameterized queries) dan foydalanish orqali oldini olish mumkin. Bu parametrlashtirilgan so‘rovlar yana **"prepared statements"** deb ham ataladi.

---

Quyidagi kod SQL injeksiyaga zaif, chunki foydalanuvchi kiritgan qiymat to‘g‘ridan-to‘g‘ri so‘rov satriga qo‘shilmoqda:

```java
String query = "SELECT * FROM products WHERE category = '"+ input + "'";
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery(query);
```

---

Ushbu kodni foydalanuvchi inputi so‘rov tuzilmasiga aralashmasligi uchun quyidagicha yozish mumkin:

```java
PreparedStatement statement = connection.prepareStatement("SELECT * FROM products WHERE category = ?");
statement.setString(1, input);
ResultSet resultSet = statement.executeQuery();
```

**SQL injeksiyani qanday oldini olish mumkin – Davomi**

Parametrlashtirilgan so‘rovlar (parameterized queries) ni foydalanuvchi inputi **so‘rov ichida faqatgina ma’lumot sifatida qatnashadigan joylarda** ishlatish mumkin. Bunga **WHERE sharti**, **INSERT** yoki **UPDATE** so‘rovlaridagi qiymatlar kiradi.

Lekin parametrlashtirilgan so‘rovlarni foydalanuvchi inputi **jadval nomi, ustun nomi yoki ORDER BY qismi**ga kiritilsa, bunday holatni to‘g‘ri ishlov bera olmaydi. Agar ilova funksionalligi foydalanuvchi kiritgan ma’lumotni shu qismlarga joylashtirishi kerak bo‘lsa, boshqa yondashuvlar qo‘llaniladi, masalan:

* Faqat ruxsat etilgan qiymatlarni **whitelisting** orqali cheklash.
* Kerakli funksionallikni ta’minlash uchun **boshqa mantiqiy usullar**dan foydalanish.

---

Parametrlashtirilgan so‘rov SQL injeksiyadan samarali himoya bo‘lishi uchun **so‘rov ichida ishlatiladigan satr doimiy (hard-coded constant)** bo‘lishi kerak.

U hech qachon istalgan manbadan keladigan o‘zgaruvchi ma’lumotni o‘z ichiga olmasligi lozim.

⚠️ **Xato yondashuv:** Har bir inputni alohida holatda tekshirib, “ishonchli” bo‘lganlarini concatenation orqali so‘rovga qo‘shish. Bu xavfli, chunki:

* Foydalanuvchi ma’lumotining asl kelib chiqishini noto‘g‘ri baholash mumkin.
* Koddagi boshqa o‘zgarishlar “ishonchli” ma’lumotni ham ifloslantirishi (taint) ehtimoli bor.
