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
                print(f'You have won the battle against {enemy.name}, '
                      f'you earned {enemy.exp} XP and your health is restored.')
                player.exp += enemy.exp
                player.hp = player.base_hp
                break
            else:
                print(f'You got defeated by {enemy.name}')
                player.hp = 0
                break
