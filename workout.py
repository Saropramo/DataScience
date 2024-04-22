"""name = input("What is your name? ")
num1 =int(input("Give me a number: "))
num2 =int(input("Give me another number : "))
user_mul_answer =int(input("What is the product of those 2 numbers : "))
if user_mul_answer == (num1 * num2):
    print("You are correct!!", name)
else:
    print ("Wrong answer", name) """

"""txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)"""

"""for x in range(1, 6):
    for y in range(1, 6):
        print(f"{x} * {y} = {x*y}")
        print("")

txt = "welcome to the jungle"

x = txt.split()

print(x)

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#")

print(x)
print(len(x))

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

class myObj:
  name = "John"

y = myObj()

x = isinstance(y, myObj)
print(x)

hello_world =lambda : print("Hello world")
hello_world()
greeting = lambda : print("why hello there")
greeting()


def add_2(x):
   return  x + 2

print(add_2(6))

add_two = lambda x : x+ 2
print(add_two(5))

cube = lambda y: y ** 3
print(cube(3))


old_greeting = lambda : print("Hello world")
greeting = lambda name: print(f"Welcome back {name}")


old_greeting()
greeting("Saran")

get_username = lambda : input("please enter your user name: ")
#print(get_username())

new_user = get_username()
print(f"This is the new user {new_user}")

   
def factorial(n):
    print(n)
    if n == 1:
        return 1
    else:
        return n * (factorial(n-1))
print(f"factorial : {factorial(10)}")


show_user = lambda user = input("please enter a username: ") : print(f"Welcome {user}")
show_user()


def drop_one(sample_string,[:index_range = 0]):
if inde
print(Sample_string[:in])"""

'''import re
print(re.search(r"[$#]" , "b$arry$"))
print(bool(89374)) #returns true
print(bool(0)) #returns false '''



item_type = [
            "number of rupees",
            "goblin horns", 
            "potions",
            "unicorn horns",
                "dragon tongues"]

item_counts = [100000, 25, 10, 1, 0]
item_dict = {}
#using enumerate to create a dict out of 2 lists
"""
for index, value in enumerate(item_type):
    item_dict[value] = item_counts[index] 

for index in range(len(item_type)):
    item_dict[item_type[index]] = item_counts[index]
print(item_dict)
"""
item_dict = dict(zip(item_type, item_counts))
print(item_dict)