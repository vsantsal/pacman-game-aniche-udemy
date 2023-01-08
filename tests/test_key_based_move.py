import unittest

from pacman import next_position, find_pacman


class KeyBasedPacmanMoveTest(unittest.TestCase):
    def setUp(self) -> None:
        # Arrange
        self.mapa = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|",
        ]
        self.pacman_x = 3
        self.pacman_y = 5

    def test_move_to_the_right(self):
        # Act
        next_position(self.mapa, 'd')

        # Assert
        x, y = find_pacman(self.mapa)
        self.assertEqual(self.pacman_x, x)
        self.assertEqual(self.pacman_y + 1, y)

    def test_move_to_the_left(self):
        # Act
        next_position(self.mapa, 'a')

        # Assert
        x, y = find_pacman(self.mapa)
        self.assertEqual(self.pacman_x, x)
        self.assertEqual(self.pacman_y - 1, y)

    def test_move_up(self):
        # Act
        next_position(self.mapa, 'w')

        # Assert
        x, y = find_pacman(self.mapa)
        self.assertEqual(self.pacman_x - 1, x)
        self.assertEqual(self.pacman_y, y)

    def test_move_down(self):
        # Act
        next_position(self.mapa, 's')

        # Assert
        x, y = find_pacman(self.mapa)
        self.assertEqual(self.pacman_x + 1, x)
        self.assertEqual(self.pacman_y, y)
