class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertAtEnd(self, data):
        NewNode = Node(data)
        temp = self.head
        if self.head is None:
            self.head = NewNode
            self.tail = NewNode
        self.tail.next = NewNode
        NewNode.prev = self.tail
        self.tail = NewNode

    def InsertAtBegin(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
        NewNode.next = self.head
        self.head.prev = NewNode
        self.head = NewNode

    def InsertAtGivenPos(self, i, data):
        newNode = Node(data)
        n = self.lengthofDLL()
        if i == 0:
            self.InsertAtBegin(data)
            return
        if i == n:
            self.InsertAtEnd(data)
            return
        if i > n:
            print("Invalid Position")
            return
        count = 0
        temp = self.head
        while temp.next is not None and count is not (i - 1):
            count += 1
            temp = temp.next
        newNode.prev = temp
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode

    def printDLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' --> ')
            temp = temp.next

    def rotate(self, N):
        temp = self.head
        count = 0
        while temp is not None and count is not (N-1):
            temp = temp.next
            count += 1
        temp2 = temp.next
        if temp2 is None:
            return
        temp.next = None
        temp2.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.head = temp2
        self.tail = temp

    def DeleteFromEnd(self):
        if self.head is None:
            print("Linked List is empty")
            return
        temp = self.tail.prev
        temp.next = None
        self.tail.prev = None
        temp = self.tail

    def DeleteFromBegin(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head.next
        if temp is None:
            self.head = None
            return
        self.head.next = None
        temp.prev = None
        self.head = temp

    def DeleteFromGivenPos(self, i):
        n = self.lengthofDLL()
        if i > n:
            print("Invalid Position")
            return
        if i == 0:
            self.DeleteFromBegin()
            return
        if i == n:
            self.DeleteFromEnd()
            return
        count = 0
        temp = self.head
        while temp.next is not None:
            count += 1
            temp = temp.next
        temp1 = temp.prev
        temp2 = temp.next
        temp.next = None
        temp.prev = None
        temp1.next = temp2
        temp2.prev = temp1

    def lengthofDLL(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next
        return count

if __name__ == '__main__':
    doublyLL = DoublyLinkedList()
    t = int(input())
    while t != 0:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        for i in range(n):
            doublyLL.InsertAtEnd(arr[i])
        doublyLL.printDLL()
        print("\n")
        doublyLL.rotate(k)
        doublyLL.printDLL()
        t -= 1