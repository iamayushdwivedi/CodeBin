class QueueUsingCircularArray:
    def __init__(self, capacity):
        self.que = [None] * capacity
        self.size = 0
        self.front = -1
        self.rear = -1
        self.cap = capacity

    def isEmpty(self):
        return self.front == -1

    def enQueue(self, data):
        if (self.rear + 1) % self.cap == self.front:
            print("Queue is Full")
            return
        if self.isEmpty():
            self.front = self.rear = 0
            self.que[self.rear] = data
            self.size += 1
            return
        self.rear = (self.rear + 1) % self.cap
        self.que[self.rear] = data
        self.size += 1
        return

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        if self.front == self.rear:
            temp = self.que[self.front]
            self.size -= 1
            return temp
        temp = self.que[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return temp

    def frontele(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.front

    def printQueue(self):
        if self.isEmpty():
            return
        for i in range(self.size):
            print(self.que[(self.front + i) % self.cap], end = ' ')
        print()

def main():
    cap = int(input())
    que = QueueUsingCircularArray(cap)
    arr = list(map(int, input().split()))
