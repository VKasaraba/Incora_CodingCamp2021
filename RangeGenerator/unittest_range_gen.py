import unittest
from range_generator import range_gen

range_gen1 = range_gen(10)
range1 = range(10)
range_gen2 = range_gen(3, 10)
range2 = range(3, 10)
range_gen3 = range_gen(3, 10, 2)
range3 = range(3, 10, 2)
range_gen4 = range_gen(-10)
range4 = range(-10)
range_gen5 = range_gen(10, -10)
range5 = range(10, -10)
range_gen6 = range_gen(10, -10, -2)
range6 = range(10, -10, -2)


class TestResult(unittest.TestCase):
    def test_results(self):
        self.assertEqual([el for el in range1], [el for el in range_gen1])
        self.assertEqual([el for el in range2], [el for el in range_gen2])
        self.assertEqual([el for el in range3], [el for el in range_gen3])
        self.assertEqual([el for el in range4], [el for el in range_gen4])
        self.assertEqual([el for el in range5], [el for el in range_gen5])
        self.assertEqual([el for el in range6], [el for el in range_gen6])

# check that errors are raised when necessary
    def test_errors_rising(self):
        with self.assertRaises(ValueError):
            next(range_gen('Harry', 10, 1))
        with self.assertRaises(ValueError):
            next(range_gen(1, 'Hermione', 1))
        with self.assertRaises(ValueError):
            next(range_gen(1, 10, 'Ron'))
        with self.assertRaises(ValueError):
            next(range_gen(1, 10, 0))  # arg3 cannot be 0
        with self.assertRaises(TypeError):
            next(range_gen())
        with self.assertRaises(TypeError):
            next(range_gen(1, 2, 3, 4))


if __name__ == '__main__':
    unittest.main()
