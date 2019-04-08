import unittest

import hypothesis.strategies as st
from hypothesis import given

from hashtablesepi import *


class TestHashTablesEpi(unittest.TestCase):

    # 12.1
    @given(st.text())
    def test_can_form_palindrome(self, a: str):
        expected_cond = sum(v % 2 for v in Counter(a).values()) <= 1
        result = can_form_palindrome(a)
        self.assertEqual(result, expected_cond)

    # 12.2
    @given(letter_text=st.text(), magazine_text=st.text())
    def test_is_letter_constructible(self, letter_text, magazine_text):
        expected_cond = not Counter(letter_text) - Counter(magazine_text)
        result = is_letter_constructible(letter_text, magazine_text)
        self.assertEqual(result, expected_cond)

    # 12.3
    @unittest.skip('unfinished')
    def test_lru_cache(self):
        c = LRUCache(1)
        c.set("isbn", 100)


if __name__ == '__main__':
    unittest.main()
