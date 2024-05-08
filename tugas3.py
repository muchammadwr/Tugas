def cari_max_min(deret):
    maksimum = max(deret)
    minimum = min(deret)
    return maksimum, minimum

    # Meminta input bilangan dari pengguna
deret_bilangan = input("Masukkan bilangan, pisahkan dengan koma: ")
deret_bilangan = list(map(int, deret_bilangan.split(",")))

# Memanggil fungsi untuk mencari nilai maksimum dan minimum
nilai_maksimum, nilai_minimum = cari_max_min(deret_bilangan)

# Menampilkan hasil
print("Bilangan maksimum =", nilai_maksimum)
print("Bilangan minimum =", nilai_minimum)
