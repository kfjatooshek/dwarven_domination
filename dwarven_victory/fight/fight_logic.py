from dwarven_victory.base import sleep


def fight_enemy(player, enemy):
    while True:
        if player.hp > 0 and enemy.hp > 0:
            player.hp -= enemy.strength
            print(f'Enemy {enemy.name} attacks you, you took {enemy.strength} damage [{player.hp} '
                  f'out of {player.base_hp}] left!')
            sleep()
            enemy.hp -= player.strength
            print(f'You attack {enemy.name} and deal {player.strength} damage [{enemy.hp} '
                  f'out of {enemy.base_hp}] left!')
            sleep()
        else:
            if player.hp > 0:
                print(f'You have won the fight with {enemy.name}, '
                      f'you earned {enemy.exp} XP and your health is restored.')
                player.exp += enemy.exp
                player.hp = player.base_hp
                break
            else:
                print(f'You got defeated by {enemy.name}')
                try_again(player)
                break



on_defeat = {1: "Use the ancient magic to resurrect the current character",
             2: "Create another character from the beginning.",
             3: "Quit the game!"}


def try_again(player):
    for i, text in on_defeat.items():
        print(f'{i:<10}{text:>20}')
    chosen_action = int(input("What do you want to do? Please enter the corresponding number."))
    if chosen_action == 1:
        player.hp = player.base_hp
        player.strength = player.base_strength
    if chosen_action == 2:
        pass
    if chosen_action == 3:
        print("Good bye, I hope you had fun!")
        quit()


