import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEquals(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(3, 3), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(3, 3), 1)
        self.assertEqual(self.calculator.result, 1)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.square(3), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_sqrt_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertEqual(self.calculator.result, 3)


if __name__ == '__main__':

    unittest.main()
