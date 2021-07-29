

# last in first out(LIFO)

class Stack:  # Creamos la clase Stack

    def __init__(self, initial_array=[]):
        self.items = initial_array

    def __str__(self): return str(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def print_stack(self):
        print(self.items)

    def contain(self, item): return item in self.items

    def get(self):
        # determaning the last position
        last_pos = len(self.items) - 1
        # getting the item in the last position
        item = self.items[last_pos]
        # deleting the item in the last position
        self.items.pop(last_pos)
        return item
