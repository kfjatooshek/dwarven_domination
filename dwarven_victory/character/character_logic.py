from dwarven_victory.character import character_stats_dict


def pick_race():
    available_races = character_stats_dict.race_attributes.keys()

    print("Here is the list of character's races available")
    for k, v in enumerate(available_races, 1):
        print(f'{k:<10}{v:<10}')
    available_races_list = list(available_races)
    players_race_number = int(input("Please enter the corresponding number to select your character's race: ")) - 1
    players_race = available_races_list[players_race_number]

    return players_race
