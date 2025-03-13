# 4) მომხმარებელს შემოატანინე მისი შემაფასებელი ქულა (0-დან 100-ის ჩათვლით).

# • იმ შემთხვევაში თუ შემოტანილი ქულა მეტია ან ტოლია 90-ის, ტერმინალში გამოიტანე "Grade A".
# • თუ მისი ქულა მეტია ან ტოლია 70-ზე გამოიტანე "Grade B". 
# • თუ მომხმარებლის ქულა მეტია ან ტოლია 50-ზე ტერმინალში დაბეჭდე "Grade C"
# • ყველა დანარჩენ შემთხვევაში გამოიტანე  "Grade F" 

user_input = int(input("enter your pount: "))
if user_input >= 90:print("grade A")
if user_input >= 70:print("garde B")
if user_input >= 50:print("grade C")
else:
    print("grade F")