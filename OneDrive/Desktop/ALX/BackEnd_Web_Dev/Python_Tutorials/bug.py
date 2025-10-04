import unittest

# Buggy function


def square(x):
    # BUG: Should be x * x, but written incorrectly as x + x
    return x + x

# Unit test class


class TestSquareFunction(unittest.TestCase):

    def test_square_positive(self):
        self.assertEqual(square(3), 9)   # This will FAIL because square(3) = 6

    def test_square_negative(self):
        # This will FAIL because square(-4) = -8
        self.assertEqual(square(-4), 16)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)   # This one will PASS


# Run tests
if __name__ == "__main__":
    unittest.main()
