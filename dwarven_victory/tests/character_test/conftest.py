import pytest
import dwarven_victory.character.character_logic as character_logic
import dwarven_victory.items.items_logic as items_logic

@pytest.fixture
def dwarven_character():
    character = character_logic.Character("dwarf")
    return character


