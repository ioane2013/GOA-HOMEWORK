# 2) დაწერეთ პროგრამა, რომელიც მომხმარებელს მოსთხოვს რიცხვის შემოტანას.
# თუ შემოტანილი რიცხვი ლუწია და  მეტია ათზე დაბეჭდოს "True".
# სხვა შემთხვევაში, დაბეჭდოს "False".

number = int(input("enter a number:  "))


if number > 10 and number % 2 == 0:
    print("True")
else:
    print("False")