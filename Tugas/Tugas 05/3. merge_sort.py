def merge(data, ascending=True, level=0):
    if len(data) > 1:
        tengah = len(data) // 2
        kiri, kanan = data[:tengah], data[tengah:]

        indent = '  ' * level
        kiri_str = [x[1] for x in kiri]
        kanan_str = [x[1] for x in kanan]
        data_str = [x[1] for x in data]
        print(f"{indent}Memecah: {data_str} -> {kiri_str} | {kanan_str}")

        merge(kiri, ascending, level + 1)
        merge(kanan, ascending, level + 1)

        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if (kiri[i][0] < kanan[j][0] and ascending) or (kiri[i][0] > kanan[j][0] and not ascending):
                data[k] = kiri[i]
                i += 1
            else:
                data[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            data[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            data[k] = kanan[j]
            j += 1
            k += 1

        gabung_str = [x[1] for x in data]
        print(f"{indent}Menggabung: {kiri_str} + {kanan_str} -> {gabung_str}")
    return data

def parse_input(input_str):
    hasil = []
    for nilai in input_str.split():
        try:
            if '/' in nilai:
                pembilang, penyebut = nilai.split('/')
                nilai_float = float(pembilang) / float(penyebut)
            else:
                nilai_float = float(nilai)
            hasil.append((nilai_float, nilai))
        except:
            print(f"'{nilai}' tidak valid dan dilewati.")
    return hasil

def main():
    ulang = 'ya'
    while ulang == 'ya':
        masukan = input("Masukkan data (pisahkan dengan spasi): ").strip()
        data = parse_input(masukan)

        if not data:
            print("Tidak ada data valid. Coba lagi.\n")
            continue

        while True:
            print("\n=== Menu ===")
            print("1. Ascending")
            print("2. Descending")
            print("3. Tambah Data")
            print("4. Keluar")
            pilihan = input("Pilih menu (1-4): ").strip()

            if pilihan == '1':
                print("\nSebelum diurutkan:", [x[1] for x in data])
                hasil = merge(data[:], ascending=True)
                print("Setelah diurutkan (Ascending):", [x[1] for x in hasil])
            elif pilihan == '2':
                print("\nSebelum diurutkan:", [x[1] for x in data])
                hasil = merge(data[:], ascending=False)
                print("Setelah diurutkan (Descending):", [x[1] for x in hasil])
            elif pilihan == '3':
                tambahan = input("Masukkan data tambahan (contoh: 3 1/4 0.25): ").strip()
                tambahan_data = parse_input(tambahan)
                data.extend(tambahan_data)
                print("Data sekarang:", [x[1] for x in data])
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid. Silakan pilih 1-4.")

        ulang = input("\nIngin mengulang program dari awal? (ya/tidak): ").strip().lower()
    print("\nTerima kasih! Program selesai.")

main()