
from collections import deque

# Membuat Queue antrean pembeli
antrean = deque()

# Data awal 10 pembeli
daftar_pembeli = [
    "Andi",
    "Budi",
    "Citra",
    "Dimas",
    "Eka",
    "Fajar",
    "Gita",
    "Hendra",
    "Intan",
    "Joko"
]

# Menambahkan 10 pembeli ke antrean
for nama in daftar_pembeli:
    antrean.append(nama)


# Fungsi menambahkan pembeli (Enqueue)
def tambah_pembeli():
    nama = input("Masukkan nama pembeli: ")

    if nama.strip() == "":
        print("Nama pembeli tidak boleh kosong!")
        return

    antrean.append(nama)
    print(f"{nama} berhasil ditambahkan ke antrean.")


# Fungsi melayani pembeli (Dequeue)
def layani_pembeli():
    if len(antrean) == 0:
        print("Antrean kosong, tidak ada pembeli!")
    else:
        pembeli = antrean.popleft()
        print(f"Pembeli atas nama {pembeli} sedang dilayani.")


# Fungsi menampilkan antrean (Display)
def tampilkan_antrean():
    if len(antrean) == 0:
        print("Antrean masih kosong.")
    else:
        print("\n=== DAFTAR ANTREAN PEMBELI ===")

        for nomor, nama in enumerate(antrean, start=1):
            print(f"{nomor}. {nama}")

        print(f"Total pembeli dalam antrean: {len(antrean)}")


# Program utama
while True:
    print("\n===== SIMULASI ANTREAN KANTIN =====")
    print("1. Tambah Pembeli")
    print("2. Layani Pembeli Berikutnya")
    print("3. Tampilkan Antrean")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        tambah_pembeli()

    elif pilihan == "2":
        layani_pembeli()

    elif pilihan == "3":
        tampilkan_antrean()

    elif pilihan == "4":
        print("Program antrean kantin selesai.")
        break

    else:
        print("Pilihan tidak valid!")
