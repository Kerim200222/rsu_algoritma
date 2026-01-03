# Linear Congruential Generator (LCG) - RSÜ Projesi

Bu proje, Python kullanılarak yazılmış basit bir Sözde Rastgele Sayı Üreteci (Pseudo-Random Number Generator) uygulamasıdır.

## Algoritma Hakkında
Projede **Linear Congruential Generator (LCG)** algoritması kullanılmıştır. Bu algoritma şu formüle dayanır:

$$X_{n+1} = (a \cdot X_n + c) \mod m$$

### Parametreler:
- **Modulus (m):** $2^{32}$
- **Multiplier (a):** 1664525
- **Increment (c):** 1013904223

## Nasıl Çalıştırılır?
Kodu çalıştırmak için terminalde şu komutu yazmanız yeterlidir:
`python rsu_algoritma.py`

Bu kod, 0 ile 100 arasında 5 adet rastgele sayı üretecektir.
