Yashirin ko‘p bosqichli ketma-ketliklar
Amalda bitta so‘rov ortiqcha bosqichlarni (sub-holatlarni) ishga tushirib, ilovani bir nechta yashirin holatlarga o‘tkazishi va so‘rov qayta ishlanishi tugamaguncha ularni tark etishi mumkin. Biz bularni «sub-holatlar» deb ataymiz.

Agar bir nechta HTTP so‘rovlarini aniqlay olsangiz va ular bir xil ma’lumot bilan o‘zaro ta’sir qilayotganini ko‘rsangiz, siz ushbu sub-holatlarni suiiste’mol qilib, ko‘p bosqichli ish jarayonlarida uchraydigan va vaqtga bog‘liq mantiqiy xatoliklarning yangi turini ochishingiz mumkin. Bu cheklovlarni buzishdan (limit overrun) ancha kengroq vaziyatlarda race condition (vaqtlash zaifligi) exploiti imkonini beradi.

Masalan, siz ko‘p omilli autentifikatsiya (MFA / 2FA) ish jarayonidagi xatoliklarni bilishingiz mumkin: avval foydalanuvchi ma’lumotlari bilan birinchi qismga kirib, keyin majburiy sahifaga (forced browsing) o‘tgach, MFAni butunlay aylanib o‘tish imkoniyati paydo bo‘ladi.

Eslatma
Agar bu ekspluatatsiya bilan tanish bo‘lmasangiz, Authentication vulnerabilities (Autentifikatsiya zaifliklari) mavzusidagi «2FA simple bypass» laboratoriya mashqini ko‘rib chiqing.

Quyidagi pseudo-kod veb-sayt qanday qilib bunday race-variatsiyaga moyil bo‘lishi mumkinligini ko‘rsatadi:

```python
session['userid'] = user.userid
if user.mfa_enabled:
    session['enforce_mfa'] = True
    # foydalanuvchiga MFA kodini yaratish va yuborish
    # brauzerni MFA kodi kiritish formasi tomon yo'naltirish
```

Ko‘rib turganingizdek, bu haqiqatan ham bitta so‘rov doirasida yuz beradigan ko‘p bosqichli ketma-ketlikdir. Eng muhimi — bu vaqtinchalik seans foydalanuvchiga haqiqiy kirish huquqini beradi, ammo MFA hali majburiy emasligi holatidir. Hujumchi login so‘rovi bilan birga himoyalangan, autentifikatsiyani talab qiladigan endpointga so‘rov yuborish orqali buni suiiste’mol qilishi mumkin.

Keyingi qismda biz yana bir nechta yashirin ko‘p bosqichli ketma-ketlik misollarini ko‘ramiz va siz bularni interaktiv laboratoriyalarda ekspluatatsiya qilishni mashq qilasiz. Biroq, bunday zaifliklar juda saytga xos bo‘lishi sababli, birinchi navbatda ularni samarali aniqlash uchun kengroq metodologiyani tushunishingiz muhim — ham laboratoriyalarda, ham real dunyoda.
