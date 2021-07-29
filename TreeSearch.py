
class TreeSearch:

    # self.items ex: [
    # (1, 9),
    # (1, 2),
    # (2, 8),
    # (2, 3),
    # (3, 4),
    # (4, 5),
    # (5, 11),
    # (11, 10),
    # (11, 7),
    # (11, 6)]
    # self.root ex: 1
    # self.node ex: 6
    def __init__(self, root):
        self.root = root  # this is the root of the Three
        # self.items is a list with tuples that indicate who opened to who. Ex: 11 opened 6 (11,6). (taking the input of top)
        self.items = []
        self.log = '\n'
        return

    def __str__(self):
        return str(self.items)

    # this function remove a node and its children

    def remove(self, node):
        # seaching dependencies of this node and removing it
        count = 0
        for i in self.items:
            print(i)
            if i[0] == node:
                self.items.pop(count)
            count += 1

        # and removing the node who created it
        for i in self.items:
            if i[1] == node:
                self.items.remove(i)

    # param must be tuple: (opener, opened)
    def add(self, param):
        self.items.append(param)
        self.log += '\'{}\' open \'{}\' \n'.format(param[0], param[1])

    # this function return who open to who
    # ex: we've list: [(86,2),(54,4),(2,10)]; who_open_me(10) => 2
    def who_open_me(self, state):
        for i in self.items:
            if i[1] == state:
                return i[0]

    # this function return the path that take the search algorithm for arrive to the goal_state
    # taking the data such as example => OUTPUT: [11, 5, 4, 3, 2, 1]
    def get_path(self, node):

        # this is the variable for can do the recursion
        save = node
        log = [node]
        while True:
            # conditional to exit if the iterator arrive to the final
            if save == self.root:
                break

            save = self.who_open_me(save)
            # saving the opener in the log
            log.append(save)

        return log
