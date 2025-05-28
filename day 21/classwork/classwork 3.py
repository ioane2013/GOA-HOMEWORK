#codewars link https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
# 7 kyu
# code:
def find_short(s):
    return len(min(s.split(), key=len))