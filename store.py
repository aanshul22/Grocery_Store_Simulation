"""CSC148 Assignment 1 - Modelling a Grocery Store (Task 1a)

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains all of the classes necessary to model the entities
in a grocery store.

Author: Anshul Agrawal
"""
from __future__ import annotations
from typing import List, Optional, TextIO
import json

EXPRESS_LIMIT = 7


class GroceryStore:
    """A grocery store.

    === Private Attributes ===
    _regular_count: number of regular checkout lines
    _express_count: number of express checkout lines
    _self_serve_count: number of self serve checkout lines
    _line_capacity: the maximum capacity of all lines
    _checkout_lines: The list of the checkoutlines in this GroceryStore
    """
    _regular_count: int
    _express_count: int
    _self_serve_count: int
    _line_capacity: int
    _checkout_lines: List[CheckoutLine]

    def __init__(self, config_file: TextIO) -> None:
        """Initialize a GroceryStore from a configuration file <config_file>.
        """
        j = json.load(config_file)
        self._regular_count = j['regular_count']
        self._express_count = j['express_count']
        self._self_serve_count = j['self_serve_count']
        self._line_capacity = j['line_capacity']
        self._checkout_lines = []

        for _ in range(self._regular_count):
            self._checkout_lines.append(RegularLine(self._line_capacity))
        for _ in range(self._express_count):
            self._checkout_lines.append(ExpressLine(self._line_capacity))
        for _ in range(self._self_serve_count):
            self._checkout_lines.append(SelfServeLine(self._line_capacity))

    def enter_line(self, customer: Customer) -> int:
        """Pick a new line for <customer> to join.

        Return the index of the line that the customer joined.
        Must use the algorithm from the handout.

        Return -1 if there is no line available for the customer to join.
        """
        smallest = self._line_capacity + 1
        enter = 0
        for line in self._checkout_lines:
            size = len(line)
            if size < smallest and line.can_accept(customer):
                smallest = size
                enter = line
        if enter == 0:
            return -1
        else:
            enter.accept(customer)
            return self._checkout_lines.index(enter)

    def line_is_ready(self, line_number: int) -> bool:
        """Thus, line_is_ready should return True if and only if there is
        exactly one customer in line.
        """
        if len(self._checkout_lines[line_number]) == 1:
            return True
        else:
            return False

    def start_checkout(self, line_number: int) -> int:
        """Return the time it will take to check out the next customer in
        line <line_number>

        Pre-condition: There is a customer in the given line.
        """
        return self._checkout_lines[line_number].start_checkout()

    def complete_checkout(self, line_number: int) -> bool:
        """Return True iff there are customers remaining to be checked out in
        line <line_number>
        """
        return self._checkout_lines[line_number].complete_checkout()

    def close_line(self, line_number: int) -> List[Customer]:
        """Close checkout line <line_number> and return the customers from
        that line who are still waiting to be checked out.
        """
        return self._checkout_lines[line_number].close()

    def get_first_in_line(self, line_number: int) -> Optional[Customer]:
        """Return the first customer in line <line_number>, or None if there
        are no customers in line.
        """
        line = self._checkout_lines[line_number]
        if len(line) == 0:
            return None
        else:
            return line.queue[0]


class Customer:
    """A grocery store customer.

    === Attributes ===
    name: A unique identifier for this customer.
    arrival_time: The time this customer joined a line.
    _items: The items this customer has.

    === Representation Invariant ===
    arrival_time >= 0 if this customer has joined a line, and -1 otherwise
    """
    name: str
    arrival_time: int
    _items: List[Item]

    def __init__(self, name: str, items: List[Item]) -> None:
        """Initialize a customer with the given <name>, an initial arrival time
         of -1, and a copy of the list <items>.

        >>> item_list = [Item('bananas', 7)]
        >>> belinda = Customer('Belinda', item_list)
        >>> belinda.name
        'Belinda'
        >>> belinda._items == item_list
        True
        >>> belinda.arrival_time
        -1
        """
        self.name = name
        self.arrival_time = -1
        self._items = items

    def num_items(self) -> int:
        """Return the number of items this customer has.

        >>> c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
        >>> c.num_items()
        2
        """
        return len(self._items)

    def get_item_time(self) -> int:
        """Return the number of seconds it takes to check out this customer.

        >>> c = Customer('Bo', [Item('bananas', 7), Item('cheese', 3)])
        >>> c.get_item_time()
        10
        """
        time = 0
        for item in self._items:
            time += item.get_time()
        return time


