# 2) შექმენით Number guess game, while ციკლების გამოყენებით.

#number guess game
number = 4
user_input = int(input("guess a number (1-10): "))
while user_input != number:
    print("incorrect number, try again.")
    user_input = int(input("guess a number (1-10): "))
    
print("entered number is correct. good job!")
    

