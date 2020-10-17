"""CSC148 Assignment 1: Tests for checkout classes

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for testing the checkout classes.

Author: Anshul Agrawal
"""
from store import RegularLine, ExpressLine, SelfServeLine, Customer, Item


def test_CheckoutLine_init() -> None:
    """Test the Initializer of the Checkout Class."""
    a = RegularLine(15)
    b = ExpressLine(10)
    c = SelfServeLine(5)
    assert a.capacity == 15
    assert a.queue == []
    assert a.is_open is True
    assert b.capacity == 10
    assert b.queue == []
    assert b.is_open is True
    assert c.capacity == 5
    assert c.queue == []
    assert c.is_open is True

def test_CheckoutLine_len() -> None:
    """Test the __len__ function of the Checkout Class."""
    a = RegularLine(15)
    b = ExpressLine(10)
    c = SelfServeLine(5)
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10)])
    a.queue = [c1]
    b.queue = [c2, c3, c4]
    assert len(a) == 1
    assert len(b) == 3
    assert len(c) == 0

def test_can_accept() -> None:
    """Test the can_accept function of the Checkout Class."""
    a = RegularLine(3)
    b = ExpressLine(3)
    c = SelfServeLine(3)
    d = ExpressLine(3)
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10)])
    c5 = Customer('E', [Item('grapes', 10)])
    c6 = Customer('F', [Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1)])
    a.queue = [c1]
    b.queue = [c2, c3, c4]
    assert a.can_accept(c5) == True
    assert b.can_accept(c5) == False
    assert c.can_accept(c5) == True
    assert d.can_accept(c6) == False
    assert d.can_accept(c5) == True

def test_accept() -> None:
    """Test the accept function of the Checkout Class."""
    a = RegularLine(3)
    b = ExpressLine(3)
    c = SelfServeLine(3)
    d = ExpressLine(3)
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10)])
    c5 = Customer('E', [Item('grapes', 10)])
    c6 = Customer('F', [Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1),
                        Item('avacado', 1), Item('avacado', 1)])
    a.queue = [c1]
    b.queue = [c2, c3, c4]
    assert a.accept(c5) == True and a.queue == [c1, c5]
    assert b.accept(c5) == False and b.queue == [c2, c3, c4]
    assert c.accept(c5) == True and c.queue == [c5]
    assert d.accept(c6) == False and d.queue == []
    assert d.accept(c5) == True and d.queue == [c5]

def test_start_checkout() -> None:
    """Test the start_checkout function of the Checkout Class."""
    a = RegularLine(3)
    b = ExpressLine(3)
    c = SelfServeLine(3)
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10), Item('avacado', 1)])
    a.queue = [c1]
    b.queue = [c2, c3]
    c.queue = [c4]
    assert a.start_checkout() == 7
    a.queue = [c1, c2]
    assert a.start_checkout() == 7
    assert b.start_checkout() == 0
    b.queue = [c3]
    assert b.start_checkout() == 5
    assert c.start_checkout() == 22
    c.queue = [c1, c2, c3, c4]
    assert c.start_checkout() == 14

def test_complete_checkout() -> None:
    """Test the complete_checkout function of the Checkout Class."""
    a = RegularLine(3)
    b = ExpressLine(3)
    c = SelfServeLine(3)
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10), Item('avacado', 1)])
    a.queue = [c1]
    b.queue = [c2, c3]
    c.queue = [c4]
    assert a.complete_checkout() == False and a.queue == []
    a.queue = [c2, c1]
    assert a.complete_checkout() == True and a.queue == [c1]
    assert b.complete_checkout() == True and b.queue == [c3]
    assert c.complete_checkout() == False and c.queue == []

def test_close() -> None:
    """Test the close function of the Checkout Class."""
    a = RegularLine(3)
    b = ExpressLine(3)
    c = SelfServeLine(3)
    c1 = Customer('A', [Item('bananas', 7)])
    c2 = Customer('B', [Item('apple', 2)])
    c3 = Customer('C', [Item('orange', 5)])
    c4 = Customer('D', [Item('grapes', 10)])
    a.queue = [c1]
    b.queue = [c2, c3, c4]
    assert a.close() == [] and a.is_open == False
    assert b.close() == [c3, c4] and a.is_open == False
    assert c.close() == [] and a.is_open == False
    assert a.queue == [c1]
    assert b.queue == [c2]
    assert c.queue == []


if __name__ == '__main__':
    import pytest
    pytest.main(['test_checkouts.py'])
