# Studi Kasus Permasalahan Sederhana (soal latihan 4.4 di nomor halaman 50 dan 51.)

import cmath


def hitung_determinan(a, b, c):
    return b**2 - 4 * a * c


def cari_akar(a, b, c):
    D = hitung_determinan(a, b, c)
    if D == 0:
        x1 = x2 = -b / (2 * a)
        return x1, x2
    elif D > 0:
        x1 = (-b + cmath.sqrt(D)) / (2 * a)
        x2 = (-b - cmath.sqrt(D)) / (2 * a)
        return x1, x2
    else:
        x1 = (-b + cmath.sqrt(-D) * 1j) / (2 * a)
        x2 = (-b - cmath.sqrt(-D) * 1j) / (2 * a)
        return x1, x2


a = float(input("Masukkan koefisien a: "))
b = float(input("Masukkan koefisien b: "))
c = float(input("Masukkan koefisien c: "))

akar1, akar2 = cari_akar(a, b, c)

print("Akar-akar persamaan kuadrat:")
print("x1 =", akar1)
print("x2 =", akar2)
