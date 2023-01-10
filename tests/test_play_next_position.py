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

    def test_move_is_case_insensitive(self):
        # Act
        x, y = next_position(self.mapa, 'S')

        # Assert
        self.assertEqual(self.pacman_x + 1, x)
        self.assertEqual(self.pacman_y, y)


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

    def test_when_unknown_direction_returns_false(self):
        # Act
        is_valid_play = play(self.mapa, 'b')

        # Assert
        self.assertFalse(is_valid_play)

    def test_when_direction_gets_out_of_columns_play_is_invalid(self):
        # Arrange
        mapa = [
            "|--------|",
            "|G.......@",
            "|--------|",
        ]

        # Act
        is_valid_play = play(mapa, 'd')

        # Assert
        self.assertFalse(is_valid_play)

    def test_when_direction_gets_out_of_rows_play_is_invalid(self):
        # Arrange
        mapa = [
            "|--------|",
            "|G.......|",
            "|----@---|",
        ]

        # Act
        is_valid_play = play(mapa, 's')

        # Assert
        self.assertFalse(is_valid_play)

    def test_when_direction_hits_side_wall_play_is_invalid(self):
        # Arrange
        mapa = [
            "|--------|",
            "|@......G|",
            "|--------|",
        ]

        # Act
        is_valid_play = play(mapa, 'a')

        # Assert
        self.assertFalse(is_valid_play)

    def test_when_direction_hits_horizontal_wall_play_is_invalid(self):
        # Arrange
        mapa = [
            "|--------|",
            "|@......G|",
            "|--------|",
        ]

        # Act
        is_valid_play = play(mapa, 'w')

        # Assert
        self.assertFalse(is_valid_play)
