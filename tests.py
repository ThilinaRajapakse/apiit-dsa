import unittest
import random
import time


def make_test(func):
    class TestImplementation(unittest.TestCase):
        def setUp(self):
            self.s = time.time()

        def tearDown(self):
            self.e = time.time()
            t = self.e - self.s

            print(f'Time taken: {t}')

        def test_worst_case(self):
            to_sort = [i for i in range(9999, -1, -1)]
            after_sort = [i for i in range(10000)]
            self.assertEqual(func(to_sort), after_sort)

        def test_random_case(self):
            to_sort = [random.randint(0, 10000) for i in range(10000)]
            after_sort = sorted(to_sort)
            self.assertEqual(func(to_sort), after_sort)

        def test_best_case(self):
            to_sort = [i for i in range(10000)]
            self.assertEqual(func(to_sort), to_sort)

    return TestImplementation

from insertion import insertion_sort
from selection import selection_sort
from mergesort import mergesort


class InsertionSortTestCase(make_test(insertion_sort)):
    pass

class SelectionSortTestCase(make_test(selection_sort)):
    pass

class MergeSortTestCase(make_test(mergesort)):
    pass