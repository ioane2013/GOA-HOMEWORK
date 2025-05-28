# 4) შექმენით ფუნქცია, რომელსაც არგუმენტად გადასცემთ სიას
#  (ჩათვალეთ, რომ სიაში ინახება Integer-ი რიცხვები)
# ამ ფუნქციამ საბოლოოდ უნდა დააბრუნოს სიიდან მხოლოდ ლუწი რიცხვები.


def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

print(get_even_numbers([16, 17, 28, 31]))