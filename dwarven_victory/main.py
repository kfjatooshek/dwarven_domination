# main game loop
from dwarven_victory.character.character_logic import CreateCharacter, pick_race
from dwarven_victory.avatars import avatars_logic
from dwarven_victory.items.items_logic import pick_item
from dwarven_victory.fight.fight_logic import fight_enemy
from dwarven_victory.enemies.enemy_logic import pick_enemy


def choose_action(players_character):
    possible_actions = {1: 'look at yourself', 2: 'check your stats', 3: 'fight the enemy!',
                        4: 'create new character', 5: 'quit the game'}
    while True:
        print(f'Here are the things you can do in this world:')
        for i, action in possible_actions.items():
            print(f'{i:<10}{action:<40}')
        chosen_action = int(input("What do you want to do? Please enter the corresponding number."))
        if chosen_action == 1:
            print(players_character)
        if chosen_action == 2:
            players_character.print_stats()
        if chosen_action == 3:
            fight_enemy(players_character, pick_enemy("enemy"))
            if not is_alive(players_character):
                try_again(players_character)
        if chosen_action == 4:
            main()
        if chosen_action == 5:
            print('I hope you had a great time! See you next time!')
            break
        else:
            continue


def is_alive(player):
    if player.hp > 0:
        return True
    else:
        try_again(player)
        return False


def try_again(player):
    on_defeat = {1: "Use the ancient magic to resurrect the current character.",
                 2: "Create another character from scratch.",
                 3: "Quit the game!"}

    for i, text in on_defeat.items():
        print(f'{i:<10}{text:<50}')
    chosen_action = int(input("What do you want to do? Please enter the corresponding number."))
    if chosen_action == 1:
        player.hp = player.base_hp
        player.strength = player.base_strength
    if chosen_action == 2:
        main()
    if chosen_action == 3:
        print("Good bye, I hope you had fun!")
        quit()


def main():
    players_character = CreateCharacter(race=pick_race())

    players_character.name = str(input("Please enter your character's name: "))
    players_character.avatar = avatars_logic.pick_avatar(players_character.race)

    players_character.weapon = pick_item('weapon')
    players_character.armor = pick_item('armor')
    players_character.adjust_stats_from_items()

    print(players_character)

    choose_action(players_character)


if __name__ == "__main__":
    main()
