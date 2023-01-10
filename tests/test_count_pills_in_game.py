import unittest

from pacman import total_pills


class TotalPillsTest(unittest.TestCase):
    def test_counts_zero_when_no_pill_in_game(self):
        # Arrange
        mapa = ["|--------|"]

        # Act
        pills_obtidas = total_pills(mapa)

        # Assert
        self.assertEqual(0, pills_obtidas)

    def test_counts_greater_than_zero_when_some_pill_in_game(self):
        # Arrange
        mapa = ["|-----P--|"]

        # Act
        pills_obtidas = total_pills(mapa)

        # Assert
        self.assertEqual(1, pills_obtidas)
