print("\nString Manipulation\n")
str_manip = input("Enter a sentence : ")
str_length = len(str_manip)
print("Length of the string : ", str_length)
# replaces @ on all occurance of the last char present in the sentence 
last_str = str_manip[str_length -1]
str_rep = str_manip.replace(last_str,"@")
print("\n@ Replaced string : ", str_rep)
# prints last three character in reverse using slice
print("\nLast three charactes of the entered sentence in reverse order : " ,str_manip[-1:-4:-1])
# Slices first three characters and last two characters the sentence
First_three_char = str_manip[:3:]
Last_two_char = str_manip[-2::1]
print("\nFirst three charcters and last two characters of the entered sentence: ", First_three_char + Last_two_char, "\n")

      

