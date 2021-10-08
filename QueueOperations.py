class Queue:
    def __init__(self, cap):
        self.queue = [None]*cap
        self.front = -1
        self.rear = -1
        self.size = 0
        self.cap = cap

    def isEmpty(self):
        return self.front == -1

    def enQueue(self, data):
        if (self.rear + 1) % self.cap == self.front:
            print("Queue is full")
            return
        if self.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = data
            self.size += 1
            return
        self.rear = (self.rear + 1) % self.cap
        self.queue[self.rear] = data
        self.size += 1

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        if self.rear == self.front:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            self.size -= 1
            return
        temp = self.queue[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1

    def frontele(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.queue[self.front]

    def PrintQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        for i in range(self.size):
            print(self.queue[(self.front + i) % self.cap], end = " ")
        print()

def reverse(que):
    if que.isEmpty():
        return
    temp = que.deQueue()
    reverse(que)
    que.enQueue(temp)


def main():
    cap = int(input())
    queue = Queue(cap)
    for i in input().split():
        queue.enQueue(int(i))
    queue.PrintQueue()
    queue.deQueue()
    queue.PrintQueue()

if __name__ == '__main__':
    main()