import time


def time_sleep(sleep_time=1):
    time.sleep(sleep_time)


def weapons():
    return [(250, 1, "Heavy Two-handed War hammer", r"""
 _______
|_______|
   ||
   ||
   ||
   ||
   ||
   ||
   ||
"""),
            (150, 2,  "Sharp and shiny sword", r"""
    /\
   /  \
  /    \
 /      \
/________\
    ||
    ||
    ||
    ||
  /____\
"""),
            (500, 3,  "Runic Axe of ancestors", r"""
  _____
 /     \
/_______\
 \  ||
  \ ||
   \||
    ||
    ||
    ||
""")]


def pick_weapon():
    print(f"Here is the list of available weapons:")

    for h, i, j, k in weapons():
        print(f'{'Number:':<20}{i:^10}\n{'Avatar name:':<20}{j:^10}\n{k}\n\n\n')
        time_sleep()

    chosen_weapon = int(input("Please choose your weapon by typing the corresponding number:\n"))-1
    print(f'You have just drawn the weapon of your choice:{weapons()[chosen_weapon][3]}')
    weapon_graphics = weapons()[chosen_weapon][3]
    weapon_str = weapons()[chosen_weapon][0]
    weapon_name = weapons()[chosen_weapon][2]
    return weapon_graphics, weapon_str, weapon_name

