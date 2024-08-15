from dwarven_victory.base import sleep


def fight_enemy(player, enemy):
    while True:
        if player.hp > 0 and enemy.hp > 0:
            player.hp -= enemy.strength
            print(f'{enemy.name} attacks you, you took {enemy.strength} damage [{player.hp} '
                  f'out of {player.base_hp}] left!')
            sleep()
        if player.hp > 0 and enemy.hp > 0:
            enemy.hp -= player.strength
            print(f'You attack {enemy.name} and deal {player.strength} damage [{enemy.hp} '
                  f'out of {enemy.base_hp}] left!')
            sleep()
        else:
            if player.hp > 0:
                print(f'\nYou have won the battle against {enemy.name}, '
                      f'you earned {enemy.exp} XP and your health is restored.\n')
                sleep()
                player.exp += enemy.exp
                player.hp = player.base_hp
                lvl_up(player)
                break
            else:
                print(f'\nYou got defeated by {enemy.name}')
                player.hp = 0
                break


# TODO this function might be too long and too complicated actually...
# to be divided into smaller functions with one responsibility only
def lvl_up(player, base_exp_required=100):
    starting_level = player.level
    starting_strength = player.strength
    starting_hp = player.hp
    while True:
        exp_required = 0
        # this "for" loop calculates total exp required for the next level
        # player.level+2 is answering the question "does character have enough exp for the next level?"
        for i in range(1, player.level+2):
            exp_required += i*base_exp_required
        # TODO too much hardcoded stuff here, but i just needed this feature working for deployment
        if player.exp >= exp_required:
            player.level += 1
            player.strength += 100
            player.hp += 100
        else:
            if player.level > starting_level:
                levels_gained = player.level - starting_level
                strength_gained = player.strength - starting_strength
                hp_gained = player.hp - starting_hp
                print (f'Congratulations! You have reached level {player.level} [+{levels_gained}]!\n'
                       f'You have gained {strength_gained} strength [{player.strength} total] and '
                       f'{hp_gained} [{player.hp} total]!\n')
                sleep(2)
            break


