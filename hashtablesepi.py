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


def lca(a, b):
    return


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
    def list_contains(subarray, keywords):
        sub_counts = Counter(subarray)
        keywords_counts = Counter(keywords)
        return sub_counts & keywords_counts == keywords_counts

    if not list_contains(s, query):
        return

    k, j = min([(i, j) for i in range(len(s))
                for j in range(i + 1,
                               len(s) + 1) if list_contains(s[i:j], query)],
               key=lambda x: len(s[x[0]:x[1]]))
    return k, j - 1


def smallest_cover_lin(s, query):
    def counter_contains(bigger, smaller):
        return bigger & smaller == smaller

    if not counter_contains(Counter(s), Counter(query)):
        return

    query_counts = Counter(query)
    current_counts = Counter()

    # Find smallest set starting at 0 that covers the set
    # Fill out Counter of query keywords in s[0:j]

    j = len([
        current_counts.update([s[j]]) for j in range(len(s))
        if not counter_contains(current_counts, query_counts)
    ])

    # Update
    i = 0
    contains_indices = [(i, j)]
    while i < len(s) and j < len(s) + 1:
        if counter_contains(current_counts, query_counts):
            contains_indices.append((i, j))
            current_counts[s[i]] -= 1
            i += 1
        elif j < len(s):
            current_counts.update(s[j])
            j += 1
        else:
            j += 1

    min_i, min_j = min(contains_indices, key=lambda x: x[1] - x[0])
    return min_i, min_j - 1


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
