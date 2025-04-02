import random
import ru_local as ru

def create_player(name, player_class):
    '''
    Function creates a player with name, class, and initial health values.
    :name (str): player's name
    :player_class (str): player's class from the list ('Warrior', 'Mage', 'Archer')
    :return: dictionary with player information
    '''
    return {
        'name': name,
        'health': 100,
        'player_class': player_class,
        'special_ability_used': False,
        'abilities_blocked': False
    }

def attack(player, target):
    '''
    Function performs an attack on another player, reducing their health.
    :player (dict): the attacking player
    :target (dict): the target player
    :return: damage (int): the amount of damage inflicted on the target.
    '''

    if player['player_class'] == 'Warrior':
        damage = random.randint(15, 25)

    elif player['player_class'] == 'Archer':
        damage = random.randint(10, 25)

    else:
        damage = random.randint(10, 30)

    target['health'] -= damage
    return damage

def use_special_ability(player, target=None):
    '''
    Function uses the special ability of the player.
    :player (dict): the player using the ability
    :target (dict, optional): target for a special ability (default None)
    :return: damage (int) or heal_amount (int): depending on the player's class
    '''
    if player['special_ability_used']:
        print(f'{player['name']} {ru.NO_ABILITY}')
        return 0

    if player['abilities_blocked']:
        print(f'{player['name']} {ru.ABILITY_BLOCKED}')
        return 0

    if target == player:
        print(f'{player['name']} {ru.ABILITY_ERROR}')
        return 0

    if player['player_class'] == 'Warrior':
        damage = random.randint(25, 40)
        target['health'] -= damage
        player['special_ability_used'] = True

        for p in players:
            if p != player:
                p['abilities_blocked'] = True
        return damage

    elif player['player_class'] == 'Mage':
        heal_amount = random.randint(30, 50)
        player['health'] += heal_amount

        if player['health'] > 100:
            player['health'] = 100
        player['special_ability_used'] = True
        return heal_amount

    elif player['player_class'] == 'Archer':
        damage = random.randint(15, 30)
        target['health'] -= damage * 2
        player['special_ability_used'] = True
        return damage

def heal(player):
    '''
    Function restores the player's health.
    :player (dict): the player to heal
    :return: heal_amount (int): the amount of health restored
    '''
    heal_amount = random.randint(15, 25)
    player['health'] += heal_amount

    if player['health'] > 100:
        player['health'] = 100

    return heal_amount

def main():
    '''
    Main function.
    :return: None
    '''
    print(f'{ru.GREETING}')

    players = []

    for i in range(1, 4):
        name = input(f'{ru.NAME} {i}: ')
        player_class = ''

        while True:
            player_class_russian = input(
                f'{ru.PLAYER_CLASS} {name} '
                f'({ru.WARRIOR}, {ru.MAGE}, {ru.ARCHER}): ')
            player_class_russian = player_class_russian.lower()

            if player_class_russian == ru.WARRIOR:
                player_class = 'Warrior'
                break
            elif player_class_russian == ru.MAGE:
                player_class = 'Mage'
                break
            elif player_class_russian == ru.ARCHER:
                player_class = 'Archer'
                break
            else:
                print(f'{ru.CLASS_ERROR}')

        players.append(create_player(name, player_class))

    while len(players) > 1:

        for player in players:

            for p in players:

                if p['health'] > 0:
                    p['abilities_blocked'] = False

            if player['health'] > 0:
                print(f'\n{ru.PLATERS_HEALTH}: ')

                for p in players:
                    print(f'{p['name']} ({p['player_class']}): {p['health']}')

                print(f'\n{player['name']}, {ru.MOTION}')
                action = input(f'{ru.ACTION}')

                if action == '1':
                    print(f'{ru.TARGET}')

                    for idx, target in enumerate(players):

                        if target != player and target['health'] > 0:
                            print(f'{idx + 1}: {target['name']} '
                                  f'({target['player_class']})')

                    target_index = int(input(f'{ru.TARGET}')) - 1
                    target = players[target_index]

                    while target == player or target['health'] <= 0:
                        print(f'{ru.TARGET_ERROR}')
                        target_index = int(input(f'{ru.TARGET}')) - 1
                        target = players[target_index]

                    damage = attack(player, target)
                    print(f'{player['name']} {ru.ATTACK} {target['name']} '
                          f'{ru.CONJUNCTION} {ru.DAMAGE} '
                          f'{damage} {ru.HP}')

                elif action == '2':

                    if player['player_class'] == 'Mage':
                        ability_result = use_special_ability(player)
                        print(f'{player['name']} {ru.SPECIAL_OPPORTUNITY} '
                              f'{ru.CONJUNCTION} {ru.HEALING} '
                              f'{ability_result} {ru.HP}')

                    else:
                        print(f'{ru.ABILITY_TARGET}')

                        for idx, target in enumerate(players):
                            if target != player and target['health'] > 0:
                                print(f'{idx + 1}: {target['name']} '
                                      f'({target['player_class']})')

                        target_index = int(input(f'{ru.ABILITY_TARGET}')) - 1
                        target = players[target_index]
                        ability_result = use_special_ability(player, target)

                        if player['player_class'] == 'Warrior':
                            print(f'{player['name']} {ru.SPECIAL_OPPORTUNITY}'
                                  f' {ru.CONJUNCTION} {ru.DAMAGE} '
                                  f'{ability_result} {ru.HP}')

                        elif player['player_class'] == 'Archer':
                            print(f'{player['name']} {ru.SPECIAL_OPPORTUNITY}'
                                  f' {ru.CONJUNCTION} {ru.DAMAGE} '
                                  f'{ability_result} {ru.HP}')

                elif action == '3':
                    heal_amount = heal(player)
                    print(f'{player['name']} {ru.HEALING} '
                          f'{heal_amount} {ru.HP}')

                if target['health'] <= 0:
                    print(f'{target['name']} {ru.DEATH_MESSAGE}')
                    players.remove(target)

    winner = players[0]

    print(f'\n{ru.CONGRATULATION} {winner['name']} '
          f'{ru.WINNER_MESSAGE} {winner['health']} {ru.HP}')

if __name__ == "__main__":
    main()
