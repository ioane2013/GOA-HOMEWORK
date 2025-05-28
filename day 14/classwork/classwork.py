# 1) მომხმარებელს შემოატანინეთ 10 მნიშვნელობა სიაში (For loop-ის მეშვეობით. )
# შემდეგ გამოიყენეთ კიდევ ერთი for loop, გადაუარეთ თითოეულ სიის ელემენტს და შამოწმეთ ეს 
# რიცხვები ლუწია თუ კენტი

numbers = []

for i in range(10):
    number = int(input("Please enter a number: "))
    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")





