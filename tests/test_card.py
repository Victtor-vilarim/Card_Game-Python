import unittest
from modules.card import Card, Rank, Suit


class TestCard(unittest.TestCase):
    def test_card_eq(self):
        test_card = Card(Rank.ACE, Suit.DIAMONDS)
        self.assertEqual(test_card, Card(Rank.ACE, Suit.DIAMONDS))

    def test_card_less(self):
        test_card = Card(Rank.TWO, Suit.DIAMONDS)
        self.assertLess(test_card, Card(Rank.THREE, Suit.DIAMONDS))

    def test_card_greater(self):
        test_card = Card(Rank.KING, Suit.SPADES)
        self.assertGreater(test_card, Card(Rank.QUEEN, Suit.DIAMONDS))


if __name__ == '__main__':
    unittest.main()
