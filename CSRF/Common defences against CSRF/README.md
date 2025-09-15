CSRF ga qarshi umumiy himoyalar

Hozirgi vaqtda CSRF zaifliklarini topish va ekspluatatsiya qilish ko‘pincha nishon veb-sayti yoki qurbonning brauzeri tomonidan joriy etilgan anti-CSRF choralari atrofidan aylanib o‘tishni talab qiladi. Eng ko‘p uchraydigan himoya usullari quyidagilardir:

CSRF tokenlari — CSRF tokeni server tomonida yaratiladigan, noyob, sirli va oldindan taxmin qilib bo‘lmaydigan qiymatdir va mijoz (brauzer) bilan bo‘lishiladi. Maxfiy harakatni (masalan, forma yuborishni) bajarishda mijoz so‘rovga to‘g‘ri CSRF tokenini qo‘shishi kerak. Bu hujumchiga qurbon nomidan haqiqiy so‘rovni yaratishni juda qiyinlashtiradi.

SameSite cookie sozlamalari — SameSite brauzer xavfsizligi mexanizmi bo‘lib, boshqa saytlardan kelayotgan so‘rovlarda sayt cookie’larining qachon yuborilishini belgilaydi. Maxfiy amallarni bajarish uchun odatda autentifikatsiyalangan sessiya cookie’si kerak bo‘ladi, shuning uchun tegishli SameSite cheklovlari hujumchining bu amallarni cross-site tarzda ishga tushirishini to‘sib qo‘yishi mumkin. 2021 yildan beri Chrome sukut bo‘yicha Lax SameSite cheklovlarini majburiy qiladi. Bu taklif qilingan standart bo‘lgani uchun, boshqa yirik brauzerlar ham kelajakda shu xulq-atvorni qabul qilishi kutiladi.

Referer-ga asoslangan tekshiruv — Ba’zi ilovalar CSRF hujumlariga qarshi kurashish uchun HTTP Referer sarlavhasidan foydalanadi, odatda so‘rovning ilovaning o‘z domenidan kelganligini tekshirish orqali. Bu odatda CSRF tokenlar bilan tekshiruv qilinishidan kamroq samarali hisoblanadi.
