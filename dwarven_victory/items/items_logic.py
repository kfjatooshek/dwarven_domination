import time
import dwarven_victory.items.item_stats_dict as items_design
from dwarven_victory.base import GameObject


def sleep(sleep_time=1):
    time.sleep(sleep_time)


class Item(GameObject):
    def __init__(self, obj_type: str = None, hp: int = 0, strength: int = 0, avatar: str = None, name: str = None):
        super().__init__(obj_type=obj_type, hp=hp, strength=strength, avatar=avatar, name=name)

    def __str__(self):
        return (f"{'Name: ':<30}{self.name:>20}\n"
                f"{'HP: ':<30}{self.hp:>20}\n"
                f"{'Strength: ':<30}{self.strength:>20}\n"
                f"{f'This is your {self.obj_type}:':<30}{self.avatar}\n\n")


def pick_item(obj_type):
    obj_type_list = items_design.items_avatar_dict.get(obj_type)
    print(f"Here is the list of available {obj_type}s:")

    for i, (element, avatar) in enumerate(obj_type_list.items(), 1):
        print(f'{'Number:':<20}{i:<10}\n'
              f'{'Item name:':<20}{element:<10}\n'
              f'{'HP: ':<20}{avatar.get('hp', 0):<10}\n'
              f'{'Strength: ':<20}{avatar.get('strength', 0):<10}\n'
              f'{'The Avatar: ':<20}\n{avatar.get('avatar', 0)}\n\n')
        sleep()

    chosen_item_number = int(input(f"Please choose your {obj_type} by typing the corresponding number:\n"))-1
    chosen_item_name = list(obj_type_list.keys())[chosen_item_number]
    chosen_item = obj_type_list.get(chosen_item_name)

    # creating the Item object of chosen type and updating its stats
    return Item(obj_type=obj_type, hp=chosen_item.get('hp', 0), strength=chosen_item.get('strength', 0),
                avatar=chosen_item.get('avatar', r''), name=chosen_item_name)


