from utils import exists_dict_in_list


class PriorityQueue:

    def __init__(self, initial_array=[]):
        self.items = initial_array
        self.sort()

    # using bubble_sort
    def sort(self):
        list_dict = self.items
        comparaciones = 0
        n = len(list_dict)
        new_list = list_dict
        for i in range(1, n):
            for j in range(n-i):
                comparaciones += 1

                if list_dict[j]['priority'] > list_dict[j+1]['priority']:
                    new_list[j], new_list[j+1] = list_dict[j+1], list_dict[j]
        self.items = new_list

    def __str__(self): return str(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.sort()
        return

    def print_queue(self):  # Metodo para mostrar los elementos del queue
        print(self.items)

    def contain(self, item):
        return exists_dict_in_list(list=self.items, key='value', value=item)

    def get(self):
        # getting the item that is in the fist position
        item = self.items[0]
        # deleting the item that is in the fist position
        self.items.pop(0)
        return item

    def get_all(self): return self.items
