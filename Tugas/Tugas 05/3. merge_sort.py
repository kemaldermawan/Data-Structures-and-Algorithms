def merge(data, level=0): # Fungsi untuk mengurutkan data menggunakan algoritma Merge Sort
    if len(data) > 1: 
        tengah = len(data) // 2 # Mencari titik tengah
        kiri, kanan = data[:tengah], data[tengah:]

        indent = '  ' * level
        print(f"{indent}Memecah: {data} -> {kiri} | {kanan}")

        merge(kiri, level + 1) 
        merge(kanan, level + 1)

        i = j = k = 0
        while i < len(kiri) and j < len(kanan): # Menggabungkan dua sub-array
            if kiri[i] < kanan[j]: # Jika elemen kiri lebih kecil
                data[k] = kiri[i]
                i += 1
            else: # Jika elemen kanan lebih kecil
                data[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri): # Menyalin sisa elemen kiri
            data[k] = kiri[i] # Jika elemen kiri lebih kecil
            i += 1
            k += 1

        while j < len(kanan): # Menyalin sisa elemen kanan
            data[k] = kanan[j] # Jika elemen kanan lebih kecil
            j += 1
            k += 1

        print(f"{indent}Menggabung: {kiri} + {kanan} -> {data}") # Menampilkan hasil penggabungan
    return data

def main():
    ulang = 'ya' 
    while ulang == 'ya':
        masukan = input("Masukkan data (pisahkan dengan spasi): ")
        if masukan.strip() == '':
            print("Input kosong. Harap masukkan angka yang dipisahkan spasi.\n")
            ulang = input("Ulangi program? (ya/tidak): ").strip().lower()
            continue

        data = list(map(int, masukan.split())) # Mengubah input menjadi list integer
        print("\nSebelum diurutkan:", data)
        hasil = merge(data)
        print("\nSetelah diurutkan:", hasil)

        ulang = input("\nUlangi program? (ya/tidak): ").strip().lower() # Mengulang program
    print("Terima kasih! Program selesai.")

main() # Menjalankan fungsi utama