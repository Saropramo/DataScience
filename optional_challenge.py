print("\n\t\t Challange program")
fruit = "Apple" 
colour = "white" 
    food = "pizza" # compilation error1 - unnecessary indentation

print(f"\n My favourite food is " + Food) # logical error1 - variable name used 'Food' instead of 'food'
print (f"\n My favourite fruit is {fruit}") # compilation error2 - missing parantheses
print("\n My favourite colour is {colour}") # logical error2 - missing formating
print("\n the last letter of my favourite fruit is " + fruit[5]) # runtime error1 - accessing index out of range
