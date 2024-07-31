from dwarven_victory.enemies.enemy_stats_dict import elements
from dwarven_victory.base import pick_element


def pick_enemy(obj_type):
    return pick_element(obj_type, dictionary=elements)

