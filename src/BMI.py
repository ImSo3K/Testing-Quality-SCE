def calculate_BMI(maesurments: tuple):
    try:
        BMI = maesurments[1] / (maesurments[0] ** 2)
    except ZeroDivisionError as err:
        raise err
    return BMI


def BMI_category(bmi):
    bmiDict={18.5:'underweight',25:'normal-weight',29.9:'excess-weight'
        ,34.9:'obese-L1',39.9:'obese-L2',40:'obese-L3'}
    for item in bmiDict:
        if bmi < item:
            return bmiDict[item]
    return bmiDict[40]
