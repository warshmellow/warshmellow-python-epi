from collections import Counter
import time


def can_form_palindrome(a: str):
    c = Counter(a)
    return sum(v % 2 for v in c.values()) <= 1


def is_letter_constructible(letter_text, magazine_text: str) -> bool:
    return not Counter(letter_text) - Counter(magazine_text)


class LRUCache:
    def __init__(self, size):
        self._table = {}
        self._size = size

    def __len__(self):
        return len(self._table)

    def size(self):
        return self._size

    def _remove_lru(self):
        def mins(table):
            min_key, min_value, min_time = None, None, None
            for k, v in table.items():
                value, t = v
                if not min_key or min_value > t:
                    min_key = k
                    min_value = value
                    min_time = t
            return min_key, (min_value, min_time)

        min_key, _ = mins(self._table)
        del self._table[min_key]

    def insert(self, key, value, time=time.gmtime()):
        # if key exists update time but not value
        if key in self._table:
            v, _ = self._table[key]
            self._table[key] = (v, time)
            return

        # if key not exists, remove Least Recently Used
        if len(self._table) == self._size:
            self._remove_lru()

        self._table[key] = (value, time)

    def get(self, key, time=time.gmtime()):
        if key in self._table:
            v, _ = self._table[key]
            self._table[key] = (v, time)
            return v

    def remove(self, key):
        del self._table[key]


def nearest_repeated(s):
    return 2


def len_longest_contained_interval(s):
    return 6