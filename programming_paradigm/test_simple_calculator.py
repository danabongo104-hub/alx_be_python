from simple_calculator import SimpleCalculator
import unittest


class TestsimpleCalculator(unittest.TestCase):
    def setUp(self):
        """set up the SimpleCalculator instance before each tests.
        """
        self.calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(-6, 2), -3)
        self.assertEqual(self.calculator.divide(-6, -2), 3)
        self.assertIsNone(self.calculator.divide(6, 0))
            

if __name__ == "__main__":
    unittest.main()