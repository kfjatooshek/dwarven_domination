from dwarven_victory.items.item_stats_dict import elements
from dwarven_victory.base import WorldElement, pick_element


def pick_item(obj_type):
    return pick_element(obj_type, dictionary=elements)



