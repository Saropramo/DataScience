print("\n\t\t Alternative string manipulation")
print("\t\t *******************************")

alternate_letters_upper_lower = "" #variable for printing alternate letters in upper and lower cases

string_entered = input("\n Enter a string : ").strip() #receive user input
while string_entered.isnumeric(): #check if user input is valid string and not a number
    print("Enter a valid string")
    string_entered = input("\n Enter a string : ").strip() #ask for user input until user enters a valid string

for i in range(len(string_entered)): # converts alternate letters into upper and lower
    if i % 2 == 0:
        alternate_letters_upper_lower += string_entered[i].upper()
    else:
        alternate_letters_upper_lower +=  string_entered[i].lower()

#display alternate letters in upper and lower cases
print(f"\n Alternative letters upper and lower case : {alternate_letters_upper_lower}") 

split_string_entered = string_entered.split()  #splits string and stores as list  
for i in range(0,len(split_string_entered)): # converts alternate words into upper and lower
    if i % 2 == 0:      
        split_string_entered[i] = split_string_entered[i].lower()       
    else:     
        split_string_entered[i] = split_string_entered[i].upper()      
#display alternate words in upper and lower cases
print(f"\n Alternative words upper and lower case : {' '.join(split_string_entered)} \n")  
    




