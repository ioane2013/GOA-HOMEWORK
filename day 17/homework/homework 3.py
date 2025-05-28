# 5) შექმენით ფუნქცია და გადაეცით არგუმენტად სია. ფუნქციამ უნდა დააბრუნოს ახალი სია,
# რომლის თითოეული ელემენტიც უნდა იყოს კვადრატში აყვანილი.

def list(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result

print(list([5, 7, 9, 24]))