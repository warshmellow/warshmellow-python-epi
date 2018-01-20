from collections import Counter


def can_form_palindrome(a: str):
    c = Counter(a)
    return sum(v % 2 for v in c.values()) <= 1


def is_letter_constructible(letter_text, magazine_text: str) -> bool:
    return not Counter(letter_text) - Counter(magazine_text)
