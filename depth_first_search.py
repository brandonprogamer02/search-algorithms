from Stack import Stack
from utils import get_path_algorithm_search


def depth_first_search(initial_state, graph, goal_state):
    def print_info_finish():
        print('LOG NODES OPENED FOR THE ALGORITHM:\n', log_verbose)
        print('----------------------------------')
        print('DIRECT_PATH OF THE ALGORITHM:\n', get_path_algorithm_search(log_list=log,
                                                                           goal_state=goal_state, initial_state=initial_state))

    # inicializing the frontier with the first element
    frontier = Stack([initial_state])

    # inicializing the explored
    explored = []
    log = []
    log_verbose = ''
    while not frontier.is_empty():

        # getting current data and removing it
        state = frontier.get()
        # adding the state's name to the explored list
        explored.append(state)

        # # # arrive us to the goal
        if(state == goal_state):
            print_info_finish()
            return True

        # iterate the neigbors of the state for add each one of them into the frontier list,if not is in explored list and frontier list :)
        for neighbor in graph.neighbors(state):

            if (not neighbor in explored) and (not frontier.contain(neighbor)):
                frontier.push(neighbor)
                # this is un log for register the descovery nodes
                log_verbose += '{} ABRIO: {} \n'.format(state, neighbor)
                log.append((state, neighbor))

    print_info_finish()
    return False
