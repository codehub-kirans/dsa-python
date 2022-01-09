from collections import deque

class Queue:
    """A Queue Class"""
    def __init__(self) -> None:
        self.data= deque([])

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.popleft()
    
    def inspect(self):
        return self.data[0]

    def isEmpty(self):
        if self.data:
            return False
        else:
            return True
    

#A Print Manager using Queue
def PrintManager():
    queue = Queue()
    queue.enqueue("Job 1")
    queue.enqueue("Job 2")
    queue.enqueue("Job 3")

    while queue.isEmpty() is False:
        print(queue.dequeue())
    
PrintManager()