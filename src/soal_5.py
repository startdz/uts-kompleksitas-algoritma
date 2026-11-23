
# Membuat data mahasiswa secara otomatis
def buat_data(jumlah):
    data = []

    for i in range(1, jumlah + 1):
        data.append({
            "nim": str(2301000 + i),
            "nama": f"Mahasiswa {i}"
        })

    return data


# SEBELUM PERBAIKAN
# Linear Search Biasa
def linear_search(data, target):
    i = 0
    cek_indeks = 0
    cek_nim = 0

    while True:
        cek_indeks += 1

        if i >= len(data):
            break

        cek_nim += 1

        if data[i]["nim"] == target:
            return data[i], cek_indeks, cek_nim

        i += 1

    return None, cek_indeks, cek_nim


# SESUDAH PERBAIKAN
# Linear Search Sentinel
def sentinel_search(data, target):
    n = len(data)

    # Menambahkan elemen penjaga
    data.append({
        "nim": target,
        "nama": "Sentinel"
    })

    i = 0
    cek_nim = 0

    # Tidak perlu memeriksa batas indeks setiap iterasi
    while True:
        cek_nim += 1

        if data[i]["nim"] == target:
            break

        i += 1

    # Menghapus elemen penjaga
    data.pop()

    # Memastikan data ditemukan pada data asli
    cek_indeks = 1

    if i < n:
        return data[i], cek_indeks, cek_nim

    return None, cek_indeks, cek_nim


# Pengujian 10, 50, dan 100 data
jumlah_data = [10, 50, 100]

print("=" * 65)
print("PENGUJIAN LINEAR SEARCH SEBELUM DAN SESUDAH PERBAIKAN")
print("=" * 65)

print(
    f"{'Data':<10}"
    f"{'Biasa':<15}"
    f"{'Sentinel':<15}"
    f"{'Pengurangan':<15}"
)

for jumlah in jumlah_data:
    data = buat_data(jumlah)

    # Target adalah NIM mahasiswa terakhir
    target = data[-1]["nim"]

    # Sebelum perbaikan
    hasil1, indeks1, nim1 = linear_search(data, target)
    langkah1 = indeks1 + nim1

    # Sesudah perbaikan
    hasil2, indeks2, nim2 = sentinel_search(data, target)
    langkah2 = indeks2 + nim2

    pengurangan = langkah1 - langkah2

    print(
        f"{jumlah:<10}"
        f"{langkah1:<15}"
        f"{langkah2:<15}"
        f"{pengurangan:<15}"
    )

    # Memastikan hasil kedua algoritma sama
    assert hasil1["nim"] == hasil2["nim"]

print("=" * 65)
print("Pengujian selesai.")
