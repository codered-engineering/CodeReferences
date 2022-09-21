#!/usr/bin/env python3

# Attention: Do not import the ev3dev.ev3 module in this file
from enum import IntEnum, unique
from typing import List, Tuple, Dict, Union


@unique
class Direction(IntEnum):
    """ Directions in shortcut """
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270


Weight = int
"""
Weight of a given path (received from the server)

Value:  -1 if blocked path
        >0 for all other paths
        never 0
"""


class Planet:
    """
    Contains the representation of the map and provides certain functions to manipulate or extend
    it according to the specifications
    """

    def __init__(self):
        """ Initializes the data structure """
        self.paths = {}

    def add_path(self, start: Tuple[Tuple[int, int], Direction], target: Tuple[Tuple[int, int], Direction],
                 weight: int):
        """
         Adds a bidirectional path defined between the start and end coordinates to the map and assigns the weight to it

        Example:
            add_path(((0, 3), Direction.NORTH), ((0, 3), Direction.WEST), 1)
        :param start: 2-Tuple
        :param target:  2-Tuple
        :param weight: Integer
        :return: void
        """

        # YOUR CODE FOLLOWS (remove pass, please!)
        if weight > 0 or weight == -1:
            if start[0] in self.paths:
                self.paths[start[0]][start[1]] = (target[0], target[1], weight)
            else:
                self.paths[start[0]] = {}
                self.paths[start[0]][start[1]] = (target[0], target[1], weight)
            if target[0] in self.paths:
                self.paths[target[0]][target[1]] = (start[0], start[1], weight)
            else:
                self.paths[target[0]] = {}
                self.paths[target[0]][target[1]] = (start[0], start[1], weight)
        else:
            raise ValueError('Weight of path must be a positive int or -1 if path is blocked')

    def get_paths(self) -> Dict[Tuple[int, int], Dict[Direction, Tuple[Tuple[int, int], Direction, Weight]]]:
        """
        Returns all paths

        Example:
            {
                (0, 3): {
                    Direction.NORTH: ((0, 3), Direction.WEST, 1),
                    Direction.EAST: ((1, 3), Direction.WEST, 2),
                    Direction.WEST: ((0, 3), Direction.NORTH, 1)
                },
                (1, 3): {
                    Direction.WEST: ((0, 3), Direction.EAST, 2),
                    ...
                },
                ...
            }
        :return: Dict
        """

        # YOUR CODE FOLLOWS (remove pass, please!)
        return self.paths

    def shortest_path(self, start: Tuple[int, int], target: Tuple[int, int]) -> Union[None, List[Tuple[Tuple[int, int], Direction]]]:
        """
        Returns a shortest path between two nodes

        Examples:
            shortest_path((0,0), (2,2)) returns: [((0, 0), Direction.EAST), ((1, 0), Direction.NORTH)]
            shortest_path((0,0), (1,2)) returns: None
        :param start: 2-Tuple
        :param target: 2-Tuple
        :return: 2-Tuple[List, Direction]
        """

        # YOUR CODE FOLLOWS (remove pass, please!)
        if start not in self.paths.keys():
            return None
        if target not in self.paths.keys():
            return None

        # dijkstra's algorithm
        vertices = list(self.paths.keys())
        distances = {vertex: float("inf") for vertex in vertices}
        previous = {vertex: None for vertex in vertices}

        distances[start] = 0

        while vertices:
            vertex = min(vertices, key=lambda v: distances[v])
            vertices.remove(vertex)
            if vertex == target:
                break
            # target is unreachable
            if distances[vertex] == float("inf"):
                return None

            # update path weight
            for neighbour, _, weight in self.paths[vertex].values():
                # blocked path
                if weight == -1:
                    continue
                path_weight = distances[vertex] + weight
                if path_weight < distances[neighbour]:
                    distances[neighbour] = path_weight
                    previous[neighbour] = vertex

        # construct temporary path as a list of vertices
        tmp_path = []
        vertex = target
        while previous[vertex]:
            tmp_path.insert(0, previous[vertex])
            vertex = previous[vertex]

        # add target to the path
        tmp_path.append(target)

        # construct path as a list of tuples (vertex, direction)
        path = []
        i = 0
        while i < len(tmp_path) - 1:
            for direction, triplet in self.paths[tmp_path[i]].items():
                if triplet[0] == tmp_path[i + 1]:
                    path.append((tmp_path[i], direction))
            i += 1

        return path
