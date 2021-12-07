class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

    def put(self, data):
        if self.front == None:
            self.front = Node(data)
            self.rear = self.front
        else:
            node = self.front
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.rear = new

    def get(self):
        node = self.front
        if node == None:
            return None
        else:
            temp = node.data
            self.front = self.front.next
            return temp


    def peek(self):
        node = self.front
        if node == None:
            return None
        else:
            return node.data


# Test code
queue = LinkedQueue()

print(queue.is_empty())
for i in range(10):
    queue.put(i)
print(queue.is_empty())

for _ in range(11):
    print(queue.get(), end=' ')
print()

for i in range(20):
    queue.put(i)
print(queue.is_empty())

for _ in range(5):
    print(queue.peek(), end = " ")
print()

for _ in range(21):
    print(queue.get(), end=' ')
print()
print(queue.is_empty())