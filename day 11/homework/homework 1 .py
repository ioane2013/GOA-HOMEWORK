# 1) შექმენით Number guess game, if else statement-ების გამოყენებით.

#number guess game

number =  1
user_input = int(input("guess a number (1-10): "))

if user_input != number:
    print("your entered number is incorrect.try again")
else:
    print("entered number is correct.good job")