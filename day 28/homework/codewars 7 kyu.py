#link https://www.codewars.com/kata/52f3149496de55aded000410/train/python
#code:
def most_frequent_item_count(collection):
    if not collection:
        return 0
    max_count = 0
    for i in collection:
        count = collection.count(i)
        if count > max_count:
            max_count = count
    return max_count

#link https://www.codewars.com/kata/5264d2b162488dc400000001/train/python
#code:
def spin_words(sentence):
    words=sentence.split(" ")
    words_r = []
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
            words_r.append(word)
        else:
            words_r.append(word)
    return  " ".join(words_r)

#link https://www.codewars.com/kata/56582133c932d8239900002e/train/python
#code:
def encode(st):
    st = st.replace('a','1').replace('e','2').replace('i','3').replace('o','4').replace('u','5')
    return st
