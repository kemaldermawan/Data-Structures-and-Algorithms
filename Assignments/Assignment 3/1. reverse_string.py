class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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

if __name__ == "__main__":
    print("Masukkan teks. Tekan Enter kosong untuk selesai:\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    print("\nTeks setelah dibalik:\n")
    for line in lines:
        print(balik_string(line))