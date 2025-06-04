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
        print(f"\nProses iterasi {i + 1}:")
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
                    index = j  # Angka lebih dulu
            elif jenis == 2:  # Turun
                if isinstance(data[j], (int, float)) and isinstance(data[index], (int, float)):
                    if data[j] > data[index]:
                        index = j
                elif isinstance(data[j], str) and isinstance(data[index], str):
                    if data[j].lower() > data[index].lower():
                        index = j
                elif isinstance(data[j], str) and isinstance(data[index], (int, float)):
                    index = j  # String lebih dulu
        if index != i:
            nilai = data[index]
            for k in range(index, i, -1):
                data[k] = data[k - 1]
            data[i] = nilai
            print(f"  Geser elemen dan tempatkan {nilai} di posisi {i}")
        print(f"  Data setelah iterasi {i + 1}: {data}")
        print("-" * 50)
    return data

while True:
    masukan = input("Masukkan data yang ingin diurutkan (pisahkan dengan koma): ")
    data = validasi(masukan)
    
    print("Pilih jenis pengurutan:")
    print("1. Pengurutan naik (angka lalu string)")
    print("2. Pengurutan turun (string lalu angka)")
    jenis = input("Masukkan pilihan (1 atau 2): ").strip()
    while jenis not in ['1', '2']:
        jenis = input("Pilihan tidak valid. Masukkan 1 atau 2: ").strip()
    jenis = int(jenis)

    print("\nData sebelum diurutkan:", data)
    selection(data, jenis)

    if jenis == 1:
        print("Data setelah diurutkan naik:", data)
    else:
        print("Data setelah diurutkan turun:", data)

    ulang = input("\nIngin mengulang program? (ya/tidak): ").strip().lower()
    if ulang != 'ya':
        print("Terima kasih! Program selesai.")
        break
