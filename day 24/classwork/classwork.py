# 7 kyu
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
# https://www.codewars.com/kata/559590633066759614000063/train/python
# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python
# https://www.codewars.com/kata/566fc12495810954b1000030/train/python
# https://www.codewars.com/kata/511f11d355fe575d2c000001/train/python

#1) code:
def accum(s):
    return '-'.join((ch * (i + 1)).capitalize() for i, ch in enumerate(s))

#2) code:
def min_max(arr):
    return [min(arr), max(arr)]

#3) code:
def arithmetic(a, b, operator):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }
    return operations[operator]

#4) code:
def nb_dig(n, d):
    count = 0
    for k in range(n + 1):
        count += str(k**2).count(str(d))
    return count

#5) code:
def two_oldest_ages(ages):
    return sorted(ages)[-2:]