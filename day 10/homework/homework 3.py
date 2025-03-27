# 4) ცვლადში შეინახეთ პაროლი. შემდეგ მომხმარებელს შემოატანინეთ პაროლი,
# სანამ მომხმარებლის მიერ შემოტანილი პაროლი არ დაემთხვევა თქვენს პაროლს,
# გამოუტანეთ "Incorrect password. Try again". იმ შემთხვევაში თუ
# ეს პაროლები ერთმანეთს დაემთხვევა გამოიტანეთ "Correct password."
# " You have successfully logged in." (გააკეთეთ While ციკლით, არ გამოიყენოთ if else statement-ები.)

password = "ioane2013"
user_input = input("enter your password: ")
while user_input != password:
    print("incorrect password. Try again")
    user_input = input("enter your password: ")
    print("your entered password is correct")

