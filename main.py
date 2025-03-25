import random
import ru_local as ru


def create_deck():
    '''
    Function, creating and shuffling a deck of cards
    :return: deck (list)
    '''
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def calculate_hand_value(hand):
    '''
    Fuction, calculating the value of cards in hands
    :hand (list): cards in player`s and dealer`s hands
    :return: value (int)
    '''
    value = 0
    aces = 0
    for card, _ in hand:
        if card in ['Jack', 'Queen', 'King']:
            value += 10
        elif card == 'Ace':
            aces += 1
            value += 11
        else:
            value += int(card)

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


def display_hands(player_hand, dealer_hand, hide_dealer_card=True):
    '''
    Function, displaying the player's and dealer's cards on the screen
    :player_hand (list): the player's cards
    :dealer_hand (list): the dealer's cards
    :hide_dealer_card (bool): indicates whether to hide the dealer's first card
    (by default, True)
    :return: None
    '''
    print(f'{ru.PLAYER_CARDS} {player_hand} '
          f'({ru.VALUE} {calculate_hand_value(player_hand)})')
    if hide_dealer_card == True:
        print(f'{ru.DEALER_CARDS} {dealer_hand[0]}, '
              f'{ru.CLOSED_CARD}')
    else:
        print(f'{ru.DEALER_CARDS}: {dealer_hand} '
              f'({ru.VALUE} {calculate_hand_value(dealer_hand)})')


def blackjack():
    '''
    Main function.
    Function, starting the Blackjack game process
    :return: None
    '''
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        display_hands(player_hand, dealer_hand)

        if calculate_hand_value(player_hand) == 21:
            print(f'{ru.BLACKJACK_MESSAGE}')
            return

        action = input(f'{ru.CHOICE}').strip().lower()
        if action == 'hit':
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21:
                display_hands(player_hand, dealer_hand, hide_dealer_card=False)
                print(f'{ru.OVERKILL_MESSAGE}')
                return
        elif action == 'stand':
            break
        else:
            print(f'{ru.ERROR_MESSAGE}')

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    display_hands(player_hand, dealer_hand, hide_dealer_card=False)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print(f'{ru.PLAYER_WIN}')
    elif player_value < dealer_value:
        print(f'{ru.DEALER_WIN}')
    else:
        print(f'{ru.DRAW}')


if __name__ == '__main__':
    blackjack()
