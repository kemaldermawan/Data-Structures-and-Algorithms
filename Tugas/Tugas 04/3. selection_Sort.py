import shlex

def validasi(data_input):
    data = []
    tokens = shlex.split(data_input)
    for token in tokens:
        parts = [p.strip() for p in token.split(',') if p.strip()]
        data.extend(parts)

    hasil = []
    for elemen in data:
        try:
            if '.' in elemen or 'e' in elemen.lower():
                hasil.append(float(elemen))
            else:
                hasil.append(int(elemen))
        except ValueError:
            hasil.append(elemen)
    return hasil

def selection(data, jenis):
    for i in range(len(data)):
        index = i
        print(f"\niterasi ke {i + 1}:")
        for j in range(i + 1, len(data)):
            print(f"  Bandingkan {data[j]} dengan {data[index]}")
            if jenis == 1:  # Naik
                if isinstance(data[j], (int, float)) and isinstance(data[index], (int, float)):
                    if data[j] < data[index]:
                        index = j
                elif isinstance(data[j], str) and isinstance(data[index], str):
                    if data[j].lower() < data[index].lower():
                        index = j
                elif isinstance(data[j], (int, float)) and isinstance(data[index], str):
                    index = j
            elif jenis == 2:  # Turun
                if isinstance(data[j], (int, float)) and isinstance(data[index], (int, float)):
                    if data[j] > data[index]:
                        index = j
                elif isinstance(data[j], str) and isinstance(data[index], str):
                    if data[j].lower() > data[index].lower():
                        index = j
                elif isinstance(data[j], str) and isinstance(data[index], (int, float)):
                    index = j
        if index != i:
            nilai = data[index]
            for k in range(index, i, -1):
                data[k] = data[k - 1]
            data[i] = nilai
            print(f"  Geser elemen dan tempatkan {nilai} di posisi {i}")
        print(f"  Data setelah iterasi {i + 1}: {data}")
        print("-" * 50)
    return data

data = []

while True:
    if not data:
        masukan = input("Masukkan data awal (pisahkan dengan koma): ")
        data = validasi(masukan)

    print("\nMenu:")
    print("1. Urutkan data (Ascending)")
    print("2. Urutkan data (Descending)")
    print("3. Tambah data")
    print("4. Keluar")
    pilihan = input("Masukkan pilihan: ").strip()

    if pilihan in ('1', '2'):
        jenis = int(pilihan)
        print("\nData sebelum diurutkan:", data)
        selection(data, jenis)
        if jenis == 1:
            print("Data setelah diurutkan naik:", data)
        else:
            print("Data setelah diurutkan turun:", data)

    elif pilihan == '3':
        tambahan = input("Masukkan data tambahan (pisahkan dengan koma): ")
        data_baru = validasi(tambahan)
        data.extend(data_baru)
        print("Data berhasil ditambahkan.")
        print("Data saat ini:", data)

    elif pilihan == '4':
        ulang = input("Apakah Anda ingin mengulang program dari awal? (ya/tidak): ").strip().lower()
        if ulang == 'ya':
            data = []
            continue
        elif ulang == 'tidak':
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Program akan berakhir.")
            break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")