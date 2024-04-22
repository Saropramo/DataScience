# Using while loop
print("\n \t Calculate and print the average")
print(" \t -------------------------------\n")
count = 0
total = 0
number = 0
# while loop to get numbers from user until user inputs -1
# prints the average of the entered numbers except -1
while number != -1:
    number  = int(input("Enter a number: "))
    if number  != -1:
        total = total + number 
        count = count + 1
        continue
# checks if any number is entered to caculate the average 
# and displays message accordingly
# prints no numbers are entered if the user inputs -1 as the first input
if count == 0 :
    
    print("\nNo numbers entered to calculate average \n")
else:
    average =  round(float(total/count),2)
    print("\nTotal count of numbers entered except -1 : ", count)         
    print("\nAverage of all the numbers entered is ", average)

