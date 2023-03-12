#5-2 More Conditional Tests

#strings

#true

print("The following should be True")

string_0 = "variable"
string_1 = "variable"

if string_0 == string_1:
    print("True")
else:
    print("False")

#false

print("The following should be False")

string_0 = "variable"
string_1 = "Variable"

if string_0 == string_1:
    print("True")
else:
    print("False")

#using lower

#true

print("The following should be True")

string_0 = "variable"
string_1 = "VARIABLE"

if string_0.lower() == string_1.lower():
    print("True")
else:
    print("False")

#false

print("The following should be False")

string_0 = "variable"
string_1 = "VARIABLE"

if string_0 == string_1:
    print("True")
else:
    print("False")


#using numbers

#true

print("The following should be True")

num_0 = 10
num_1 = 5

if num_0 >= num_1:
    print("True")
else:
    print("False")

#false

print("The following should be False")

num_0 = 10
num_1 = 5

if num_0 <= num_1:
    print("True")
else:
    print("False")

#the OR keyword

#true

print("The following should be True")

num_0 = 10
num_1 = 5
num_2 = 1000

if num_0 > num_1 or num_2 < num_1:
    print("True")
else:
    print("False")

print("The following should be False")

num_0 = 10
num_1 = 5

if num_0 > num_1 and num_2 < num_1:
    print("True")
else:
    print("False")

# conditiona lists

print("The following should be True")

cars = ["audi","bmw","subaru","toyota"]

if "audi" in cars:
    print("True")
else:
    print("False")

print("The following should be False")


if "Honda" in cars:
    print("True")
else:
    print("False")