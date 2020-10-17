"""Assignment 1 - Container (Task 3)

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains contains the classes representing the Container
and Priority Queue data types.

Author: Anshul Agrawal
"""

from __future__ import annotations
from typing import Any, List


class Container:
    """A container that holds objects.

    You should not change this class.

    This is an abstract class.  Only child classes should be instantiated.
    """

    def add(self, item: Any) -> None:
        """Add <item> to this Container.
        """
        raise NotImplementedError('Implemented in a subclass')

    def remove(self) -> None:
        """Remove and return a single item from this Container.
        """
        raise NotImplementedError('Implemented in a subclass')

    def is_empty(self) -> bool:
        """Return True iff this Container is empty.
        """
        raise NotImplementedError('Implemented in a subclass')


class PriorityQueue(Container):
    """A queue of items that operates in priority order.

    Items are removed from the queue according to priority; the item with the
    highest priority is removed first. Ties are resolved in FIFO order,
    meaning the item which was inserted *earlier* is the first one to be
    removed.

    Priority is defined by the rich comparison methods for the objects in the
    container (__lt__, __le__, __gt__, __ge__).

    If x < y, then x has a *HIGHER* priority than y.

    All objects in the container must be of the same type.

    === Private Attributes ===
    _items: The items stored in the priority queue.

    === Representation Invariants ===
    _items is a sorted list, where the front item is the one with the
    highest priority.
    """
    _items: List

    def __init__(self) -> None:
        """Initialize an empty PriorityQueue.
        """
        self._items = []

    def remove(self) -> Any:
        """Remove and return the next item from this PriorityQueue.

        Precondition: <self> should not be empty.

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('arju')
        >>> pq.add('mona')
        >>> pq.add('hat')
        >>> pq.remove()
        'arju'
        >>> pq.remove()
        'fred'
        >>> pq.remove()
        'hat'
        >>> pq.remove()
        'mona'
        """
        return self._items.pop(0)

    def is_empty(self) -> bool:
        """
        Return True iff this PriorityQueue is empty.

        >>> pq = PriorityQueue()
        >>> pq.is_empty()
        True
        >>> pq.add('fred')
        >>> pq.is_empty()
        False
        """
        return len(self._items) == 0

    def add(self, item: Any) -> None:
        """Add <item> to this PriorityQueue.

        >>> pq = PriorityQueue()
        >>> pq.add('fred')
        >>> pq.add('arju')
        >>> pq.add('mona')
        >>> pq.add('hana')
        >>> pq._items
        ['arju', 'fred', 'hana', 'mona']
        """
        temp_items = self._items.copy()
        if not self._items:
            self._items.append(item)
            return None
        else:
            for element in temp_items:
                if item < element:
                    self._items.insert(self._items.index(element), item)
                    return None
            self._items.append(item)
            return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config={
        'allowed-import-modules': ['__future__', 'typing',
                                   'python_ta', 'doctest']})
