import unittest
import BMI


class BMI_test(unittest.TestCase):
    def test_weight_category(self):
        # stub
        stub1 = 17.3
        stub2 = 22.2
        stub3 = 27.8

        # excpected
        exptected1 = 'underweight'
        exptected2 = 'normal-weight'
        exptected3 = 'obese'

        # action
        result1 = BMI.calculate_BMI(stub1)
        result2 = BMI.calculate_BMI(stub2)
        result3 = BMI.calculate_BMI(stub3)

        # actual check
        self.assertEqual(exptected1, result1)
        self.assertEqual(exptected2, result2)
        self.assertEqual(exptected3, result3)
