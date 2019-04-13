from collections import Counter, defaultdict
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
    indices_by_entry = defaultdict(list)
    for i, entry in enumerate(s):
        indices_by_entry[entry].append(i)

    h = {}
    for entry, ind in indices_by_entry.items():
        if len(ind) > 1:
            h[entry] = min([ind[i] - ind[i - 1] for i in range(1, len(ind))])

    return min(h.values())


def len_longest_contained_interval(s):
    def all_between(a):
        first, last = a[0], a[-1]
        if first == last:
            return True
        elif first < last:
            return len([x for x in a if first <= x and x <= last]) == len(a)
        else:
            return len([x for x in a if first >= x and x >= last]) == len(a)

    if len(s) <= 1:
        return
    elif len(s) == 2:
        return 2

    all_possible = [(i, j) for i in range(len(s))
                    for j in range(i + 1, len(s)) if all_between(s[i:j])]

    return max([j - i for i, j in all_possible])
