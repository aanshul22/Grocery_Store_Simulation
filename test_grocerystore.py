"""CSC148 Assignment 1: Tests for GroceryStore

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the GroceryStore class.

Author: Anshul Agrawal
"""
from io import StringIO
from store import GroceryStore
from store import *
JSON_FILE_CONTENTS = '{"regular_count": 1,"express_count": 2,   \
                       "self_serve_count": 3,"line_capacity": 2}'

SHORT_FILE_CONTENTS = '{"regular_count": 1,"express_count": 1,   \
                       "self_serve_count": 1,"line_capacity": 2}'

ONE_LINE_FILE_CONTENTS = '{"regular_count": 1,"express_count": 0,   \
                       "self_serve_count": 0,"line_capacity": 5}'

SELF_SERVE_FILE_CONTENTS = '{"regular_count": 0,"express_count": 0,   \
                       "self_serve_count": 1,"line_capacity": 5}'


def test_grocerystore_init() -> None:
    """Test the Initializer of the GroceryStore Class."""

    gs = GroceryStore(StringIO(JSON_FILE_CONTENTS))
    assert gs._regular_count == 1
    assert gs._express_count == 2
    assert gs._self_serve_count == 3
    assert gs._line_capacity == 2
    assert type(gs._checkout_lines[0]) == RegularLine
    assert type(gs._checkout_lines[1]) == ExpressLine
    assert type(gs._checkout_lines[2]) == ExpressLine
    assert type(gs._checkout_lines[3]) == SelfServeLine
    assert type(gs._checkout_lines[4]) == SelfServeLine
    assert type(gs._checkout_lines[5]) == SelfServeLine
    for line in gs._checkout_lines:
        assert line.capacity == 2

def test_enter_line() -> None:
    """Test the enter_line function of the GroceryStore Class."""
    gs = GroceryStore(StringIO(SHORT_FILE_CONTENTS))
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10)])
    c5 = Customer('E', [Item('grapes', 10), Item('grapes', 10),
                        Item('grapes', 10), Item('grapes', 10),
                        Item('grapes', 10), Item('grapes', 10),
                        Item('grapes', 10), Item('grapes', 10)])
    c6 = Customer('F', [Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1)])
    c7 = Customer('G', [Item('bananas', 7)])
    c8 = Customer('H', [])
    assert gs.enter_line(c1) == 0
    assert gs.enter_line(c2) == 1
    assert gs.enter_line(c3) == 2
    assert gs.enter_line(c4) == 0
    assert gs.enter_line(c5) == 2
    assert gs.enter_line(c6) == -1
    assert gs.enter_line(c7) == 1
    assert gs.enter_line(c8) == -1
    assert len(gs._checkout_lines[0].queue) == 2
    assert len(gs._checkout_lines[1].queue) == 2
    assert len(gs._checkout_lines[2].queue) == 2

def test_line_is_ready() -> None:
    """Test the line_is_ready function of the GroceryStore Class."""
    gs = GroceryStore(StringIO(SHORT_FILE_CONTENTS))
    gs2 = GroceryStore(StringIO(SHORT_FILE_CONTENTS))
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10)])
    gs.enter_line(c1)
    gs.enter_line(c2)
    gs.enter_line(c3)
    gs.enter_line(c4)
    assert gs.line_is_ready(0) == False
    assert gs.line_is_ready(1) == True
    assert gs.line_is_ready(2) == True
    assert gs2.line_is_ready(0) == False
    assert gs2.line_is_ready(1) == False
    assert gs2.line_is_ready(2) == False


def test_start_checkout() -> None:
    """Test the start_checkout function of the GroceryStore Class."""
    gs = GroceryStore(StringIO(ONE_LINE_FILE_CONTENTS))
    gs2 = GroceryStore(StringIO(SELF_SERVE_FILE_CONTENTS))
    c1 = Customer('A', [Item('bananas', 7), Item('apple', 2), \
                        Item('orange', 5), Item('grapes', 10)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    gs.enter_line(c1)
    gs.enter_line(c2)
    gs2.enter_line(c3)
    assert gs.start_checkout(0) == 24
    assert gs2.start_checkout(0) == 10


def test_complete_checkout() -> None:
    """Test the complete_checkout function of the GroceryStore Class."""
    gs = GroceryStore(StringIO(SHORT_FILE_CONTENTS))
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10)])
    gs.enter_line(c1)
    gs.enter_line(c2)
    gs.enter_line(c3)
    gs.enter_line(c4)
    assert gs.complete_checkout(0) == True
    assert gs.complete_checkout(1) == False
    assert gs.complete_checkout(2) == False

def test_close_line_and_get_first_in_line() -> None:
    """Test the close_line function of the GroceryStore Class."""
    gs = GroceryStore(StringIO(ONE_LINE_FILE_CONTENTS))
    gs2 = GroceryStore(StringIO(SELF_SERVE_FILE_CONTENTS))
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10)])
    gs.enter_line(c1)
    gs.enter_line(c2)
    gs.enter_line(c3)
    gs.enter_line(c4)
    assert gs.close_line(0) == [c2, c3, c4]
    assert gs.get_first_in_line(0) == c1
    assert gs._checkout_lines[0].queue == [c1]
    assert gs2.get_first_in_line(0) is None

if __name__ == '__main__':
    import pytest
    pytest.main(['test_grocerystore.py'])
