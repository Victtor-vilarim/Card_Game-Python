import unittest
from modules import Player, Deck, Rank, Card, Suit
from rules import (spread, auto_discard_card, flush_check, flush, toak_check, toak)
from collections import deque
from config import INITIAL_HAND


class TestRules(unittest.TestCase):
    def test_spread(self):
        deck = Deck()
        deck.shuffle()

        players = [Player('player1'), Player('player2')]
        spread(deck, players)
        for player in players:
            self.assertEqual(len(player.hand), INITIAL_HAND)

    def test_discard_card(self):
        discard_list = [Card(Rank.KING, Suit.HEARTS), Card(Rank.ACE, Suit.DIAMONDS)]
        player = Player('name')
        player.take_card(Card(Rank.KING, Suit.CLUBS))

        auto_discard_card(discard_list, player)
        self.assertEqual(len(player.hand), 0)
        self.assertEqual(len(discard_list), 3)

    def test_flush_check(self):
        c1 = Card(Rank.JACK, Suit.CLUBS)
        c2 = Card(Rank.QUEEN, Suit.CLUBS)
        c3 = Card(Rank.KING, Suit.CLUBS)
        self.assertTrue(flush_check(c1, c2, c3))

    def test_flush_return_false(self):
        player = Player('name')
        player.hand = deque([Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES),
                             Card(Rank.NINE, Suit.HEARTS),
                             Card(Rank.EIGHT, Suit.SPADES), Card(Rank.FIVE, Suit.DIAMONDS),
                             Card(Rank.NINE, Suit.DIAMONDS), Card(Rank.FOUR, Suit.DIAMONDS),
                             Card(Rank.TEN, Suit.SPADES), Card(Rank.KING, Suit.HEARTS)])

        self.assertFalse(flush(player))

    def test_flush_return_true(self):
        player = Player('name')
        player.hand = deque([Card(Rank.SIX, Suit.DIAMONDS), Card(Rank.NINE, Suit.SPADES),
                             Card(Rank.JACK, Suit.HEARTS), Card(Rank.EIGHT, Suit.SPADES),
                             Card(Rank.FIVE, Suit.DIAMONDS), Card(Rank.QUEEN, Suit.HEARTS),
                             Card(Rank.FOUR, Suit.DIAMONDS), Card(Rank.TEN, Suit.SPADES),
                             Card(Rank.KING, Suit.HEARTS)])

        self.assertTrue(flush(player))

    def test_toak_check_true(self):
        card1 = Card(Rank.NINE, Suit.SPADES)
        card2 = Card(Rank.NINE, Suit.DIAMONDS)
        card3 = Card(Rank.NINE, Suit.HEARTS)

        self.assertTrue(toak_check(card1, card2, card3))

    def test_toak_check_false_rank(self):
        card1 = Card(Rank.EIGHT, Suit.SPADES)
        card2 = Card(Rank.NINE, Suit.DIAMONDS)
        card3 = Card(Rank.NINE, Suit.HEARTS)

        self.assertFalse(toak_check(card1, card2, card3))

    def test_toak_check_false_suit(self):
        card1 = Card(Rank.NINE, Suit.SPADES)
        card2 = Card(Rank.NINE, Suit.SPADES)
        card3 = Card(Rank.NINE, Suit.HEARTS)

        self.assertFalse(toak_check(card1, card2, card3))

    def test_toak_return_false(self):
        player = Player('name')
        player.hand = deque([Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES),
                             Card(Rank.NINE, Suit.HEARTS),
                             Card(Rank.EIGHT, Suit.SPADES), Card(Rank.FIVE, Suit.DIAMONDS),
                             Card(Rank.NINE, Suit.DIAMONDS), Card(Rank.FOUR, Suit.DIAMONDS),
                             Card(Rank.TEN, Suit.SPADES), Card(Rank.KING, Suit.HEARTS)])

        self.assertFalse(toak(player))

    def test_toak_return_true(self):
        player = Player('name')
        player.hand = deque([Card(Rank.SIX, Suit.SPADES), Card(Rank.NINE, Suit.SPADES),
                             Card(Rank.NINE, Suit.HEARTS), Card(Rank.EIGHT, Suit.SPADES),
                             Card(Rank.SIX, Suit.DIAMONDS), Card(Rank.NINE, Suit.DIAMONDS),
                             Card(Rank.EIGHT, Suit.HEARTS), Card(Rank.EIGHT, Suit.DIAMONDS),
                             Card(Rank.SIX, Suit.HEARTS)])

        self.assertTrue(toak(player))


if __name__ == '__main__':
    unittest.main()
