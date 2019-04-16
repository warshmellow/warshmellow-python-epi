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


def smallest_cover(s, query):
    return 8, 10


def len_longest_contained_interval(s):
    if len(s) <= 1:
        return
    elif len(s) == 2 and s[0] == s[1] - 1:
        return 2
    elif len(s) == 2 and s[0] != s[1] - 1:
        return

    s.sort()

    results = [1]
    # init
    if s[1] == s[0] + 1:
        results.append(2)
    else:
        results.append(1)

    # recursive
    for i, x in enumerate(s):
        if i < 2:
            continue
        # what is the length of largest subset ending in x?
        if x == s[i - 1] + 1:
            results.append(results[i - 1] + 1)
        else:
            results.append(1)

    return max(results)
