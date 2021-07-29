from PriorityQueue import PriorityQueue
from utils import get_path_algorithm_search
from TreeSearch import TreeSearch


def uniform_cost_search(initial_state, goal_state, graph):

    def print_info_finish():
        print('LOG NODES OPENED FOR THE ALGORITHM:\n', log_verbose)
        print('----------------------------------')
        print('DIRECT_PATH OF THE ALGORITHM:\n',
              tree_search.get_path(goal_state))

    # inicializing the frontier with the first element
    # [{'value': 's', 'priority':20}]
    frontier = PriorityQueue([{'value': initial_state, 'priority': 0}])

    tree_search = TreeSearch(root=initial_state)

    # inicializing the explored
    explored = []

    # this list indicate who open to who
    # log = []
    # this list tell you who open to who with the total_cost
    log_verbose = '\n'
    while not frontier.is_empty():

        # getting current data and removing it
        state = frontier.get()
        # adding the state's name to the explored list
        explored.append(state['value'])

        # arrive us to the goal
        if(state['value'] == goal_state):
            print_info_finish()
            return True

        # iterate the neigbors of the state for add each one of them into the frontier list,if not is in explored list and frontier list :)
        for neighbor in graph.neighbors(state['value']):

            if (not neighbor in explored):
                # log.append((state['value'], neighbor))
                # adding the log of tree search
                tree_search.add((state['value'], neighbor))
                # this get the path of this node to the root
                path = tree_search.get_path(neighbor)

                # getting cost of this node
                total_cost = 0
                previous = neighbor
                for el in path:
                    cost = graph.get_edge_data(previous, el)
                    if cost is None:
                        continue
                    previous = el
                    total_cost += cost['distance']

                frontier.push({'value': neighbor, 'priority': total_cost})

                # this is un log for register the descovery nodes
                log_verbose += '{} ABRIO: {} WITH COST: {}\n'.format(
                    state['value'], neighbor, total_cost)

    print_info_finish()
    return False
