from dwarven_victory.enemies.enemy_stats_dict import elements
from dwarven_victory.items.items_logic import pick_element


def pick_enemy(obj_type):
    return pick_element(obj_type, dictionary=elements)


x = pick_enemy('enemy')
print(x)
