from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt


class StatisticsTest(TestCase):

    def test_average_empty(self):
        """Average of empty array"""
        self.assertRaises(ValueError, average, [])

    def test_variance_typical_values(self):
        """Variance of typical values"""
        self.assertAlmostEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertAlmostEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertAlmostEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_empty(self):
        """Variance of empty array"""
        self.assertRaises(ValueError, variance, [])

    def test_variance_non_integers(self):
        """Variance should work with decimal values"""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_stdev(self):
        # standard deviation of a single value should be zero
        self.assertAlmostEqual(0.0, stdev([10.0]))
        # simple test
        self.assertAlmostEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertAlmostEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))


if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=1)
