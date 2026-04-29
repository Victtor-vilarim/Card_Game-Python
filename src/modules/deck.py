from collections import deque
from random import shuffle

from config import NUMBER_OF_DECKS
from .card import Card, Rank, Suit


class Deck:
    def __init__(self):
        self.cards = deque()
        for _ in range(NUMBER_OF_DECKS):
            for suit in Suit:
                for rank in Rank:
                    self.cards.append(Card(rank, suit))

    def __len__(self):
        return len(self.cards)

    def __eq__(self, other):
        return len(self.cards) == len(other.cards)

    def __lt__(self, other):
        return len(self.cards) < len(other.cards)

    def __gt__(self, other):
        return len(self.cards) > len(other.cards)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.popleft()
