from breadth_first_search import breadth_first_search
from depth_first_search import depth_first_search
from uniform_cost_search import uniform_cost_search
from test import test
from graphs import graph1, graph2
from utils import draw_graph


def main():
    print('------ejecutando test------')
    test()
    print('------ejecutando codigo normal------')

    # breadth_first_search(
    #     initial_state=1,
    #     graph=graph1(),
    #     goal_state=6)

    # depth_first_search(
    #     initial_state=1,
    #     graph=graph1(),
    #     goal_state=6
    # )

    uniform_cost_search(
        initial_state='s',
        graph=graph2(),
        goal_state='f'
    )
    # draw_graph(graph2())


main()
