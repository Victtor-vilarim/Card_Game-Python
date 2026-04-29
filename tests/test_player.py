from modules import Player
from modules import Card, Rank, Suit
import unittest
from collections import deque, defaultdict


class TestPlayer(unittest.TestCase):
    def test_init(self):
        test_player = Player('name')
        test_player.hand.append(Card(Rank.ACE, Suit.SPADES))
        test_player.hand.append(Card(Rank.KING, Suit.CLUBS))
        self.assertEqual(test_player.hand, deque([Card(Rank.ACE, Suit.SPADES), Card(Rank.KING, Suit.CLUBS)]))

    def test_take_card(self):
        test_player = Player('name')
        test_player.take_card(Card(Rank.ACE, Suit.CLUBS))

        self.assertIn(Card(Rank.ACE, Suit.CLUBS), test_player.hand)

    def test_discard(self):
        test_player = Player('name')
        test_player.take_card(Card(Rank.ACE, Suit.HEARTS))
        self.assertEqual(test_player.discard(), Card(Rank.ACE, Suit.HEARTS))

    def test_order_cards(self):
        test_player = Player('name')
        test_player.take_card(Card(Rank.KING, Suit.CLUBS))
        test_player.take_card(Card(Rank.QUEEN, Suit.DIAMONDS))
        test_player.take_card(Card(Rank.ACE, Suit.HEARTS))
        test_player.order_cards()

        self.assertEqual(Card(Rank.KING, Suit.CLUBS), test_player.hand.pop())

    def test_filter_suit_return(self):
        player = Player('name')
        player.hand = deque([Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES),
                             Card(Rank.NINE, Suit.HEARTS),
                             Card(Rank.EIGHT, Suit.SPADES), Card(Rank.FIVE, Suit.DIAMONDS),
                             Card(Rank.NINE, Suit.DIAMONDS), Card(Rank.FOUR, Suit.DIAMONDS),
                             Card(Rank.TEN, Suit.SPADES), Card(Rank.KING, Suit.HEARTS)])

        self.assertIsInstance(player.filter_suit(), defaultdict)

    def test_filter_suit_len(self):
        player = Player('name')
        player.hand = deque([Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES),
                             Card(Rank.NINE, Suit.HEARTS),
                             Card(Rank.EIGHT, Suit.SPADES), Card(Rank.FIVE, Suit.DIAMONDS),
                             Card(Rank.NINE, Suit.DIAMONDS), Card(Rank.FOUR, Suit.DIAMONDS),
                             Card(Rank.TEN, Suit.SPADES), Card(Rank.KING, Suit.HEARTS)])

        self.assertEqual(len(player.filter_suit()), 3)

    def test_filter_rank_return(self):
        player = Player('name')
        player.hand = deque([Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES),
                             Card(Rank.NINE, Suit.HEARTS),
                             Card(Rank.EIGHT, Suit.SPADES), Card(Rank.FIVE, Suit.DIAMONDS),
                             Card(Rank.NINE, Suit.DIAMONDS), Card(Rank.FOUR, Suit.DIAMONDS),
                             Card(Rank.TEN, Suit.SPADES), Card(Rank.KING, Suit.HEARTS)])

        self.assertIsInstance(player.filter_rank(), defaultdict)

    def test_filter_rank_len(self):
        player = Player('name')
        player.hand = deque([Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES),
                             Card(Rank.NINE, Suit.HEARTS),
                             Card(Rank.EIGHT, Suit.SPADES), Card(Rank.FIVE, Suit.DIAMONDS),
                             Card(Rank.NINE, Suit.DIAMONDS), Card(Rank.FOUR, Suit.DIAMONDS),
                             Card(Rank.TEN, Suit.SPADES), Card(Rank.KING, Suit.HEARTS)])

        self.assertEqual(len(player.filter_rank().keys()), 7)


if __name__ == '__main__':
    unittest.main()
