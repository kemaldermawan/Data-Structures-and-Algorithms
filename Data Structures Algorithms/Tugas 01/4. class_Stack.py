class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Stack kosong!"
        removed = self.items.pop()
        return f"'{removed}' telah dihapus dari stack."

    def peek(self):
        if len(self.items) == 0: 
            return "Stack kosong!"
        return self.items[-1]

    def clear(self):
        self.items = []
        return "Stack telah dikosongkan."

    def display(self):
        if len(self.items) == 0:
            return "Stack kosong."
        return "\n".join(f"- {item}" for item in reversed(self.items))


stack = Stack()

while True:
    print("\n=== Menu Stack ===")
    print("1. Push (Tambah Elemen)")
    print("2. Pop (Hapus Elemen Teratas)")
    print("3. Peek (Lihat Elemen Teratas)")
    print("4. Clear (Kosongkan Stack)")
    print("5. Tampilkan Stack")
    print("6. Keluar Program")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        nama = input("Masukkan nama yang ingin ditambahkan ke stack: ")
        stack.push(nama)
        print(f"'{nama}' berhasil ditambahkan.")
    elif pilihan == "2":
        print(stack.pop())
    elif pilihan == "3":
        print(stack.peek())
    elif pilihan == "4":
        print(stack.clear())
    elif pilihan == "5":
        print(stack.display())
    elif pilihan == "6":
        ulang = input("Apakah Anda ingin mengulang program? (ya/tidak): ").strip().lower()
        if ulang != "ya":
            print("Terima kasih! Program selesai.")
            break
    else:
        print("Pilihan tidak valid. Silakan masukkan angka 1-6.")