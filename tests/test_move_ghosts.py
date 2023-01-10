import unittest

from pacman import move_ghosts, find_ghosts


class MoveGhostsTest(unittest.TestCase):
    def test_when_no_ghosts_in_map_nothing_changes(self):
        # Arrange
        mapa = [
            "|--------|",
            "|....@.|.|",
            "|........|",
            "|--------|",
        ]
        # Act
        move_ghosts(mapa)

        # Assert
        self.assertEqual(0, len(find_ghosts(mapa)))

    def test_when_one_ghost_unconstrained_in_map_count_does_not_increase_and_ghost_moves(self):
        # Arrange
        mapa = [
            "|--------|",
            "|........|",
            "|...G..|.|",
            "|........|",
            "|--------|",
        ]
        ghosts_before = find_ghosts(mapa)

        # Act
        move_ghosts(mapa)
        ghosts_after = find_ghosts(mapa)

        # Assert
        self.assertEqual(1, len(ghosts_after))
        self.assertNotEqual(ghosts_before[0], ghosts_after[0])

    def test_when_ghost_hits_wall_ghost_does_not_move(self):
        # Arrange
        mapa = [
            "|---|",
            "|-G-|",
            "|---|",
        ]
        ghosts_before = find_ghosts(mapa)

        # Act
        move_ghosts(mapa)
        ghosts_after = find_ghosts(mapa)

        # Assert
        self.assertEqual(1, len(ghosts_after))
        self.assertEqual(ghosts_before[0], ghosts_after[0])

    def test_when_ghost_hits_other_ghost_does_not_move(self):
        # Arrange
        mapa = [
            "G",
            "G",
        ]
        ghosts_before = find_ghosts(mapa)

        # Act
        move_ghosts(mapa)
        ghosts_after = find_ghosts(mapa)

        # Assert
        self.assertEqual(len(ghosts_before), len(ghosts_after))
        self.assertEqual(ghosts_before[0], ghosts_after[0])

    def test_when_ghost_hits_pill_does_not_move(self):
        # Arrange
        mapa = [
            "|PPP|",
            "|PGP|",
            "|PPP|",
        ]
        ghosts_before = find_ghosts(mapa)

        # Act
        move_ghosts(mapa)
        ghosts_after = find_ghosts(mapa)

        # Assert
        self.assertEqual(len(ghosts_before), len(ghosts_after))
        self.assertEqual(ghosts_before[0], ghosts_after[0])

    def test_when_hits_pacman_hero_dies(self):
        # Arrange
        mapa = [
            "|@@@|",
            "|@G@|",
            "|@@@|",
        ]
        ghosts_before = find_ghosts(mapa)

        # Act
        pacman_was_hit = move_ghosts(mapa)
        ghosts_after = find_ghosts(mapa)

        # Assert
        self.assertEqual(len(ghosts_before), len(ghosts_after))
        self.assertEqual(ghosts_before[0], ghosts_after[0])
        self.assertTrue(pacman_was_hit)
