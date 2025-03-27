# 5) გამოიყენეთ range და ლუწ ინდექსებზე მდგომი რიცხვები შეკრიბეთ. ჯამი გამოიტანეთ ტერმინალში.

numbers = [2,8,1,12,3]

jami = 0

for i in range(0, len(numbers), 2): 
    jami += numbers[i]

print(jami)
