import snoop
from loguru import logger


class Heap:
    """Heap Sort Class"""

    def __init__(self) -> None:
        self.data = []

    def root_node(self):
        if self.data:
            return self.data[0]
        else:
            return None

    def last_node(self):
        if self.data:
            return self.data[-1]
        else:
            return None

    def last_node_index(self):
        return len(self.data) - 1

    def parent_index(self, index) -> int:
        return int((index - 1) / 2)

    def leftchild_index(self, index) -> int:
        return int((index * 2) + 1)

    def rightchild_index(self, index) -> int:
        return int((index * 2) + 2)

    def insert(self, value):
        self.data.append(value)
        new_node_index = self.last_node_index()

        while (
            new_node_index > 0
            and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]
        ):
            self.data[self.parent_index(new_node_index)], self.data[new_node_index] = (
                self.data[new_node_index],
                self.data[self.parent_index(new_node_index)],
            )
            new_node_index = self.parent_index(new_node_index)

    def delete(self):
        if self.data:
            popped_value = self.root_node()
            print("Popped: ", popped_value)
            trickle_node_value = self.data.pop()

            if len(self.data) > 0:
                self.data[0] = trickle_node_value
                trickle_node_index = 0

                while self.has_larger_child(trickle_node_index):
                    greater_child_index = self.calculate_larger_child_index(
                        trickle_node_index
                    )
                    self.data[trickle_node_index], self.data[greater_child_index] = (
                        self.data[greater_child_index],
                        self.data[trickle_node_index],
                    )

                    trickle_node_index = greater_child_index

                return popped_value
        else:
            print("Heap is empty. Nothing to delete!")
            return None

    def has_larger_child(self, index):
        # if the node has no children, return false straightaway
        if self.leftchild_index(index) > self.last_node_index():
            return False

        # check if last node is a right child by checking if right node index is <= the max index size of list
        if self.rightchild_index(index) <= self.last_node_index():
            if (
                self.data[self.rightchild_index(index)] > self.data[index]
                or self.data[self.leftchild_index(index)] > self.data[index]
            ):
                return True
            else:
                return False
        # else last node is left child
        elif self.data[self.leftchild_index(index)] > self.data[index]:
            return True
        else:
            return False

    def calculate_larger_child_index(self, index):
        # check if right child does not exist, i.e if it is greater than the max list index, return left child index
        if self.rightchild_index(index) > self.last_node_index():
            return self.leftchild_index(index)
        elif (
            self.data[self.leftchild_index(index)]
            > self.data[self.rightchild_index(index)]
        ):
            return self.leftchild_index(index)
        else:
            return self.rightchild_index(index)

    def print(self):
        print("Heap: ", self.data)
        print("Root Node: ", self.root_node(), "Last Node: ", self.last_node())
        print()


# Heap Test
h = Heap()

h.insert(5)
h.insert(9)
h.insert(3)
h.insert(7)
h.insert(11)
h.print()

h.delete()
h.delete()
h.delete()
h.delete()
h.delete()
h.delete()

h.print()
