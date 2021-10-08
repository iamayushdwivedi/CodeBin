class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

if __name__ == '__main__':
    x = Node(1)
    y = Node(2)
    z = Node(3)
    p = Node(4)
    x.next = y
    y.prev = x
    y.next = z
    z.prev = y
    z.next = p
    p.prev = z
    temp = x
    while temp is not None:
        print(temp.data, end = ' --> ')
        temp = temp.next
