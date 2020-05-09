from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List, Any


class CollectionIterator(Iterator):
    _position: int = None
    _is_reverse: bool = False
    _collection: List[Any] = None

    def __init__(self, collection, is_reverse: bool = False) -> None:
        self._collection = collection
        self._is_reverse = is_reverse
        self._position = -1 if is_reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._is_reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class StringCollation(Iterable):
    _collection: List[str] = None

    def __init__(self, collection: List[str] = None) -> None:
        if collection is None:
            self._collection = []
        else:
            self._collection = collection

    def __iter__(self) -> CollectionIterator:
        return CollectionIterator(self._collection)

    def get_reverse_iterator(self) -> CollectionIterator:
        return CollectionIterator(self._collection, True)

    def add(self, item: str):
        self._collection.append(item)


if __name__ == "__main__":
    words = StringCollation(["Zero"])
    words.add("One")
    words.add("Two")
    words.add("Three")

    print("Straight traversal:")
    for word in words:
        print(word)
    print()

    print("Reverse traversal:")
    for word in words.get_reverse_iterator():
        print(word)
    print()
