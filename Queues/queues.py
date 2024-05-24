class Queue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        return "Queue: " + " -> ".join(str(self.queue[(self.front + i) % self.capacity]) for i in range(self.size))

# Example usage
queue = Queue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue)          # Output: Queue: 10 -> 20 -> 30
print(queue.dequeue())# Output: 10
print(queue.peek())   # Output: 20
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)     # Output: Queue is full (since the capacity is 5)
print(queue)          # Output: Queue: 20 -> 30 -> 40 -> 50
