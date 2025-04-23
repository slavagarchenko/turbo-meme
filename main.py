#Case5
#Creators: Garchenko Vyacheslav, Gaberman Artem


import random
import ru_local as ru

character_descriptions = f"""
Доступные персонажи и их характеристики:
1. {ru.WARRIOR} (Воин): Высокий урон в ближнем бою, использует способность наносить один мощный и сильный удар.
2. {ru.MAGE} (Маг): Специалист по магии, может лечить себя и наносить урон.
3. {ru.ARCHER} (Лучник): Быстрый и точный, его способность наносить двойной урон.
4. {ru.VALKYRIE} (Valkyrie): Наносит урон всем противникам одновременно.
5. {ru.BERSERK} (Berserk): Урон увеличивается при снижении здоровья, может наносить большой урон и восстанавливаться.
"""

def create_player(name, player_class):
    '''
    Создает игрока с именем, классом и начальным здоровьем.
    '''
    return {
        'name': name,
        'health': 100,
        'player_class': player_class,
        'special_ability_used': False
    }

def attack(player, target):
    '''
    Выполняет атаку, уменьшая здоровье цели.
    '''
    if player['player_class'] == 'Warrior':
        damage = random.randint(15, 25)
    elif player['player_class'] == 'Archer':
        damage = random.randint(10, 25)
    else:
        damage = random.randint(10, 30)
    target['health'] -= damage
    if target['health'] < 0:
        target['health'] = 0
    return damage

def use_special_ability(player, target=None, players=None):
    '''
    Использует специальную способность в зависимости от класса.
    '''
    if player['special_ability_used']:
        print(f'{player["name"]} {ru.NO_ABILITY}')
        return 0

    if player['player_class'] == 'Valkyrie':
        damage = random.randint(20, 35)
        for p in players:
            if p != player and p['health'] > 0:
                p['health'] -= damage
                if p['health'] < 0:
                    p['health'] = 0
                print(f'{p["name"]} {ru.HP} {p["health"]}')
        player['special_ability_used'] = True
        return damage

    elif player['player_class'] == 'Berserk':
        damage = random.randint(20, 40)  # Диапазон урона

        target and target['health'] > 0
        target['health'] -= damage
        heal_amount = int(0.4 * damage)
        player['health'] += heal_amount
        if player['health'] > 100:
            player['health'] = 100
        player['special_ability_used'] = True
        return damage

    elif player['player_class'] == 'Warrior':
        damage = random.randint(25, 40)
        target['health'] -= damage
        if target['health'] < 0:
            target['health'] = 0
        player['special_ability_used'] = True
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
        if target['health'] < 0:
            target['health'] = 0
        player['special_ability_used'] = True
        return damage

    else:
        return 0

def heal(player):
    '''
    Восстанавливает здоровье игрока.
    '''
    heal_amount = random.randint(15, 25)
    player['health'] += heal_amount
    if player['health'] > 100:
        player['health'] = 100
    return heal_amount

def main():
    '''
    Основной цикл игры.
    '''
    print(f'{ru.GREETING}')
    print(character_descriptions)

    players = []

    for i in range(1, 4):
        name = input(f'{ru.NAME} {i}: ')

        player_class = ''
        while True:
            player_class_russian = input(
                f'{ru.PLAYER_CLASS} {name} '
                f'({ru.WARRIOR}, {ru.MAGE}, {ru.ARCHER}, {ru.VALKYRIE}, {ru.BERSERK}): '
            ).lower()

            if player_class_russian == ru.WARRIOR.lower():
                player_class = 'Warrior'
                break
            elif player_class_russian == ru.MAGE.lower():
                player_class = 'Mage'
                break
            elif player_class_russian == ru.ARCHER.lower():
                player_class = 'Archer'
                break
            elif player_class_russian == ru.VALKYRIE.lower():
                player_class = 'Valkyrie'
                break
            elif player_class_russian == ru.BERSERK.lower():
                player_class = 'Berserk'
                break
            else:
                print(f'{ru.CLASS_ERROR}')

        players.append(create_player(name, player_class))

    while len([p for p in players if p['health'] > 0]) > 1:
        for player in players:
            if player['health'] > 0:
                print(f'\n{ru.PLAYERS_HEALTH}:')
                for p in players:
                    print(f"{p['name']} ({p['player_class']}): {p['health']} {ru.HP}")

                print(f'\n{player["name"]}, {ru.MOTION}')
                action = input(f'{ru.ACTION}')

                if action == '1':
                    target_index = int(input(f'{ru.TARGET}')) - 1
                    target = players[target_index]
                    while target == player or target['health'] <= 0:
                        print(f'{ru.TARGET_ERROR}')
                        target_index = int(input(f'{ru.TARGET}')) - 1
                        target = players[target_index]
                    damage = attack(player, target)
                    print(f'{player["name"]} {ru.ATTACK} {target["name"]} {ru.CONJUNCTION} {ru.DAMAGE} {damage} {ru.HP}')

                elif action == '2':
                    if player['player_class'] == 'Valkyrie':
                        ability_result = use_special_ability(player, players=players)
                        print(f'{player["name"]} {ru.SPECIAL_OPPORTUNITY} {ru.CONJUNCTION} {ru.DAMAGE} {ability_result} всех персонажей')
                    else:
                        print(f'{ru.ABILITY_TARGET}')
                        for idx, p in enumerate(players):
                            if p != player and p['health'] > 0:
                                print(f'{idx + 1}: {p["name"]} ({p["player_class"]})')
                        target_index = int(input(f'{ru.ABILITY_TARGET}')) - 1
                        target = players[target_index]
                        ability_result = use_special_ability(player, target, players)
                        print(f'{player["name"]} {ru.SPECIAL_OPPORTUNITY} {ru.CONJUNCTION} {ru.DAMAGE} {ability_result} {ru.HP} {target["name"]}')

                elif action == '3':
                    heal_amount = heal(player)
                    print(f'{player["name"]} {ru.HEALING} {heal_amount} {ru.HP}')

                if 'target' in locals() and target['health'] <= 0:
                    print(f'{target["name"]} {ru.DEATH_MESSAGE}')
                    players.remove(target)

    winner = players[0]
    print(f'\n{ru.CONGRATULATION} {winner["name"]} {ru.WINNER_MESSAGE} {winner["health"]} {ru.HP}')

if __name__ == "__main__":
    main()
