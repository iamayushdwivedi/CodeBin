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
def precedence(str):
    if str == '^':
        return 3
    if str == '*' or str == '/':
        return 2
    if str == '+' or str == '-':
        return 1
    if str == '(' or str == ')':
        return -1
    else:
        return 0

def main():
    st = Stack()
    arr = list(input().split())
    str = ''
    for i in range(len(arr)):
        val = precedence(arr[i])
        if val == 0:
            str += arr[i]
        else:
            if arr[i] == '(':
                st.push(arr[i])
            elif arr[i] == ')':
                while st.isEmpty() is False and st.top != '(':
                    str += arr[i]
                    st.pop()
                if st.top == "(":
                    st.pop()
            else:
                while st.isEmpty() is False and precedence(arr[i]) <= precedence(st.top()):
                    str += st.top()
                    st.pop()
                st.push(arr[i])
    while st.isEmpty() is False:
        str += st.top()
        st.pop()
    print(str)

if __name__ == '__main__':
    main()