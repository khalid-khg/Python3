num1 = 5
num2 = 6
print(num1 > num2)
print(num1 < num2)
print(5 > 6)
print(6 > 5)
print( 5 == 6)
print(5 == 5)
print(5 != 6)
print(5 != 5)
print(5 >= 6)
print(6 >= 6)
print(7 >= 6)
print(5 <= 6)

print(True and True) # True
print(True and False) # False
print(False and False) # False
a,b = 1,2
print(a)
print(b)
print(a == a and b == b) # True
print(a == a and b < a) # False
print(a > b and b < a) # False


print(True or True) # True
print(True or False) # True
print(False or False) # False
print(a == a or b == b) # True
print(a == a or b < a) # True
print(a > b or b < a) # False

print(not True) # False
print(not False) # True

print(not (a != 5)) # False
print(not (a == 5)) # True
