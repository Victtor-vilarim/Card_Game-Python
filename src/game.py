import sys
from typing import Any
from modules import Player, Deck
from rules import spread, auto_discard_card, check_win, discard_card
from utils import print_hand_menu, print_initial_menu, win_message, print_card_options
from config import INITIAL_HAND, NUMBER_OF_PLAYERS


def initialize() -> tuple[Deck, list[Player], list[Any]]:
    players: list[Player] = []
    for i in range(NUMBER_OF_PLAYERS):
        players.append(Player(f'Player {i + 1}'))

    deck = Deck()
    deck.shuffle()
    spread(deck, players)

    discard_list = []

    return deck, players, discard_list


def exe(*args):
    deck = args[0]
    players = args[1]
    discard_list = args[2]

    i = 0
    while True:
        for player in players:
            if check_win(player):
                win_message(player)
                sys.exit(0)

            print(f'----- Rodada {i + 1} - {player.name} -----')
            print_initial_menu()
            print_hand_menu(player)

            first_deck_card = deck.cards[0]
            print('Cemitério: ', *discard_list, sep=',')
            try:
                nameless_card_var = discard_list[-1]
            except IndexError:
                nameless_card_var = None

            card_options = first_deck_card, nameless_card_var

            if len(player.hand) < INITIAL_HAND + 1:
                print_card_options(card_options)
                choice = input('Qual carta deseja pegar? ')
                if choice == '1':
                    player.take_card(deck.deal())
                elif choice == '2' and nameless_card_var:
                    player.take_card(discard_list.pop())
                else:
                    discard_list.append(deck.deal())
            else:

                print('-' * 10)
                for j, card in enumerate(player.hand):
                    print(f'{j + 1} - {card}')

                choice = input('Qual carta deseja descartar? ')
                if choice.strip().isdigit() and choice != '0':
                    try:
                        discard_card(discard_list, player, int(choice) - 1)
                    except IndexError:
                        print('Valor inválido')
                        print('Descarte automático...')
                        auto_discard_card(discard_list, player)
                else:
                    print('Valor inválido')
                    print('Descarte automático...')
                    auto_discard_card(discard_list, player)

        i += 1
