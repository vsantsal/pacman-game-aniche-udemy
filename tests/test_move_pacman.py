import unittest

from pacman import move_pacman, find_pacman


class MovePacmanTest(unittest.TestCase):
    def test_should_move_to_empty_space(self):
        # Arrange
        mapa = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|",
        ]
        nova_posicao_x = 4
        nova_posicao_y = 5

        # Act
        move_pacman(mapa, nova_posicao_x, nova_posicao_y)

        # Assert
        novo_x, novo_y = find_pacman(mapa)
        self.assertEqual(nova_posicao_x, novo_x)
        self.assertEqual(nova_posicao_y, novo_y)
