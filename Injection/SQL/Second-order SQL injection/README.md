
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

