import unittest
from src import BMI


class BMI_test(unittest.TestCase):
    def test_BMI_calculation(self):
        # stub
        stub1 = (1.72, 87.3)
        stub2 = (0, 87.3)

        # expected
        expected1 = float
        expected2 = ZeroDivisionError

        # action
        result1 = BMI.calculate_BMI(stub1)

        # actual check
        self.assertIsInstance(result1, expected1)
        self.assertRaises(expected2, BMI.calculate_BMI, stub2)

    def test_BMI_category(self):
        # stub
        stub1 = 17.3
        stub2 = 22.2
        stub3 = 27.8
        stub4 = 31
        stub5 = 36
        stub6 = 41

        # excpected
        expected1 = 'underweight'
        expected2 = 'normal-weight'
        expected3 = 'excess-weight'
        expected4 = 'obese-L1'
        expected5 = 'obese-L2'
        expected6 = 'obese-L3'

        # action
        result1 = BMI.BMI_category(stub1)
        result2 = BMI.BMI_category(stub2)
        result3 = BMI.BMI_category(stub3)
        result4 = BMI.BMI_category(stub4)
        result5 = BMI.BMI_category(stub5)
        result6 = BMI.BMI_category(stub6)

        # actual check
        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)
        self.assertEqual(expected3, result3)
        self.assertEqual(expected4, result4)
        self.assertEqual(expected5, result5)
        self.assertEqual(expected6, result6)


if __name__ == '__main__':
    unittest.main()
