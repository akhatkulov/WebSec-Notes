**Turli kontekstlarda SQL injeksiya**

Oldingi laboratoriyalarda siz SQL injeksiya hujumini amalga oshirish uchun so‘rov satridan (query string) foyg‘landingiz. Biroq, SQL injeksiyalarni ilova SQL so‘rovida ishlov beradigan **istalgan boshqariladigan input** orqali amalga oshirish mumkin. Masalan, ayrim veb-saytlar ma’lumotlarni JSON yoki XML formatida qabul qiladi va shu orqali ma’lumotlar bazasiga so‘rov yuboradi.

Bu turli formatlar sizga WAF yoki boshqa himoya mexanizmlari tufayli bloklanadigan hujumlarni yashirish (obfuscate) imkoniyatini berishi mumkin. Zaif implementatsiyalarda ko‘pincha so‘rovda SQL injeksiya uchun keng tarqalgan kalit so‘zlar qidiriladi. Shu sababli, bunday filtrlardan qochish uchun siz taqiqlangan kalit so‘zlarni **kodlash** yoki **escape qilish** orqali o‘zgartirib yuborishingiz mumkin.

Masalan, quyidagi **XML asosidagi SQL injeksiya** SELECT so‘zidagi `S` harfini XML escape-ketma-ketligi orqali kodlaydi:

```xml
<stockCheck>
    <productId>123</productId>
    <storeId>999 &#x53;ELECT * FROM information_schema.tables</storeId>
</stockCheck>
```

Bu qiymat server tomonda **dekodlanadi** va SQL interpreter’ga yuborilishidan oldin asl SELECT so‘ziga qaytariladi.

