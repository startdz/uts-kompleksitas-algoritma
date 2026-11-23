
# Data mahasiswa
mahasiswa = [
    {"nim": "2301001", "nama": "Andi Saputra"},
    {"nim": "2301002", "nama": "Budi Santoso"},
    {"nim": "2301003", "nama": "Citra Lestari"},
    {"nim": "2301004", "nama": "Dimas Pratama"},
    {"nim": "2301005", "nama": "Eka Putri"},
    {"nim": "2301006", "nama": "Fajar Nugraha"},
    {"nim": "2301007", "nama": "Gita Amelia"},
    {"nim": "2301008", "nama": "Hendra Wijaya"},
    {"nim": "2301009", "nama": "Intan Permata"},
    {"nim": "2301010", "nama": "Joko Susilo"}
]


# Algoritma Linear Search
def linear_search(data, nim):
    langkah = 0

    for i in range(len(data)):
        langkah += 1

        if data[i]["nim"] == nim:
            return data[i], langkah

    return None, langkah


# Algoritma Binary Search
def binary_search(data, nim):
    low = 0
    high = len(data) - 1
    langkah = 0

    while low <= high:
        langkah += 1
        mid = (low + high) // 2

        if data[mid]["nim"] == nim:
            return data[mid], langkah

        elif data[mid]["nim"] < nim:
            low = mid + 1

        else:
            high = mid - 1

    return None, langkah


# Pengujian pencarian
daftar_nim = ["2301001", "2301005", "2301010"]

print("=== HASIL PENCARIAN DATA MAHASISWA ===")

for nim in daftar_nim:
    hasil_linear, langkah_linear = linear_search(
        mahasiswa, nim
    )

    hasil_binary, langkah_binary = binary_search(
        mahasiswa, nim
    )

    print(f"\nNIM yang dicari: {nim}")

    if hasil_linear:
        print("Linear Search :", hasil_linear["nama"])
    else:
        print("Linear Search : Data tidak ditemukan")

    print("Jumlah langkah Linear Search:", langkah_linear)

    if hasil_binary:
        print("Binary Search :", hasil_binary["nama"])
    else:
        print("Binary Search : Data tidak ditemukan")

    print("Jumlah langkah Binary Search:", langkah_binary)
