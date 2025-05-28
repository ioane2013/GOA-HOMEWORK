# link https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

#code:
from collections import Counter

def duplicate_count(text):
    counts = Counter(text.lower())
    return sum(1 for count in counts.values() if count > 1)

# link https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

#code:
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)




# link https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

#code:
import re

def to_camel_case(text):
    words = re.split('[-_]', text)
    return words[0] + ''.join(word.capitalize() for word in words[1:])
