class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Masukkan karakter di depan linked list (mirip stack push)
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Ambil string dari linked list mulai dari head sampai akhir
    def to_string(self):
        result = ""
        current = self.head
        while current:
            result += current.data
            current = current.next
        return result

def balik_string(text):
    ll = LinkedList()
    for char in text:
        ll.push(char)
    return ll.to_string()

# --- Program utama ---
if __name__ == "__main__":
    teks = input("Masukkan string yang ingin dibalik: ")
    hasil = balik_string(teks)
    print("Hasil string dibalik:")
    print(hasil)