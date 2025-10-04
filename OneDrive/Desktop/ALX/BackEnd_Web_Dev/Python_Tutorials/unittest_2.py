# load test framework.
import unittest

# Define the function you want to test.


def square(x):
    return x * x

# define a group of tests.


class TestMathFunctions(unittest.TestCase):
    # individual test cases.
    def test_square_positive(self):
        # Define ways to check result
        self.assertEqual(square(3), 9)

    def test_square_negative(self):
        self.assertEqual(square(-4), 16)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)


# runs all the tests.
if __name__ == "__main__":
    unittest.main()
