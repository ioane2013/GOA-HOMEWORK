#codewars link https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
# 7 kyu
#code:
def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))