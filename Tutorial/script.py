print("Hello world!")
print(" Updated code for test")

# variables in python require no type declaration
myint = 7
print(myint)

# floats in python
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# strings in python
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
mystring = "Don't worry about apostrophes"
print(mystring)

# integer addition
one = 1
two = 2
three = one + two
print(three)

# strings can be added together with simple addition
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#assignment can be done seperately
a, b = 3, 4
print(a,b)

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
    
# lists
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)
    
# append
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

# operators
number = 1 + 2 * 3 / 4.0
print(number)

# modulo
remainder = 11 % 3
print(remainder)

# exponents
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

# multiplying strings
lotsofhellos = "hello" * 10
print(lotsofhellos)

# list operators
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

# combine lists
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
    
    



