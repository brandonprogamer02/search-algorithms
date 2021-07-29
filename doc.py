from graphs import graph2

G = graph2()

# set attribute from the a node
G.nodes.get('s')['price'] = 1000

# get attribute from the a node
G.nodes.get('s')['price']

# set attribute from the a edge
G.get_edge_data('s', 'b')['distance'] = 100

# get attribute from the a node
G.get_edge_data('s', 'b')['distance']
