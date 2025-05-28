# 8 kyu
# https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python
# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python
# 1) code:
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    
# 2) code:
def boolean_to_string(b):
    return str(b)