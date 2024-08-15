# main game loop
from character.character_logic import Character, pick_race
from avatars import avatars_logic
from items.items_logic import pick_item
from fight.fight_logic import fight_enemy
from enemies.enemy_logic import pick_enemy
from base import sleep


def choose_action(players_character: Character):
    possible_actions = {1: 'look at yourself', 2: 'check your stats', 3: 'fight the enemy!',
                        4: 'create new character', 5: 'quit the game'}
    while True:
        print(f'Here are the things you can do in this world:')
        for corresponding_number, action in possible_actions.items():
            print(f'{corresponding_number:<10}{action:<40}')
        chosen_action = int(input('What do you want to do? Please enter the corresponding number.'))
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


def is_alive(player: Character):
    if player.hp > 0:
        return True
    else:
        try_again(player)
        return False


def try_again(player: Character):
    on_defeat = {1: "Use the ancient magic to resurrect the current character.",
                 2: "Create another character from scratch.",
                 3: "Quit the game!"}

    for i, text in on_defeat.items():
        print(f'{i:<10}{text:<50}')
    chosen_action = int(input('What do you want to do? Please enter the corresponding number.'))
    if chosen_action == 1:
        player.hp = player.base_hp
        player.strength = player.base_strength
    if chosen_action == 2:
        main()
    if chosen_action == 3:
        print('Good bye, I hope you had fun!')
        quit()


def print_game_intro():
    text_lines = ['- So is it true? Is it really that bad that we have to reinforce ourselves with such mediocrity....',
                  '- Like this one, oh, here?',
                  '<The character whose physique is hidden in the dense fog seems to be talking just about you, '
                  'not hiding the disgust and derision in his voice>',
                  '- Well, since you are already here, let''s not waste more time... Every minute brings Sauron closer '
                  'to the victory',
                  '<the figure groans quietly with resignation>.',
                  'Here is how you story begins...\n\n\n']
    for line in text_lines:
        print(line)
        sleep(5)


def main():
    print_game_intro()
    player_character = Character(race=pick_race())

    player_character.name = str(input("Please enter your character's name: "))
    player_character.avatar = avatars_logic.pick_avatar(player_character.race)

    player_character.weapon = pick_item('weapon')
    player_character.armor = pick_item('armor')
    player_character.adjust_stats_from_items()

    print(player_character)

    choose_action(player_character)


if __name__ == "__main__":
    main()
