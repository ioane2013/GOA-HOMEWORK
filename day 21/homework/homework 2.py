#codewars link https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
# 8 kyu
#code:
def replace_exclamation(st):
    return ''.join('!' if c.lower() in 'aeiou' else c for c in st)
