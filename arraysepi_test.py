import arraysepi
import unittest

class TestArraysEpi(unittest.TestCase):
    def test_sumsum(self):
        nums = [1,2,3]
        self.assertEqual(arraysepi.mysum(nums), sum(nums))
    
if __name__ == '__main__':
    unittest.main()