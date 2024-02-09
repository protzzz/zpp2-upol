seznam = []

def push(item):
    seznam.append(item)

def pop():
    if len(seznam) == 0:
        return None
    return seznam.pop()

def print_seznam():
    print("seznam:", end=" ")
    for item in seznam:
        print(item, end=" ")
    print()

queue = []

def enqueue(item):
    queue.append(item)

def dequeue():
    if len(queue) == 0:
        return None
    return queue.pop(0)

def print_queue():
    print("Queue:", end=" ")
    for item in queue:
        print(item, end=" ")
    print()

push(1)
push(2)
push(3)
print_seznam()
pop()
push(2)
print_seznam()
print(pop())
print(pop())
print_seznam()


print()

enqueue(1)
enqueue(2)
enqueue(3)
print_queue()
print(dequeue())
print_queue()
print(dequeue())
print(dequeue())
print(dequeue())
print_queue()
