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

    def InsertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def insertAtithPosition(self, i, data):
        newNode = Node(data)
        if i == 0:
            self.InsertAtBegin(data)
        else:
            count = 0
            temp = self.head
            while temp.next is not None and count is not (i - 1):
                count += 1
                temp = temp.next
            if temp.next is None and i > count + 1:
                return
            else:
                newNode.next = temp.next
                temp.next = newNode


    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' -> ')
            temp = temp.next

def main():
    singlyLinkedList = LinkedList()
    i = int(input())
    arr = list(map(int, input().split()))
    singlyLinkedList.insertAtithPosition(i, 100)
    singlyLinkedList.printLinkedList()

if __name__ == '__main__':
    main()