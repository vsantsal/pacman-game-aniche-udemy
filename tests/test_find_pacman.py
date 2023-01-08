import unittest

from pacman import find_pacman


class FindPacmanTest(unittest.TestCase):
    def test_returns_correct_cartesian_coordinates_when_pacman_is_once_in_map(self):
        # Arrange
        mapa = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|",
        ]
        # Act
        x, y = find_pacman(mapa)

        # Assert
        self.assertEqual(3, x)
        self.assertEqual(5, y)

    def test_returns_default_minus_1_cartesian_coordinates_when_pacman_is_not_in_map(self):
        # Arrange
        mapa = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|--------|",
        ]
        # Act
        x, y = find_pacman(mapa)

        # Assert
        self.assertEqual(-1, x)
        self.assertEqual(-1, y)
