
# first in first out (FIFO)

class Queue:  # Creamos la clase Stack

    def __init__(self, initial_array=[]):
        self.items = initial_array

    def __str__(self): return str(self.items)

    def is_empty(self):  # Metodo para verificar si la pila esta vacia
        return self.items == []

    def push(self, item):  # Metodo para insertar elementos a la pila
        self.items.append(item)

    def print_queue(self):  # Metodo para mostrar los elementos de la pila
        print(self.items)

    def contain(self, item): return item in self.items

    def get(self):
        # getting the item that is in the fist position
        item = self.items[0]
        # deleting the item that is in the fist position
        self.items.pop(0)
        return item
