import unittest

# Example class for demonstration of arithmethic operations
# add, subtract, multiply, divide
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a -  b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0: 
            raise ValueError("Cannot divide by zero")
        return a / b
    
# Test class for Calculator 
class TestCalculator(unittest.TestCase): 
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 4), 7)
        self.assertEqual(self.calculator(-3, 2), -1)

    def test_substract(self): 
        self.assertTrue(self.calculator.subtract(6, 2), 4)
        self.assertEqual(self.calculator.subtract(11, 6), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 4), 12)
        self.assertEqual(self.calculator.multiply(-3, 5), 15)

        expected_result = -20
        actual_result = self.calculator.multiply(-4, 5)
        print(f"Actual Result: {actual_result}")
        self.assertEqual(actual_result, expected_result)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(18, 2), 9)
        self.assertEqual(self.calculator.divide(22, 2), 11)
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    # Run the tests
    if __name__ == '__main__': 
        unittest.main()

