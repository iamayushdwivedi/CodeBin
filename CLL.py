class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
            return
        self.tail.next = newNode
        self.tail = newNode
        self.tail.next = self.head

    def InsertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head
        newNode.next = self.head
        self.head = newNode
        self.tail.next = self.head

    def InsertAtithPos(self, i, data):
        newNode = Node(data)
        n = self.LengthOfLinkedList()
        if i == 0:
            self.InsertAtBegin(data)
            return
        if i == n - 1:
            self.InsertAtEnd(data)
            return
        if i > n:
            print("Invalid Position")
            return
        count = 0
        temp = self.head
        while True and count is not (i - 1):
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        newNode.next = temp.next
        temp.next = newNode
    def LengthOfLinkedList(self):
        temp = self.head
        count = 0
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
        return count

    def printCLL(self):
        temp = self.head
        while True:
            print(temp.data, end = ' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print()

    def DeleteAtEnd(self):
        if self.head is None:
            return
        if self.head.next is self.head:
            self.head = None
            self.tail = None
            return
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        self.tail.next = None
        self.tail = temp
        self.tail.next = self.head

    def DeleteAtBegin(self):
        if self.head is None:
            return
        if self.head.next is self.head:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.tail.next = self.head

    def DeleteAtGivenPos(self, i):
        n = self.LengthOfLinkedList()
        if i == 0:
            self.DeleteAtBegin()
            return
        if i == n - 1:
            self.DeleteAtEnd()
            return
        if i > n:
            print("Invalid Position")
            return
        temp = self.head
        count = 0
        while True and count is not (i - 1):
            count += 1
            temp = temp.next
            if temp.next == self.head:
                break
        temp.next = temp.next.next

if __name__ == '__main__':
    circularLL = CircularLL()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        circularLL.InsertAtEnd(arr[i])
    circularLL.printCLL()
    circularLL.DeleteAtGivenPos(2)
    circularLL.printCLL()  