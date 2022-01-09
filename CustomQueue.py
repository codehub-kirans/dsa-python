class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.previous_node = None
        self.next_node = None

class DoublyLinkledList:
    def __init__(self) -> None:
        self.first_node = None
        self.last_node = None

    def insert_at_end(self, data):
        node = Node(data)
        print("Adding: ", node.data)

        if self.first_node is None or self.last_node is None:
            self.first_node = node
            self.last_node = node
        else:
            self.last_node.next_node = node
            self.last_node = node
    
    def remove_at_front(self):
        node = self.first_node

        if node is None or self.last_node is None:
            print("Nothing to remove")
        elif node == self.last_node:
            print("Removing Last: ", node.data)
            del node
            self.first_node = self.last_node = None
        else:
            print("Removing: ", node.data)
            self.first_node = self.first_node.next_node
            del node

    def is_empty(self):
        if self.first_node is None:
            return True
        else:
            return False
    
class Queue:
    def __init__(self) -> None:
        self.queue = DoublyLinkledList()

    def enqueue(self, data):
        self.queue.insert_at_end(data)

    def dequeue(self):
        self.queue.remove_at_front()

    def is_empty(self):
        return self.queue.is_empty()

#A Print Manager using Queue
def PrintManager():
    queue = Queue()
    queue.enqueue("Job 1")
    queue.enqueue("Job 2")
    queue.enqueue("Job 3")

    while queue.is_empty() is False:
        queue.dequeue()

    queue.enqueue("Job 4")
    queue.enqueue("Job 5")
    queue.enqueue("Job 6")

    while queue.is_empty() is False:
        queue.dequeue()
    
PrintManager()




