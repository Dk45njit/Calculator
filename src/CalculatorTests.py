import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator();
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator();
        self.assertEqual(calculator.result, 0)

    def test_add_method_calculator(self):
       test_data = CsvReader('./src/Unit Test Addition.csv').data
       for row in test_data:
        self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
        self.assertEqual(self.calculator.result, int(row['Result']))