import unittest

from pacman import find_ghosts


class FindGhostsTest(unittest.TestCase):
    def test_returns_correct_cartesian_coordinates_when_only_one_ghost_map(self):
        # Arrange
        mapa = [
            "|--------|",
            "|G...@.|.|",
            "|........|",
            "|--------|",
        ]
        # Act
        ghosts = find_ghosts(mapa)

        # Assert
        self.assertEqual(1, len(ghosts))
        self.assertIn((1, 1), ghosts)

    def test_returns_empty_list_when_no_ghost_in_map(self):
        # Arrange
        mapa = [
            "|--------|",
            "|....@.|.|",
            "|........|",
            "|--------|",
        ]
        # Act
        ghosts = find_ghosts(mapa)

        # Assert
        self.assertEqual(0, len(ghosts))
