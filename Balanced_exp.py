class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tos = -1

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def push(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tos += 1
            return
        newNode.next = self.head
        self.head = newNode
        self.tos += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        self.head = self.head.next
        self.tos -= 1

    def size(self):
        return self.tos + 1

    def top(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.head.data

def main():
    st = Stack()
    t = int(input())
    while t > 0:
        str = input()
        flag = 1
        for ele in str:
            if ele == '(':
                st.push(ele)
            else:
                if st.isEmpty():
                    flag = 0
                    break
                st.pop()
        if st.isEmpty() is False or flag == 0:
            print("Bracket Expression is not balanced")
        else:
            print("Bracket Expression is balanced")
        t -= 1

if __name__ == '__main__':
    main()
    