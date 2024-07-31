import items_design
import time
from dwarven_victory.base import GameObject


def sleep(sleep_time=1):
    time.sleep(sleep_time)


class Weapon(GameObject):
    def __init__(self, item_type: str = None, name: str = "Broken Sword"):
        super().__init__(name=name)
        self.item_type = item_type

    def pick_weapon(self, item_type: str):
        print(f"Here is the list of available {item_type}s:")
        items = items_design.items().get(item_type)
        for index, item in enumerate(items, 1):
            print(f'{'Number:':<20}{index:<10}\n{'Weapon:':<20}{item['name']:^10}\n{'Strength:':<20}{item['strength']}\n'
                  f'{item['avatar']}\n\n\n')
            sleep()

        chosen_weapon = int(input("Please choose your weapon by typing the corresponding number:\n"))-1
        print(f'You have just drawn the weapon of your choice: {weapons[chosen_weapon]['name']}\n\n'
              f'{weapons[chosen_weapon]['avatar']}')

        weapon_graphics = weapons[chosen_weapon]['avatar']
        weapon_str = weapons[chosen_weapon]['strength']
        weapon_name = weapons[chosen_weapon]['name']
        return weapon_graphics, weapon_str, weapon_name

    def update_stats(self):
        pass


x = Weapon()
print(x)


