class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def InsertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def DeleteAtEnd(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def DeleteFromBegin(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next

    def DeleteAtGivenPos(self, i):
        n = self.CalculateLength(self.head)
        if self.head is None or i > n - 1:
            return
        if i == 0:
            self.DeleteFromBegin()
            return
        if i == n - 1:
            self.DeleteAtEnd()
            return
        count = 0
        temp = self.head
        while temp is not None and count is not (i - 1):
            count += 1
            temp = temp.next
        temp.next = temp.next.next


    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' -> ')
            temp = temp.next
    def CalculateLength(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count


def main():
    singlyLinkedList = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyLinkedList.InsertAtEnd(arr[i])
    singlyLinkedList.printLinkedList()
    singlyLinkedList.DeleteAtGivenPos(3)
    singlyLinkedList.printLinkedList()
    print("\n")
    singlyLinkedList.DeleteFromBegin()
    singlyLinkedList.printLinkedList()
    print("\n",singlyLinkedList.CalculateLength())
    temp = singlyLinkedList.head
if __name__ == '__main__':
    main()