#link https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python
#code 1:
def sum_str(a, b):
    if a == '':
        a = '0'
    if b == '':
        b = '0'
    result = str(int(a) + int(b))
    return result

#link https://www.codewars.com/kata/572b6b2772a38bc1e700007a/train/python
#code 2:
def uni_total(s):
    result = 0
    for i in s:
        result += ord(i)
    return result

