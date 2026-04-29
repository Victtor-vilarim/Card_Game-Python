import unittest
from config import NUMBER_OF_CARDS
from modules.deck import Deck


class TestDeck(unittest.TestCase):
    def test_init(self):
        test_deck = Deck()
        self.assertEqual(len(test_deck), NUMBER_OF_CARDS)

    def test_eq(self):
        test_deck = Deck()
        self.assertEqual(test_deck, Deck())

    def test_shuffle_deal(self):
        test_shuffled_deck = Deck()
        test_shuffled_deck.shuffle()
        first_item_shuffled = test_shuffled_deck.deal()

        test_unshuffled_deck = Deck()
        first_item_unshuffled = test_unshuffled_deck.deal()

        self.assertNotEqual(first_item_shuffled, first_item_unshuffled)


if __name__ == '__main__':
    unittest.main()
