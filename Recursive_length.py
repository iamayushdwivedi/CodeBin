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
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' -> ')
            temp = temp.next

    def LLR(self, temp):
        if temp is None:
            return 0
        return 1 + self.LLR(temp.next)

def main():
    singlyLinkedList = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyLinkedList.InsertAtEnd(arr[i])
    singlyLinkedList.printLinkedList()
    temp = singlyLinkedList.head
    print("\n", singlyLinkedList.LLR(temp))
if __name__ == '__main__':
    main()