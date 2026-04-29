from collections import defaultdict

from config import INITIAL_HAND
from modules import Deck, Player, Card


# Preparação
def spread(deck: Deck, players: list[Player]) -> None:
    for _ in range(INITIAL_HAND):
        for player in players:
            player.take_card(deck.deal())


# Dinâmica
def discard_card(discard_list: list, player: Player, index: int) -> int:
    start = 0
    end = len(player.hand) - 1

    while start < end + 1:
        mid = (start + end) // 2

        if player.hand[mid].value() == player.hand[index].value():
            card = player.hand[index]
            player.hand.remove(card)
            discard_list.append(card)
            return 1

        if player.hand[mid].value() < player.hand[index].value():
            start = mid + 1
        elif player.hand[mid].value() > player.hand[index].value():
            end = mid - 1

    return 0


def auto_discard_card(discard_list: list[Card], player: Player) -> None:
    discard_list.append(player.discard())


# condição de vitória
def flush_check(c1: Card, c2: Card, c3: Card) -> bool:
    if c2.value() == c1.value() + 1 and c3.value() == c2.value() + 1:
        if c1.suit.value == c2.suit.value == c3.suit.value:
            return True
    return False


def toak_check(c1: Card, c2: Card, c3: Card) -> bool:
    if c1.value() == c2.value() == c3.value():
        if c1.suit.value != c2.suit.value and c1.suit.value != c3.suit.value and c2.suit.value != c3.suit.value:
            return True
    return False


def flush(player: Player) -> bool:
    suits = player.filter_suit()
    filtered_suit = defaultdict(tuple)
    repeated_suits = set()

    for suit in suits.values():
        for i in range(len(suit) - 2):
            a, b, c = suit[i], suit[i + 1], suit[i + 2]
            if flush_check(a, b, c):
                if a not in repeated_suits:
                    repeated_suits.add(b)
                    repeated_suits.add(c)
                    filtered_suit[a.suit.value, a.value(), b.value(), c.value()] = (a, b, c)

    if len(filtered_suit.values()) == 3:
        return True
    return False


def toak(player: Player) -> bool:
    ranks = player.filter_rank()
    filtered_rank = defaultdict(tuple)
    repeated_ranks = set()

    for rank in ranks.values():
        for i in range(len(rank) - 2):
            a, b, c = rank[i], rank[i + 1], rank[i + 2]
            if toak_check(a, b, c):
                if a not in repeated_ranks and b not in repeated_ranks and c not in repeated_ranks:
                    repeated_ranks.add(a)
                    repeated_ranks.add(b)
                    repeated_ranks.add(c)
                    filtered_rank[a.value(), a.suit.value, b.suit.value, c.suit.value] = (a, b, c)

    if len(filtered_rank.values()) == 3:
        return True
    return False


def check_win(player: Player) -> bool:
    if flush(player):
        return True
    if toak(player):
        return True
    return False