class Item:
    """A class to represent an item to be checked out.

    Do not change this class.

    === Attributes ===
    name: the name of this item
    _time: the amount of time it takes to checkout this item
    """
    name: str
    _time: int

    def __init__(self, name: str, time: int) -> None:
        """Initialize a new time with <name> and <time>.

        >>> item = Item('bananas', 7)
        >>> item.name
        'bananas'
        >>> item._time
        7
        """
        self.name = name
        self._time = time

    def get_time(self) -> int:
        """Return how many seconds it takes to checkout this item.

        >>> item = Item('bananas', 7)
        >>> item.get_time()
        7
        """
        return self._time


class CheckoutLine:
    """A checkout line in a grocery store.

    This is an abstract class; subclasses are responsible for implementing
    start_checkout().

    === Attributes ===
    capacity: The number of customers allowed in this CheckoutLine.
    is_open: True iff the line is open.
    queue: Customers in this line in FIFO order.

    === Representation Invariants ===
    - Each customer in this line has not been checked out yet.
    - The number of customers is less than or equal to capacity.
    """
    capacity: int
    is_open: bool
    queue: List[Customer]

    def __init__(self, capacity: int) -> None:
        """Initialize an open and empty CheckoutLine.

        >>> line = CheckoutLine(1)
        >>> line.capacity
        1
        >>> line.is_open
        True
        >>> line.queue
        []
        """
        self.capacity = capacity
        self.is_open = True
        self.queue = []

    def __len__(self) -> int:
        """Return the size of this CheckoutLine.
        """
        return len(self.queue)

    def can_accept(self, customer: Customer) -> bool:
        """Return True iff this CheckoutLine can accept <customer>.
        """
        if len(self) < self.capacity and self.is_open:
            return True
        else:
            return False

    def accept(self, customer: Customer) -> bool:
        """Accept <customer> at the end of this CheckoutLine.
        Return True iff the customer is accepted.

        >>> line = CheckoutLine(1)
        >>> c1 = Customer('Belinda', [Item('cheese', 3)])
        >>> c2 = Customer('Hamman', [Item('chips', 4), Item('gum', 1)])
        >>> line.accept(c1)
        True
        >>> line.accept(c2)
        False
        >>> line.queue == [c1]
        True
        """
        if self.can_accept(customer):
            self.queue.append(customer)
            return True
        else:
            return False

    def start_checkout(self) -> int:
        """Checkout the next customer in this CheckoutLine.

        Return the time it will take to checkout the next customer.
        """
        return self.queue[0].get_item_time()

    def complete_checkout(self) -> bool:
        """Finish the checkout for this CheckoutLine.

        Return whether there are any remaining customers in the line.
        """
        self.queue.pop(0)
        if len(self.queue) > 0:
            return True
        else:
            return False

    def close(self) -> List[Customer]:
        """Close this line.

        Return a list of all customers that need to be moved to another line.
        """
        self.is_open = False
        remaining = self.queue[1:]
        self.queue = self.queue[:1]
        return remaining


class RegularLine(CheckoutLine):
    """A regular CheckoutLine."""


class ExpressLine(CheckoutLine):
    """An express CheckoutLine.
    """
    def can_accept(self, customer: Customer) -> bool:
        """Return True iff this CheckoutLine can accept <customer>.
        """
        if len(self) < self.capacity and customer.num_items() <= EXPRESS_LIMIT \
           and self.is_open:
            return True
        else:
            return False


class SelfServeLine(CheckoutLine):
    """A self-serve CheckoutLine.
    """
    def start_checkout(self) -> int:
        """Checkout the next customer in this CheckoutLine.

        Return the time it will take to checkout the next customer.
        """
        return self.queue[0].get_item_time() * 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config={
        'allowed-import-modules': ['__future__', 'typing', 'json',
                                   'python_ta', 'doctest'],
        'disable': ['W0613']})
