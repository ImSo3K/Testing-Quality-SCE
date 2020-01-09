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

        # excpected
        exptected1 = 'underweight'
        exptected2 = 'normal-weight'
        exptected3 = 'obese'

        # action
        result1 = BMI.BMI_category(stub1)
        result2 = BMI.BMI_category(stub2)
        result3 = BMI.BMI_category(stub3)

        # actual check
        self.assertEqual(exptected1, result1)
        self.assertEqual(exptected2, result2)
        self.assertEqual(exptected3, result3)


if __name__ == '__main__':
    unittest.main()
