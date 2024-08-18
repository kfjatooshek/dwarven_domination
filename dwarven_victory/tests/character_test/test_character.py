import pytest
from dwarven_victory.character.character_logic import Character, pick_race


class TestDwarfCharacter:
    def setup_method(self, method):
        print(f"setting up method {method}")
        self.player = Character("dwarf")

    def teardown_method(self, method):
        print(f"tearning down {method}")

    def test_strength(self):
        assert 100 <= self.player.strength <= 200

    def test_race(self):
        assert self.player.race == "dwarf"
