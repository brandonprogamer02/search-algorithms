from Stack import Stack
import heapq as heapq
from graphs import graph2
import networkx as nx
from utils import draw_graph, get_path_algorithm_search
from time import time
from PriorityQueue import PriorityQueue
from TreeSearch import TreeSearch


def test():
    k = TreeSearch(1)
    ls = [
        # (1, 9),
        # (1, 2),
        # (2, 8),
        # (2, 3),
        # (3, 4),
        (4, 5),
        (5, 11),
        (11, 10),
        # (11, 7),
        (11, 6)]
    for i in ls:
        k.add(i)

    print('BEFORE REMOVE: ', k)
    k.remove(11)
    print('AFTER REMOVE: ', k)
    return
