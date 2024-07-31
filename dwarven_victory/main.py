# main game loop
from dwarven_victory.character.character_logic import DwarvenCharacter, ElvenCharacter, pick_race
from dwarven_victory.avatars import avatars_logic
from dwarven_victory.items.items_logic import pick_item


def main():
    character_race = pick_race()
    character_name = str(input("Please enter your character's name: "))
    character_avatar = avatars_logic.pick_avatar(character_race)

    players_character = None
    if character_race == "dwarf":
        players_character = DwarvenCharacter()
    if character_race == "elf":
        players_character = ElvenCharacter()

    players_character.name = character_name
    players_character.avatar = character_avatar

    players_character.weapon = pick_item('weapon')
    players_character.armor = pick_item('armor')
    players_character.adjust_stats_from_items()

    print(players_character)


if __name__ == "__main__":
    main()
