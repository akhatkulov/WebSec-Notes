Clickjacking nima?
Clickjacking — bu foydalanuvchi interfeysiga asoslangan hujum bo‘lib, unda foydalanuvchi aldov orqali yashirin sayt tarkibidagi amalga oshiriladigan elementni (masalan, tugma yoki havola) bosishga majbur qilinadi, lekin u o‘zi ko‘rayotgan kontentni bosayotganini o‘ylaydi. Quyidagi misolga e’tibor bering:

Veb foydalanuvchi aldov sayti (masalan, elektron pochta orqali yuborilgan havola)ga kiradi va mukofot yutish uchun tugmani bosadi. Foydalanuvchi bunga bexabar holda hujumchi tomonidan boshqa yashirin tugmani bosishga chalg‘itiladi va bu boshqa saytda hisobdan to‘lov qilinishiga olib keladi. Bu clickjacking hujumining bir misolidir.

Ushbu texnika yashirin, amalga oshiriladigan veb sahifa (yoki bir nechta sahifa)ni `iframe` ichida joylashtirishga asoslanadi. Ushbu `iframe` foydalanuvchi kutgan aldov sayti kontenti ustiga joylashtiriladi. Clickjacking hujumi CSRF hujumidan farq qiladi: foydalanuvchi tugmani bosish kabi harakatni bajarishi talab qilinadi, CSRF esa foydalanuvchining xabari yoki roziligisiz butun so‘rovni soxtalashtirishga asoslangan.

CSRF hujumlaridan himoyalanish ko‘pincha CSRF tokeni orqali ta’minlanadi: bu sessiyaga xos, bir martalik raqam yoki nonce hisoblanadi. Clickjacking hujumlari CSRF tokenlari bilan oldini olish mumkin emas, chunki hujum maqsadli sessiya haqiqiy sayt kontenti bilan o‘rnatiladi va barcha so‘rovlar domen ichida sodir bo‘ladi. CSRF tokenlari so‘rovlarga joylashtiriladi va serverga normal sessiya doirasida yuboriladi. Farq shundaki, bu jarayon yashirin `iframe` ichida amalga oshiriladi.

---

**Clickjacking hujumini qanday yaratish mumkin**
Clickjacking hujumlari CSS yordamida qatlamlarni yaratish va boshqarishga tayanadi. Hujumchi maqsadli saytni `iframe` qatlamida aldov sayti ustiga joylashtiradi. Quyida style teg va parametrlar yordamida oddiy misol keltirilgan:

```html
<head>
	<style>
		#target_website {
			position: relative;
			width: 128px;
			height: 128px;
			opacity: 0.00001;
			z-index: 2;
		}
		#decoy_website {
			position: absolute;
			width: 300px;
			height: 400px;
			z-index: 1;
		}
	</style>
</head>
<body>
	<div id="decoy_website">
	...aldov saytining kontenti shu yerda...
	</div>
	<iframe id="target_website" src="https://vulnerable-website.com">
	</iframe>
</body>
```

Maqsadli sayt `iframe` ichida shunday joylashtiriladiki, foydalanuvchi aldov saytidagi kontentni ko‘rib turgan joy bilan aniq moslashadi. Buning uchun kerakli kenglik va balandlik qiymatlari aniqlanadi. `Absolute` va `relative` pozitsiyalar foydalanuvchi ekran o‘lchami, brauzer turi va platformaga qaramay to‘g‘ri joylashuvni ta’minlaydi.

`z-index` esa qatlamlarning ustma-ust joylashuv tartibini belgilaydi. `Opacity` qiymati 0.0 (yoki deyarli 0.0) qilib belgilanishi kerak, shunda `iframe` tarkibi foydalanuvchiga ko‘rinmaydi. Ba’zi brauzerlar clickjackingdan himoya qilish uchun `iframe` shaffofligini aniqlash mexanizmlarini ishlatadi (masalan, Chrome 76 versiyasida mavjud, Firefox esa buni qilmaydi). Hujumchi `opacity` qiymatini shunday tanlaydiki, kerakli effekt yuzaga kelsa va himoya mexanizmlari ishga tushmasin.

