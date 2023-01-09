import unittest

from pacman import next_position, find_pacman, play


class NextPositionTest(unittest.TestCase):
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
        x, y = next_position(self.mapa, 'd')

        # Assert
        self.assertEqual(self.pacman_x, x)
        self.assertEqual(self.pacman_y + 1, y)

    def test_move_to_the_left(self):
        # Act
        x, y = next_position(self.mapa, 'a')

        # Assert
        self.assertEqual(self.pacman_x, x)
        self.assertEqual(self.pacman_y - 1, y)

    def test_move_up(self):
        # Act
        x, y = next_position(self.mapa, 'w')

        # Assert
        self.assertEqual(self.pacman_x - 1, x)
        self.assertEqual(self.pacman_y, y)

    def test_move_down(self):
        # Act
        x, y = next_position(self.mapa, 's')

        # Assert
        self.assertEqual(self.pacman_x + 1, x)
        self.assertEqual(self.pacman_y, y)

    def test_move_to_unknow_key_raises_value_error(self):
        with self.assertRaises(ValueError) as contexto:
            next_position(self.mapa, 'b')
        self.assertEqual("Direção 'b' não reconhecida",
                         contexto.exception.args[0])


class PlayPacmanTest(unittest.TestCase):
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
        play(self.mapa, 'd')

        # Assert
        x, y = find_pacman(self.mapa)
        self.assertEqual(self.pacman_x, x)
        self.assertEqual(self.pacman_y + 1, y)

    def test_move_to_the_left(self):
        # Act
        play(self.mapa, 'a')

        # Assert
        x, y = find_pacman(self.mapa)
        self.assertEqual(self.pacman_x, x)
        self.assertEqual(self.pacman_y - 1, y)

    def test_move_up(self):
        # Act
        play(self.mapa, 'w')

        # Assert
        x, y = find_pacman(self.mapa)
        self.assertEqual(self.pacman_x - 1, x)
        self.assertEqual(self.pacman_y, y)

    def test_move_down(self):
        # Act
        play(self.mapa, 's')

        # Assert
        x, y = find_pacman(self.mapa)
        self.assertEqual(self.pacman_x + 1, x)
        self.assertEqual(self.pacman_y, y)
