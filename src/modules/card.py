from enum import Enum
from typing import NamedTuple
from functools import total_ordering

from config import ACE_VALUE


class Rank(Enum):
    ACE = ACE_VALUE
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Suit(Enum):
    CLUBS = 'Club'
    HEARTS = 'Heart'
    SPADES = 'Spades'
    DIAMONDS = 'Diamonds'


@total_ordering
class Card(NamedTuple):
    rank: Rank
    suit: Suit

    def value(self):
        return self.rank.value

    def __repr__(self) -> str:
        return f'{self.rank.name} of {self.suit.value}'

    def __eq__(self, other) -> bool:
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other) -> bool:
        if self.value() != other.value():
            return self.value() < other.value()

        return len(self.suit.value) < len(other.suit.value)

    def __gt__(self, other) -> bool:
        if self.value() != other.value():
            return self.value() > other.value()

        return len(self.suit.value) > len(other.suit.value)
