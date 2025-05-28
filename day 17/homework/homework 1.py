# 3) შექმენით ფუნქცია სახელწოდებით double_values რომელიც არგუმენტად მიიღებს სიას და
# დააბრუნებს ახალ სიას, სადაც თითოეული ელემენტი გაორმაგებული იქნება.
def double_values(lst):
    return [x * 2 for x in lst]

print(double_values([1, 2, 3, 4]))