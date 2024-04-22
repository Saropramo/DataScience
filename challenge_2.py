
# Request user data
string_fav = input("Enter your favourite restaurant: ")
int_fav = int(input("Enter your favourite number: "))
# Display user data
print("your favourite restaurant is ", string_fav)
print("Your favourite number is ", int_fav)

# print(int(string_fav))
# If I try to convert string_fav to int it shows error message as 
# ValueError: invalid literal for int() with base 10: 'xyz'. 
# It shows this error as it can't convert non digits into integers