import networkx as nx

dict_data = [
    {'name': 'vancouver',
     'neighbors': [['calgary', 100], ['seattle', 45]]},

    {'name': 'calgary',
     'neighbors': [['vancouver', 100], ['seattle', 118], ['winnipeg', 180], ['helena', 130]]},

    {'name': 'seattle',
     'neighbors': [['portland', 44], ['helena', 189], ['vancouver', 45], ['calgary', 118]]},

    {'name': 'portland',
     'neighbors': [['seattle', 44]]},

    {'name': 'winnipeg',
     'neighbors': [['helena', 137], ['calgary', 180]]},

    {'name': 'helena',
     'neighbors': [['seattle', 189], ['calgary', 130], ['winnipeg', 137]]}

]

dict_data2 = [
    {'name': 'boston', 'neighbors': ['new york']},
    {'name': 'new york', 'neighbors': ['boston', 'pittsburgh', 'washington']},
    {'name': 'pittsburgh', 'neighbors': ['new york', 'washington']},
    {'name': 'washington', 'neighbors': ['new york', 'pittsburgh']}
]


def graph1():
    my_graph = nx.Graph()

    my_graph.add_node(1)
    my_graph.add_edge(1, 9)
    my_graph.add_edge(1, 2)

    my_graph.add_node(0)
    my_graph.add_edge(0, 12)
    my_graph.add_edge(0, 9)

    my_graph.add_node(9)
    my_graph.add_edge(9, 10)
    my_graph.add_edge(9, 8)

    my_graph.add_node(2)
    my_graph.add_edge(2, 1)
    my_graph.add_edge(2, 8)
    my_graph.add_edge(2, 3)

    my_graph.add_node(10)
    my_graph.add_edge(10, 9)
    my_graph.add_edge(10, 8)
    my_graph.add_edge(10, 11)

    my_graph.add_node(12)
    my_graph.add_edge(12, 0)
    my_graph.add_edge(12, 7)

    my_graph.add_node(7)
    my_graph.add_edge(7, 12)
    my_graph.add_edge(7, 11)

    my_graph.add_node(11)
    my_graph.add_edge(11, 7)
    my_graph.add_edge(11, 6)
    my_graph.add_edge(11, 8)
    my_graph.add_edge(11, 5)

    my_graph.add_node(6)
    my_graph.add_edge(6, 11)

    my_graph.add_node(8)
    my_graph.add_edge(8, 9)
    my_graph.add_edge(8, 2)
    my_graph.add_edge(8, 3)
    my_graph.add_edge(8, 4)
    my_graph.add_edge(8, 5)
    my_graph.add_edge(8, 11)
    my_graph.add_edge(8, 10)

    my_graph.add_node(5)
    my_graph.add_edge(5, 11)
    my_graph.add_edge(5, 8)
    my_graph.add_edge(5, 4)

    my_graph.add_node(4)
    my_graph.add_edge(4, 8)
    my_graph.add_edge(4, 5)
    my_graph.add_edge(4, 3)

    my_graph.add_node(3)
    my_graph.add_edge(3, 8)
    my_graph.add_edge(3, 2)
    my_graph.add_edge(3, 4)
    return my_graph


def graph2():
    my_graph = nx.Graph()

    my_graph.add_node('s')
    my_graph.add_edge('s', 'a', distance=3)
    my_graph.add_edge('s', 'b', distance=6)
    my_graph.add_edge('s', 'c', distance=2)

    my_graph.add_node('a')
    my_graph.add_edge('a', 'd', distance=3)

    my_graph.add_node('b')
    my_graph.add_edge('b', 'd', distance=4)
    my_graph.add_edge('b', 'e', distance=2)
    my_graph.add_edge('b', 'g', distance=9)

    my_graph.add_node('c')
    my_graph.add_edge('c', 'e', distance=1)

    my_graph.add_node('d')
    my_graph.add_edge('d', 'f', distance=5)

    my_graph.add_node('e')
    my_graph.add_edge('e', 'h', distance=5)
    my_graph.add_edge('e', 'f', distance=6)

    my_graph.add_node('f')
    my_graph.add_edge('f', 'g', distance=5)

    my_graph.add_node('h')
    my_graph.add_edge('h', 'g', distance=8)

    my_graph.add_node('g')

    return my_graph
