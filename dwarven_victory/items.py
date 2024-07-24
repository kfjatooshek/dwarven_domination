import time


def time_sleep(sleep_time=1):
    time.sleep(sleep_time)


weapons = [
    {'name': "Heavy Two-handed War hammer", 'strength': 250, 'avatar':  r"""
 _______
|_______|
   ||
   ||
   ||
   ||
   ||
   ||
   ||
"""},
    {'name': "Sharp and shiny sword", 'strength': 150, 'avatar': r"""
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
"""},
    {'name': "Runic Axe of ancestors", 'strength': 500, 'avatar': r"""
  _____
 /     \
/_______\
 \  ||
  \ ||
   \||
    ||
    ||
    ||
"""}]


def pick_weapon():
    print(f"Here is the list of available weapons:")

    for index, item in enumerate(weapons, 1):
        print(f'{'Number:':<20}{index:<10}\n{'Weapon:':<20}{item['name']:^10}\n{'Strength:':<20}{item['strength']}\n'
              f'{item['avatar']}\n\n\n')
        time_sleep()

    chosen_weapon = int(input("Please choose your weapon by typing the corresponding number:\n"))-1
    print(f'You have just drawn the weapon of your choice: {weapons[chosen_weapon]['name']}\n\n'
          f'{weapons[chosen_weapon]['avatar']}')

    weapon_graphics = weapons[chosen_weapon]['avatar']
    weapon_str = weapons[chosen_weapon]['strength']
    weapon_name = weapons[chosen_weapon]['name']
    return weapon_graphics, weapon_str, weapon_name
