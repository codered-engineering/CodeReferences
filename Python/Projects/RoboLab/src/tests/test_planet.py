#!/usr/bin/env python3

import unittest
from planet import Direction, Planet


class ExampleTestPlanet(unittest.TestCase):
    def setUp(self):
        """
        Instantiates the planet data structure and fills it with paths

        +--+
        |  |
        +-0,3------+
           |       |
          0,2-----2,2 (target)
           |      /
        +-0,1    /
        |  |    /
        +-0,0-1,0
           |
        (start)

        """
        # Initialize your data structure here
        self.planet = Planet()
        self.planet.add_path(((0, 0), Direction.NORTH), ((0, 1), Direction.SOUTH), 1)
        self.planet.add_path(((0, 1), Direction.WEST), ((0, 0), Direction.WEST), 1)

    @unittest.skip('Example test, should not count in final test results')
    def test_target_not_reachable_with_loop(self):
        """
        This test should check that the shortest-path algorithm does not get stuck in a loop between two points while
        searching for a target not reachable nearby

        Result: Target is not reachable
        """
        self.assertIsNone(self.planet.shortest_path((0, 0), (1, 2)))


class TestRoboLabPlanet(unittest.TestCase):
    def setUp(self):
        """
        Instantiates the planet data structure and fills it with paths

        MODEL YOUR TEST PLANET HERE (if you'd like):

           +----(-2,2)----+
           |       |      |
         -3,1---(-2,1)   1,1
           |       |      |
           +----(-2,0)    |
                   |      |
      +----+       |      |
      |    |       |      |
      +-(-3,-1)-(-2,-1) -1,-1
           |       |      |
           +----(-2,-2) -1,-2
                   |      |
                   X   (start)

        """
        # Initialize your data structure here
        self.planet = Planet()
        # self.planet.add_path(...)
        # Gromit https://robolab.inf.tu-dresden.de/planets/Gromit.svg
        self.planet.add_path(((-1, -2), Direction.NORTH), ((-1, -1), Direction.SOUTH), 1) 
        self.planet.add_path(((-1, -1), Direction.NORTH), ((-1, 1), Direction.SOUTH), 1)
        self.planet.add_path(((-1, 1), Direction.NORTH), ((-2, 2), Direction.EAST), 1)
        self.planet.add_path(((-2, 2), Direction.WEST), ((-3, 1), Direction.NORTH), 1)
        self.planet.add_path(((-2, 2), Direction.SOUTH), ((-2, 1), Direction.NORTH), 1)
        self.planet.add_path(((-3, 1), Direction.EAST), ((-2, 1), Direction.WEST), 1)
        self.planet.add_path(((-3, 1), Direction.SOUTH), ((-2, 0), Direction.WEST), 1)
        self.planet.add_path(((-2, 1), Direction.SOUTH), ((-2, 0), Direction.NORTH), 1)
        self.planet.add_path(((-2, 0), Direction.SOUTH), ((-2, -1), Direction.NORTH), 1)
        self.planet.add_path(((-2, -1), Direction.WEST), ((-3, -1), Direction.EAST), 1)
        self.planet.add_path(((-2, -1), Direction.SOUTH), ((-2, -2), Direction.NORTH), 1)
        self.planet.add_path(((-3, -1), Direction.NORTH), ((-3, -1), Direction.WEST), 1)
        self.planet.add_path(((-3, -1), Direction.SOUTH), ((-2, -2), Direction.WEST), 1)

    def test_integrity(self):
        """
        This test should check that the dictionary returned by "planet.get_paths()" matches the expected structure
        """
        self.assertDictEqual(
            {
                (-1, -2): {
                    Direction.NORTH: ((-1, -1), Direction.SOUTH, 1)
                },
                (-1, -1): {
                    Direction.SOUTH: ((-1, -2), Direction.NORTH , 1),
                    Direction.NORTH: ((-1, 1), Direction.SOUTH, 1)
                },
                (-1, 1): {
                    Direction.SOUTH: ((-1, -1), Direction.NORTH , 1),
                    Direction.NORTH: ((-2, 2), Direction.EAST, 1)
                },
                (-2, 2): {
                    Direction.EAST: ((-1, 1), Direction.NORTH , 1),
                    Direction.WEST: ((-3, 1), Direction.NORTH , 1),
                    Direction.SOUTH: ((-2, 1), Direction.NORTH , 1)
                },
                (-3, 1): {
                    Direction.NORTH : ((-2, 2), Direction.WEST, 1),
                    Direction.EAST: ((-2, 1), Direction.WEST, 1),
                    Direction.SOUTH: ((-2, 0), Direction.WEST, 1)
                },
                (-2, 1): {
                    Direction.NORTH : ((-2, 2), Direction.SOUTH, 1),
                    Direction.WEST: ((-3, 1), Direction.EAST, 1),
                    Direction.SOUTH: ((-2, 0), Direction.NORTH , 1)
                },
                (-2, 0): {
                    Direction.WEST: ((-3, 1), Direction.SOUTH, 1),
                    Direction.NORTH : ((-2, 1), Direction.SOUTH, 1),
                    Direction.SOUTH: ((-2, -1), Direction.NORTH , 1)
                },
                (-2, -1): {
                    Direction.NORTH : ((-2, 0), Direction.SOUTH, 1),
                    Direction.WEST: ((-3, -1), Direction.EAST, 1),
                    Direction.SOUTH: ((-2, -2), Direction.NORTH , 1)
                },
                (-3, -1): {
                    Direction.EAST: ((-2, -1), Direction.WEST, 1),
                    Direction.NORTH : ((-3, -1), Direction.WEST, 1),
                    Direction.WEST: ((-3, -1), Direction.NORTH , 1),
                    Direction.SOUTH: ((-2, -2), Direction.WEST, 1)
                },
                (-2, -2): {
                    Direction.NORTH : ((-2, -1), Direction.SOUTH, 1),
                    Direction.WEST: ((-3, -1), Direction.SOUTH, 1)
                }
            }, self.planet.get_paths())

    def test_empty_planet(self):
        """
        This test should check that an empty planet really is empty
        """
        self.assertDictEqual(Planet().get_paths(), {})

    def test_target(self):
        """
        This test should check that the shortest-path algorithm implemented works.

        Requirement: Minimum distance is three nodes (two paths in list returned)
        """
        self.assertListEqual(
            [
                ((-1, -2), Direction.NORTH),
                ((-1, -1), Direction.NORTH),
                ((-1, 1), Direction.NORTH),
                ((-2, 2), Direction.WEST),
                ((-3, 1), Direction.SOUTH),
                ((-2, 0), Direction.SOUTH),
                ((-2, -1), Direction.SOUTH)
            ], self.planet.shortest_path((-1, -2), (-2, -2)))

    def test_target_not_reachable(self):
        """
        This test should check that a target outside the map or at an unexplored node is not reachable
        """
        self.assertIsNone(self.planet.shortest_path((-1, -2), (0, 0)))

    def test_same_length(self):
        """
        This test should check that the shortest-path algorithm implemented returns a shortest path even if there
        are multiple shortest paths with the same length.

        Requirement: Minimum of two paths with same cost exists, only one is returned by the logic implemented
        """
        self.assertListEqual(self.planet.shortest_path((-2, 2), (-2, 0)), self.planet.shortest_path((-2, 2), (-2, 0)))

    def test_target_with_loop(self):
        """
        This test should check that the shortest-path algorithm does not get stuck in a loop between two points while
        searching for a target nearby

        Result: Target is reachable
        """
        self.assertListEqual(
            [
                ((-3, 1), Direction.NORTH),
                ((-2, 2), Direction.EAST)
            ], self.planet.shortest_path((-3, 1), (-1, 1)))

    def test_target_not_reachable_with_loop(self):
        """
        This test should check that the shortest-path algorithm does not get stuck in a loop between two points while
        searching for a target not reachable nearby

        Result: Target is not reachable
        """
        # block the path
        self.planet.add_path(((-1, 1), Direction.NORTH), ((-2, 2), Direction.EAST), -1)
        self.assertIsNone(self.planet.shortest_path((-3, 1), (-1, 1)))


if __name__ == "__main__":
    unittest.main()
