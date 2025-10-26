def selection(data, jenis):
    for i in range(len(data)):
        index = i
        print(f"\nIterasi ke-{i + 1}:")

        if jenis == 1:
            print(f"  Mencari nilai terkecil dari index {i} hingga {len(data) - 1}")
        elif jenis == 2:
            print(f"  Mencari nilai terbesar dari index {i} hingga {len(data) - 1}")

        for j in range(i + 1, len(data)):
            print(f"  Bandingkan {data[j][1]} dengan {data[index][1]}")
            if jenis == 1:
                if data[j][0] < data[index][0]:
                    index = j
            elif jenis == 2:
                if data[j][0] > data[index][0]:
                    index = j

        if index != i:
            nilai = data[index]
            for k in range(index, i, -1):
                data[k] = data[k - 1]
            data[i] = nilai
            print(f"  Geser elemen dan tempatkan {nilai[1]} di posisi index ke-{i}")

        print(f"  Data setelah iterasi {i + 1}: {[x[1] for x in data]}")
        print("-" * 50)
    return data

data = []
dataAwal = []

while True:
    if not data:
        masukan = input("Masukkan data awal (pisahkan dengan koma): ")
        data = [
            (float(x.split('/')[0]) / float(x.split('/')[1]), x.strip()) if '/' in x else (float(x), x.strip())
            for x in masukan.split(',')
        ]
        dataAwal = data.copy()

    print("\n=== Menu ===")
    print("1. Ascending")
    print("2. Descending")
    print("3. Ascending dan Descending")
    print("4. Tambah data")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan: ").strip()

    if pilihan == '1':
        dataCopy = dataAwal.copy()
        print("\n--- Proses Ascending ---")
        print("\nData sebelum diurutkan:", [x[1] for x in dataCopy])
        selection(dataCopy, 1)
        print("Data setelah diurutkan menaik:", [x[1] for x in dataCopy])

    elif pilihan == '2':
        dataCopy = dataAwal.copy()
        print("\n--- Proses Descending ---")
        print("\nData sebelum diurutkan:", [x[1] for x in dataCopy])
        selection(dataCopy, 2)
        print("Data setelah diurutkan menurun:", [x[1] for x in dataCopy])

    elif pilihan == '3':
        print("\nData sebelum diurutkan:", [x[1] for x in dataAwal])
        asc = dataAwal.copy()
        desc = dataAwal.copy()

        print("\n--- Proses Ascending ---")
        selection(asc, 1)
        print("Data setelah diurutkan menaik:", [x[1] for x in asc])

        print("\nData sebelum diurutkan:", [x[1] for x in dataAwal])

        print("\n--- Proses Descending ---")
        selection(desc, 2)
        print("Data setelah diurutkan menurun:", [x[1] for x in desc])

    elif pilihan == '4':
        tambahan = input("Masukkan data tambahan (pisahkan dengan koma): ")
        tambahan_data = [
            (float(x.split('/')[0]) / float(x.split('/')[1]), x.strip()) if '/' in x else (float(x), x.strip())
            for x in tambahan.split(',')
        ]
        data += tambahan_data
        dataAwal = data.copy()
        print("Data berhasil ditambahkan.")
        print("Data saat ini:", [x[1] for x in data])

    elif pilihan == '5':
        ulang = input("Apakah Anda ingin mengulang program dari awal? (ya/tidak): ").strip().lower()
        if ulang == 'ya':
            data = []
            dataAwal = []
            continue
        elif ulang == 'tidak':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Program akan berakhir.")
            break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")