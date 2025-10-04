## Yagona endpointdagi (single-endpoint) race condition’lar

Bitta endpointga turli qiymatlar bilan parallel so‘rovlar yuborish ba’zan kuchli race condition’larni yuzaga keltirishi mumkin.

Masalan, foydalanuvchi ID’si va reset token’ini (qayta tiklash tokeni) foydalanuvchining sessiyasida saqlaydigan parol tiklash mexanizmini ko‘rib chiqing.

Bu holatda, bir xil sessiyadan, lekin ikki xil foydalanuvchi nomi bilan parallel ikkita parol tiklash so‘rovi yuborilsa, quyidagi kabi to‘qnashuv (collision) yuzaga kelishi mumkin:

(parol tiklash mexanizmida to‘qnashuv)

Barcha operatsiyalar tugagach oxirgi holatga e’tibor bering:

```
session['reset-user'] = victim
session['reset-token'] = 1234
```

Sessiyada endi victim (maqsad)ning foydalanuvchi ID’si bor, lekin haqiqiy reset token hujumchiga yuborilgan.

**Eslatma**
Ushbu hujum ishlashi uchun, har bir jarayon tomonidan bajarilayotgan turli operatsiyalar aynan to‘g‘ri tartibda sodir bo‘lishi kerak. Kerakli natijaga erishish uchun bir necha urinuv yoki bir oz omad talab etilishi mumkin.

Elektron pochta manzillarini tasdiqlash yoki elektron pochtaga asoslangan boshqa operatsiyalar — yagona endpointdagi race condition’lar uchun odatda yaxshi maqsad hisoblanadi. Chunki elektron pochta ko‘pincha server mijozga HTTP javobini bergandan keyin fon ipida (background thread) yuboriladi, bu esa race condition yuz berish ehtimolini oshiradi.
