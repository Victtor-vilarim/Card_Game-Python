import sys
from colorama import Fore, init

from config import NUMBER_OF_CARDS, NUMBER_OF_PLAYERS, NUMBER_OF_DECKS
from rules import flush_check, toak_check, flush, toak
from modules import Player, Card


def suit_group_ge_three(a: Card, b: Card, c: Card):
    if flush_check(a, b, c):
        print_three_cards(a, b, c)

    elif check_two_cards_flush(a, b):
        print_two_cards(a, b)


def rank_group_ge_three(a: Card, b: Card, c: Card):
    if toak_check(a, b, c):
        print_three_cards(a, b, c)
    elif check_two_cards_toak(a, b):
        print_two_cards(a, b)
    elif check_two_cards_toak(b, c):
        print_common_cards(a)
        print_two_cards(b, c)
    elif a != b and a != c and b != c:
        print_common_cards(a, b, c)


def check_two_cards_flush(a: Card, b: Card):
    if a.value() + 1 == b.value():
        return True
    return False


def check_two_cards_toak(a: Card, b: Card):
    if a.value() == b.value() and a.suit.value != b.suit.value:
        return True
    return False


def print_three_cards(a: Card, b: Card, c: Card):
    print(f'- {Fore.GREEN}{a}')
    print(f'- {Fore.GREEN}{b}')
    print(f'- {Fore.GREEN}{c}')


def print_two_cards(a: Card, b: Card):
    print(f'- {Fore.LIGHTYELLOW_EX}{a}')
    print(f'- {Fore.LIGHTYELLOW_EX}{b}')


def print_common_cards(*args):
    for card in args:
        print(f'- {card}')


def print_flush_hand(player: Player):
    suits = player.filter_suit()
    print('-' * 20)

    for suit in suits.values():
        a = suit[0]
        if len(suit) < 2:
            continue

        b = suit[1]
        if len(suit) == 2:
            if check_two_cards_flush(a, b):
                print_two_cards(a, b)

            continue

        c = suit[2]
        if len(suit) == 3:
            suit_group_ge_three(a, b, c)

        elif len(suit) > 3:
            for i in range(len(suit) - 2):
                card1 = suit[i]
                card2 = suit[i + 1]
                card3 = suit[i + 2]

                suit_group_ge_three(card1, card2, card3)


def print_toak_hand(player: Player):
    ranks = player.filter_rank()
    print('-' * 20)

    for rank in ranks.values():
        a = rank[0]
        if len(rank) < 2:
            print(f'- {Fore.RED}{a}')
            continue

        b = rank[1]
        if len(rank) == 2:
            if check_two_cards_toak(a, b):
                print_two_cards(a, b)
            else:
                print_common_cards(a, b)

            continue

        c = rank[2]
        if len(rank) == 3:
            rank_group_ge_three(a, b, c)

        elif len(rank) > 3:
            for i in range(len(rank) - 2):
                card1 = rank[i]
                card2 = rank[i + 1]
                card3 = rank[i + 2]
                rank_group_ge_three(card1, card2, card3)


def print_settings():
    print(f'{'-' * 5} Informações iniciais {'-' * 5}')
    print(f'Número de jogadores: {NUMBER_OF_PLAYERS}')
    print(f'Número de baralhos: {NUMBER_OF_DECKS}')
    print(f'Número de cartas: {NUMBER_OF_CARDS}')


def print_rules():
    print('-' * 20)
    print('Condição de vitória:')
    print(f'{Fore.WHITE}O jogador deverá formar 3 trios '
          'do mesmo número, mas naipes diferentes,\n'
          f'ou 3 trios de uma sequência do mesmo naipe')

    input(f'\n{Fore.LIGHTGREEN_EX}Pressione <enter> para continuar')

    print('\nPreparando o jogo:')
    print(f'{Fore.WHITE}No começo do jogo é distribuído nove cartas para cada jogador\n'
          'e se vira a carta do topo do baralho, a carta seguinte (rank) a ela\n'
          'será uma carta Coringa.\n'
          'Podendo ser usada para completar qualquer trinca.')

    input(f'\n{Fore.LIGHTGREEN_EX}Pressione <enter> para continuar')

    print('\nDinâmica de cada rodada:')
    print(f'{Fore.WHITE}A cada rodada o jogador deve pegar uma '
          'carta do baralho ou, se existir, comprar\n'
          'a carta descartada pelo adversário na vez '
          'do mesmo. O jogador pode manter a carta ou\n'
          'descartar se ela não for necessária.')


def choicer(func):
    def wrapper():
        while True:
            func()
            choice1 = input('Sua escolha: ')
            match choice1:
                case '1':
                    break
                case '2':
                    print('1 - Configurações')
                    print('2 - Regras')
                    choice2 = input('Sua escolha: ')
                    if choice2 == '1':
                        print_settings()
                    else:
                        print_rules()

                case '3':
                    sys.exit(0)

    return wrapper


@choicer
def print_initial_menu():
    print(f'{'-' * 10} Pife {'-' * 10}')
    print('1 - Jogar')
    print('2 - Opções')
    print('3 - Sair')


def print_hand_menu(player: Player):
    while True:
        print('----- Menu da rodada -----')
        print('1 - Mostrar mão em flush')
        print('2 - Mostrar mão tem Toak')
        print('3 - Jogar round')

        choice2 = input('Sua escolha: ')
        if choice2 == '1':
            print_flush_hand(player)
        elif choice2 == '2':
            print_toak_hand(player)
        else:
            break


def print_card_options(cards: tuple):
    print('---- Selecione uma opção de carta ----')
    print(f'1 - {cards[0]} do deck')
    print(f'2 - {cards[1]} do cemitério')
    print('3 - Passar vez')


def win_message(player: Player):
    if flush(player):
        print(f'O {player.name} ganhou o jogo por meio de flush!')
        print_flush_hand(player)

    elif toak(player):
        print(f'O {player.name} ganhou o jogo por meio de Toak!')
        print_toak_hand(player)


init(autoreset=True)
