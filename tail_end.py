class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def InsertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' -> ')
            temp = temp.next

def main():
    singlyLinkedList = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyLinkedList.InsertAtEnd(arr[i])
    singlyLinkedList.printLinkedList()

if __name__ == '__main__':
    main()