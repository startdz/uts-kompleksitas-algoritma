
# Data transaksi belanja
transaksi = [
    {"barang": "Beras 5 kg", "harga": 75000},
    {"barang": "Minyak Goreng", "harga": 18000},
    {"barang": "Gula Pasir", "harga": 16000},
    {"barang": "Telur 1 kg", "harga": 28000},
    {"barang": "Mie Instan", "harga": 3500},
    {"barang": "Susu UHT", "harga": 12000},
    {"barang": "Roti Tawar", "harga": 15000},
    {"barang": "Kopi", "harga": 10000},
    {"barang": "Teh Celup", "harga": 8000},
    {"barang": "Sabun Mandi", "harga": 5000}
]


# Pendekatan Iteratif
def total_iteratif(data):
    total = 0
    langkah = 0

    for item in data:
        total += item["harga"]
        langkah += 1

    return total, langkah


# Pendekatan Rekursif
def total_rekursif(data, index=0):
    if index >= len(data):
        return 0, 0

    nilai, langkah = total_rekursif(data, index + 1)

    return data[index]["harga"] + nilai, langkah + 1


# Menampilkan data transaksi
print("===== DAFTAR TRANSAKSI BELANJA =====")

for nomor, item in enumerate(transaksi, start=1):
    print(
        f"{nomor}. {item['barang']} "
        f"- Rp{item['harga']:,}".replace(",", ".")
    )


# Menghitung total menggunakan kedua pendekatan
hasil_iteratif, langkah_iteratif = total_iteratif(transaksi)

hasil_rekursif, langkah_rekursif = total_rekursif(transaksi)


# Menampilkan hasil
print("\n===== HASIL PERHITUNGAN =====")

print(f"Total Iteratif  : Rp{hasil_iteratif:,}".replace(",", "."))
print(f"Total Rekursif  : Rp{hasil_rekursif:,}".replace(",", "."))

print("\n===== PERBANDINGAN =====")

print(f"Langkah Iteratif : {langkah_iteratif}")
print(f"Langkah Rekursif : {langkah_rekursif}")

if hasil_iteratif == hasil_rekursif:
    print("Kesimpulan: Kedua pendekatan menghasilkan total yang sama.")
else:
    print("Kesimpulan: Hasil perhitungan berbeda!")
