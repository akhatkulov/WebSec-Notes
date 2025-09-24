CORS (cross-origin resource sharing) nima?
Cross-origin resource sharing (CORS) — bu brauzer mexanizmi bo‘lib, u berilgan domen tashqarisida joylashgan resurslarga boshqariladigan tarzda murojaat qilish imkonini beradi. U **bir xil manba siyosati**ni (SOP — same-origin policy) kengaytiradi va unga moslashuvchanlik qo‘shadi. Biroq, agar biror veb-saytning CORS siyosati noto‘g‘ri sozlangan yoki noto‘g‘ri joriy qilingan bo‘lsa, bu **xoch-domen hujumlari** uchun imkoniyat yaratishi mumkin. CORS **CSRF (cross-site request forgery)** kabi xoch-manbali hujumlardan himoya mexanizmi emas.

**Bir xil manba siyosati (Same-origin policy)**
Bir xil manba siyosati — bu cheklovchi xoch-manbali (cross-origin) spetsifikatsiya bo‘lib, u veb-saytning manba domenidan tashqaridagi resurslar bilan o‘zaro ishlash imkoniyatini cheklaydi. Ushbu siyosat ko‘p yillar oldin zararli bo‘lishi mumkin bo‘lgan xoch-domen o‘zaro ta’sirlarga, masalan, biror veb-saytning boshqasidan shaxsiy ma’lumotlarni o‘g‘irlashiga javoban belgilangan. Odatda, u bir domenning boshqa domenlarga so‘rov yuborishiga ruxsat beradi, lekin javoblarni olish imkoniyatini bermaydi.

**Bir xil manba siyosatini yumshatish**
Bir xil manba siyosati juda cheklangan va natijada ushbu cheklovlarni chetlab o‘tish uchun turli yondashuvlar ishlab chiqilgan. Ko‘plab veb-saytlar subdomenlar yoki uchinchi tomon saytlari bilan to‘liq xoch-manbali (cross-origin) kirishni talab qiladigan tarzda o‘zaro aloqada bo‘ladi. Bir xil manba siyosatini nazorat ostida yumshatish **CORS (cross-origin resource sharing)** orqali amalga oshirilishi mumkin.

Cross-origin resource sharing protokoli HTTP sarlavhalari (headers) to‘plamidan foydalanadi. Bu sarlavhalar ishonchli veb-manbalarni va ularga bog‘liq xususiyatlarni, masalan, autentifikatsiya qilingan kirishga ruxsat berilishini belgilaydi. Ular brauzer va u murojaat qilayotgan xoch-manbali veb-sayt o‘rtasida sarlavhalar almashinuvi orqali qo‘llaniladi.
