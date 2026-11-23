
# Data nilai mahasiswa
mahasiswa = [
    {"nim": "2301001", "nama": "Andi", "nilai": 75},
    {"nim": "2301002", "nama": "Budi", "nilai": 85},
    {"nim": "2301003", "nama": "Citra", "nilai": 60},
    {"nim": "2301004", "nama": "Dimas", "nilai": 90},
    {"nim": "2301005", "nama": "Eka", "nilai": 70},
    {"nim": "2301006", "nama": "Fajar", "nilai": 95},
    {"nim": "2301007", "nama": "Gita", "nilai": 80},
    {"nim": "2301008", "nama": "Hendra", "nilai": 65},
    {"nim": "2301009", "nama": "Intan", "nilai": 88},
    {"nim": "2301010", "nama": "Joko", "nilai": 72}
]


# Algoritma Bubble Sort
def bubble_sort(data):
    hasil = data.copy()
    perbandingan = 0
    pertukaran = 0

    n = len(hasil)

    for i in range(n - 1):
        ditukar = False

        for j in range(n - 1 - i):
            perbandingan += 1

            if hasil[j]["nilai"] < hasil[j + 1]["nilai"]:
                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]
                pertukaran += 1
                ditukar = True

        # Berhenti jika tidak ada pertukaran
        if not ditukar:
            break

    return hasil, perbandingan, pertukaran


# Algoritma Selection Sort
def selection_sort(data):
    hasil = data.copy()
    perbandingan = 0
    pertukaran = 0

    n = len(hasil)

    for i in range(n - 1):
        indeks_terbesar = i

        for j in range(i + 1, n):
            perbandingan += 1

            if hasil[j]["nilai"] > hasil[indeks_terbesar]["nilai"]:
                indeks_terbesar = j

        if indeks_terbesar != i:
            hasil[i], hasil[indeks_terbesar] = (
                hasil[indeks_terbesar],
                hasil[i]
            )
            pertukaran += 1

    return hasil, perbandingan, pertukaran


# Menampilkan data awal
print("===== DATA NILAI MAHASISWA =====")

for m in mahasiswa:
    print(f"{m['nama']} - Nilai: {m['nilai']}")


# Proses pengurutan
hasil_bubble, banding_bubble, tukar_bubble = bubble_sort(mahasiswa)

hasil_selection, banding_selection, tukar_selection = selection_sort(mahasiswa)


# Menampilkan hasil Bubble Sort
print("\n===== HASIL BUBBLE SORT =====")

for nomor, m in enumerate(hasil_bubble, start=1):
    print(f"{nomor}. {m['nama']} - Nilai: {m['nilai']}")

print("Jumlah perbandingan:", banding_bubble)
print("Jumlah pertukaran:", tukar_bubble)


# Menampilkan hasil Selection Sort
print("\n===== HASIL SELECTION SORT =====")

for nomor, m in enumerate(hasil_selection, start=1):
    print(f"{nomor}. {m['nama']} - Nilai: {m['nilai']}")

print("Jumlah perbandingan:", banding_selection)
print("Jumlah pertukaran:", tukar_selection)


# Perbandingan hasil
print("\n===== PERBANDINGAN ALGORITMA =====")

if [m["nilai"] for m in hasil_bubble] == [
    m["nilai"] for m in hasil_selection
]:
    print("Kedua algoritma menghasilkan urutan nilai yang sama.")
else:
    print("Hasil pengurutan berbeda.")
