def tampilkan_abjad(data):
    if not data:
        print("Array kosong.")
    else:
        urut = sorted(data, key=lambda x: x.lower())
        print("Isi array (urutan abjad):", " - ".join(urut))

def tampilkan_antrian(data):
    if not data:
        print("Array kosong.")
    else:
        print("Isi array (urutan antrian):", " - ".join(data))

def tambah(data):
    nama = input("Masukkan data yang ingin ditambah: ").strip()
    if not nama:
        print("Input tidak boleh kosong.")
        return
    data.append(nama)
    print(f"'{nama}' ditambahkan.")

def hapus(data):
    if not data:
        print("Tidak ada data untuk dihapus.")
        return
    nama = input("Masukkan data yang ingin dihapus: ").strip()
    if not nama:
        print("Input tidak boleh kosong.")
        return
    if nama in data:
        data.remove(nama)
        print(f"'{nama}' dihapus.")
    else:
        print("Data tidak ditemukan.")

def main():
    daftar = []
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Tampilkan Data Sesuai Abjad")
        print("4. Tampilkan Data Sesuai Antrian")
        print("5. Selesai")
        pilihan = input("Pilih (1-5): ").strip()

        if pilihan == '1':
            tambah(daftar)
        elif pilihan == '2':
            hapus(daftar)
        elif pilihan == '3':
            tampilkan_abjad(daftar)
        elif pilihan == '4':
            tampilkan_antrian(daftar)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")

while True:
    main()
    ulang = input("\nApakah ingin mengulang program? (ya/tidak): ").strip().lower()
    if ulang != 'ya':
        print("Terima kasih! Program selesai.")
        break