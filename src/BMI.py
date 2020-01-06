def calculate_BMI(maesurments: tuple):
    try:
        BMI = maesurments[1] / (maesurments[0] ** 2)
    except ZeroDivisionError as err:
        return err
    return BMI


def BMI_category(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi > 25:
        return 'obese'
    else:
        return 'normal-weight'
