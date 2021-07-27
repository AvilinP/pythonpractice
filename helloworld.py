#This is a comment 
print("Hello, world!")
if 5 > 2:
    print("Five is greater than two!")

# variables are instantly declared and can change both type and content
x = 5
x = "Avilin"

print(x)
print(type(x)) # type() shows varible type

#variables are case-sensitive 
X = 5
x = "Avilin"
print(x)
print(X)

#possible var names 
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 

print(myvar2)

# assign multiple varibles
# Note: Make sure the number of variables matches the number of values, 
# or else you will get an error.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One value to multiple varibles 
x = y = z = "Orange"
print(x)
print(y)
print(z)

# unpack a collection 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# output variables
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

# + sign and numbers. can't combine + with different types
# ex: x = 5 y = "hej" <-- gives error
x = 5
y = 10
print(x + y)


# data types
o = tuple((10.5, 11.2, 12.1))
print(type(o))

#convert data types
x = 1
y = 2.8
z = 1j # can not convert complex numbers

a = float(x)
print(a)

b = int(y)
print(b)

c = complex(x)
print(c)

