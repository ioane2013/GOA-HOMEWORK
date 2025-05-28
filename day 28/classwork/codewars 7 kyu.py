# link https://www.codewars.com/kata/5356ad2cbb858025d800111d/train/python

#code:
def cap_me(names):
    return [name.capitalize() for name in names]

#link https://www.codewars.com/kata/54b81566cd7f51408300022d/train/python
# code:
def word_search(words, term):
    term_lower = term.lower()
    return [word for word in words if term_lower in word.lower()]
