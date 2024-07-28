# main game loop
from dwarven_victory.character.character import DwarvenCharacter, ElvenCharacter
from dwarven_victory.avatars import avatars_logic
from dwarven_victory.character import character_stats_dict
from dwarven_victory.character.character_logic import pick_race


def main():
    players_race = pick_race()

    character_name = str(input("Please enter your character's name: "))

    players_avatar = avatars_logic.pick_avatar(players_race)

    if players_race == "dwarf":
        players_character = DwarvenCharacter(name=character_name, race=players_race, avatar=players_avatar )
    if players_race == "elf":
        players_character = ElvenCharacter(name=character_name, race=players_race, avatar=players_avatar)

    print(players_character)


if __name__ == "__main__":
    main()
