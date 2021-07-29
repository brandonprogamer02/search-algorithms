import networkx as nx
import matplotlib.pyplot as plt
from numpy import left_shift


def getDictFromList(list, key, value):
    for i in list:
        if i[key] == value:
            return i
    return -1


def exists_dict_in_list(list, key, value):
    for i in list:
        if i[key] == value:
            return True
    return False


def draw_graph(graph):
    plt.subplot(121)

    nx.draw(graph, with_labels=True, font_weight='bold',
            font_size=20, node_color='white')
    plt.show()


# this function return the path that take the search algorithm for arrive to the goal_state
# INPUT:
#   log_list = [(1, 9), (1, 2), (2, 8), (2, 3), (3, 4), (4, 5), (5, 11), (11, 10), (11, 7), (11, 6)]
#   initial_state = 1; final_state = 6
# OUTPUT: [11, 5, 4, 3, 2, 1]
def get_path_algorithm_search(
    # log_list is a list with tuples that indicate who opened to who. Ex: 11 opened 6. (taking the input of top)
    log_list, initial_state  # initial_state is a initial_state of the graph
    , goal_state  # goal_state is the state of finising of the graph
):

    # this function return who open to who
    # ex: we've list: [(86,2),(54,4),(2,10)]; who_open_me(10) => 2
    def who_open_me(state):
        for i in log_list:
            if i[1] == state:
                return i[0]

    # this is the variable for can do the recursion
    save = goal_state
    log = [goal_state]
    while True:
        # conditional to exit if the iterator arrive to the final
        if save == initial_state:
            break

        save = who_open_me(save)
        # saving the opener in the log
        log.append(save)

    return log
