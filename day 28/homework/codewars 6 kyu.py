# link https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

# code:
def spin_words(sentence):
    return ' '.join(
        word[::-1] if len(word) >= 5 else word
        for word in sentence.split()
    )


# link https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

# code:
def encode(string):
    vowel_to_number = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    return ''.join(vowel_to_number.get(char, char) for char in string)

def decode(string):
    number_to_vowel = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    return ''.join(number_to_vowel.get(char, char) for char in string)
