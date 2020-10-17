"""CSC148 Assignment 1: Tests for Customer

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the Customer class.

Author: Anshul Agrawal
"""
from store import Customer
from store import Item


def test_customer_init() -> None:
    """Test the Initializer of the Customer Class."""
    i1 = Item('mango', 1)
    i2 = Item('mango', 1)
    c = Customer('Anshul', [i1, i2])
    assert c.name == 'Anshul'
    assert c.arrival_time == -1
    assert c._items[0] == i1
    assert c._items[1] == i2

def test_customer_num_items() -> None:
    """Test the num_items of the Customer Class."""
    c1 = Customer('Anshul', [Item('bananas', 7), Item('mango', 1)])
    c2 = Customer('Aavi', [])
    assert c1.num_items() == 2
    assert c2.num_items() == 0

def test_customer_get_item_time() -> None:
    """Test the get_item_time of the Customer Class."""
    c1 = Customer('Anshul', [Item('bananas', 7), Item('mango', 1)])
    c2 = Customer('Aavi', [])
    assert c1.get_item_time() == 8
    assert c2.get_item_time() == 0

if __name__ == '__main__':
    import pytest
    pytest.main(['test_customer.py'])
