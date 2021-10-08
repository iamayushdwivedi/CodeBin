class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def InsertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end = ' -> ')
            temp = temp.next

def main():
    singlyLinkedList = LinkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyLinkedList.InsertAtBegin(arr[i])
    singlyLinkedList.printLinkedList()

if __name__ == '__main__':
    main()