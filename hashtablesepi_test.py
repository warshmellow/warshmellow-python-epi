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
    def test_lru_cache(self):
        now = time.gmtime(1554824405)

        c = LRUCache(1)
        c.set("isbn1", 100, now)
        c.set("isbn2", 200, time.gmtime(1554824405 + 1000))
        self.assertEqual(len(c), 1)
        self.assertEqual(c.get("isbn1"), None)
        self.assertEqual(c.get("isbn2"), 200)


if __name__ == '__main__':
    unittest.main()
