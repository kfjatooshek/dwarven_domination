import pytest
from dwarven_victory.character.character_logic import Character, pick_race


def test_strength(dwarven_character):
    assert 100 <= dwarven_character.strength <= 200


def test_name(dwarven_character):
    assert dwarven_character.name is None





