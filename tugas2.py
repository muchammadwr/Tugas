# Tugas 05: Studi Kasus Perbandingan (soal latihan 5.3 di halaman 55)
def hitung_harga(harga, jumlah):
    total = harga * jumlah
    if total > 1500000:
        diskon = total * 0.1
        harga_setelah_diskon = total - diskon
        return harga_setelah_diskon
    else:
        return total


harga = float(input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah barang: "))

harga_total = hitung_harga(harga, jumlah)
print("Total harga yang harus dibayar: Rp", harga_total)
