print("\n String Replace ")
single_str = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print("\n given string : ",single_str)
# replaces the ! symbol with space
replace_str = single_str.replace("!", " ")
print("\n replace ! with space :",replace_str )
# changes the string to upper case
upper_str = replace_str.upper()
print("\n upper case string :", upper_str)
# prints string in reverse 
print("\n reverse string : ", upper_str[::-1],"\n")
