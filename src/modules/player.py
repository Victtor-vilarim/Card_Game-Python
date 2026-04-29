from collections import deque, defaultdict

from .card import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = deque()

    def take_card(self, card: Card) -> None:
        self.hand.append(card)

    def discard(self) -> Card:
        return self.hand.pop()

    def order_cards(self) -> None:
        self.hand = deque(sorted(self.hand, key=lambda card: card.value()))

    def filter_suit(self) -> defaultdict:
        self.order_cards()
        baseline = defaultdict(list)
        for card in self.hand:
            baseline[card.suit.value].append(card)

        return baseline

    def filter_rank(self) -> defaultdict:
        self.order_cards()
        baseline = defaultdict(list)
        for card in self.hand:
            baseline[card.value()].append(card)

        return baseline
