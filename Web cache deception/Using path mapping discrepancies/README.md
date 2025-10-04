# Yo‘l xaritalashdagi (path mapping) tafovutlar — oʻzbekcha tarjima

**URL path mapping** — URL yo‘llarini serverdagi resurslarga (fayllar, skriptlar yoki buyruq bajarishlar kabi) bog‘lash jarayonidir. Turli ramkalar va texnologiyalar turli xil xaritalash uslublaridan foydalanadi. Eng ko‘p uchraydigan ikkita uslub — anʼanaviy (traditional) URL xaritalash va REST uslubidagi URL xaritalash.

**Anʼanaviy URL xaritalash** fayl tizimidagi resursga to‘g‘ridan-to‘g‘ri yo‘lni bildiradi. Masalan:

`http://example.com/path/in/filesystem/resource.html`

* `http://example.com` — serverga yo‘naltirilgan domen.
* `/path/in/filesystem/` — server fayl tizimidagi papka yo‘li.
* `resource.html` — so‘ralayotgan aniq fayl.

**REST uslubidagi URL** esa jismoniy fayl tuzilmasiga to‘g‘ri kelmasligi mumkin. U API ning mantiqiy qismlarini ifodalaydi:

`http://example.com/path/resource/param1/param2`

* `http://example.com` — server.
* `/path/resource/` — resursni ifodalovchi endpoint.
* `param1` va `param2` — server so‘rovni qayta ishlash uchun ishlatadigan yo‘l parametrlar.

Kesh (cache) va origin server URL yo‘lini resurslarga qanday bog‘lashdagi tafovutlar veb-kesh aldov (web cache deception) zaifliklariga olib kelishi mumkin. Quyidagi misolga eʼtibor bering:

`http://example.com/user/123/profile/wcd.css`

* REST uslubidagi origin server buni `/user/123/profile` endpointi uchun so‘rov deb tushunishi va `wcd.css` ni ahamiyatsiz qo‘shimcha sifatida eʼtiborsiz qoldirishi mumkin — natijada foydalanuvchi 123 ning profil maʼlumotlari qaytadi.
* Anʼanaviy URL xaritalashga ega bo‘lgan kesh esa buni `/user/123/profile/wcd.css` yo‘li ostidagi `wcd.css` fayli uchun so‘rov deb qabul qilishi mumkin. Agar kesh `.css` bilan tugaydigan yo‘llar uchun javoblarni saqlashga sozlangan bo‘lsa, u profildan olingan dinamik maʼlumotni CSS fayli sifatida keshlab, keyinchalik shu URL orqali yana boshqa foydalanuvchilarga xizmat qilishi mumkin.

## Yo‘l xaritalashdagi tafovutlardan foydalanish (eksploitatsiya)

Origin server URL yo‘lini resurslarga qanday bog‘lashini sinash uchun, maqsadli endpoint URL ga ixtiyoriy bir yo‘l segmentini qo‘shib ko‘ring. Agar javob asosiy (base) javob bilan bir xil sezgir maʼlumotni qaytarishda davom etsa, bu origin serverning URL yo‘lini abstraktlashtirib, qo‘shilgan segmentni eʼtiborsiz qoldirayotganidan dalolat beradi. Masalan, `/api/orders/123` ni `/api/orders/123/foo` ga o‘zgartirish ham buyurtma maʼlumotlarini qaytarsa — origin URL segmentini oddiy parametr deb qabul qilmoqda.

Keshning URL yo‘lini qanday xaritalashini sinash uchun, yo‘lni o‘zgartirib va statik kengaytma (extension) qo‘shib, kesh qoidasi bilan moslashtirishga harakat qiling. Masalan, `/api/orders/123/foo` ni `/api/orders/123/foo.js` ga o‘zgartiring. Agar bu javob keshlansa, bu quyidagilarga ishora qiladi:

* Kesh to‘liq URL yo‘lini statik kengaytma bilan birgalikda talqin qiladi.
* `.js` bilan tugaydigan so‘rovlarga javoblarni saqlash uchun kesh qoidasi mavjud.

Keshlar baʼzan maʼlum statik kengaytmalar asosida qoidalar o‘rnatadi. Sinov uchun turli kengaytmalarni tekshiring: `.css`, `.ico`, `.exe` va boshqalar.

Keyin siz dinamik javobni qaytaradigan va keshga yoziladigan zararli URL yaratishingiz mumkin. Eʼtibor bering: bu hujum faqat siz sinagan aniq endpointga nisbatan ishlashi mumkin, chunki origin server har bir endpoint uchun turlicha abstraktsiya qoidalariga ega bo‘lishi ehtimoli katta.

**Eslatma**
Burp Scanner path mapping tafovutlari tufayli yuzaga keladigan web cache deception zaifliklarini audit paytida avtomatik aniqlaydi. Shuningdek, Web Cache Deception Scanner BApp kengaytmasidan ham noto‘g‘ri sozlangan veb-keshlarni aniqlash uchun foydalanish mumkin.
