def calculate_BMI(maesurments: tuple):
    return maesurments[1] / (maesurments[0] ** 2)


def BMI_category(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi > 25:
        return 'obese'
    else:
        return 'normal-weight'
