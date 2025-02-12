# Variable & data type
p = 5 #p is 5
q = "Jacob" 
print(p) 
print(type(p)) #get the type
print(q)
print(type(q))
n = 7
n = "Oha" 
n = 'Oha' #the both are same
print(n)
#casting
name = str(14) #it will be "14"
print(name)
number = int(14) #it will be 14
print(number)
decimal = float(14) #it will be 14.0
print(decimal)
#assing multiple value
a, b, c = "apple", "manggo", "banana"
print(a, b, c)
a = b = c = "fruits"
print(a)
#unpacking
fruits = ["apple", "manggo", "banana"]
a,  b, c = fruits
print(b)

# String
course = "Electronic for Everyone"
print(course.upper())
print(course.find('c'))
print(course.find('Everyone'))
print(course.replace('Electronic', '3'))
print(course.__len__())
print('for' in course)
print(course)

# Operator
# Arithmatic operator 
print(10+2)
print(10-4)
print(10-12)
print(2*4)
print(6/3)
print(3**2)
print(5/2)
print(5//2)
print(9 % 3)

# Assignment Operator
x = 10 # let's declare variable
y = 20
x += 3
print("x=",x)
y -= 2
print("y=",y)
x *= 3
print("x=",x)
y /= 2
print("y=",y)
x %= 4
print("x=",x)
y //= 3 
y = int(y)
print("y=",y)
x **= 3
print("x=",x)
y &= 3
print("y=",y)
x |= 3
print("x=",x)
y ^= 2
print("y=",y)
x >>= 2
print("x=", x)
y <<= 2
print("y=", y)
print("x=",x:=3)

# Operator Precendence
print(8 * 9 + 10)
print(8 * (9 + 10))

# Comaprison Operator
'''
>   (grater than to)
>=  (grater than or equal to)
<   (less than to)
<=  (less than or equal to )
==  (equal to)
!=  (not equal to)

result :
True (1)    = yes
False (0)   = no
'''
z = 5 > 3
print(z)
z = 3 < 1
print(z)
z = 3 >= 3
print(z)
z = 4 <= 6
print(z)
z = 3 == 3
print(z)
z = 3 != 3
print(z)
print(type(z))

# Logical Operator
age = 20
print(age > 10 and age < 30) # both must be True
price = 80.9
print(price > 0 or price < 84) # at least one is True
print(not(price > 40)) # True value can be False

# Bitwise Operator (later)

# If Statements
agefif = 35

if agefif > 40:
    print("you're look pretty old")
elif agefif > 30:
    print("you are adult")
elif agefif > 20:
    print("you're young")
else:
    print("you're so young")
print("done")
# short hand if
if agefif == 30: print("it's same") 
# short hand if else 
print("you're young") if agefif > 20 else print("you're so young") 
# (ternary operators or conditional expression)
  
# nested if
x = 9

if x > 10:
    print("lebih dari 10")
    if x > 20:
        print("dan juga lebih dari 20")
    elif x == 20 :
        print("sama dengan 20")
    else :
        print("kurang dari 20")
else :
    print("kurang dari 10")

# While loops
i = 1
while i < 6:
    print(i)
    i += 1
    if i == 4:
        print("stop")
        break

# For loops
for d in range(0, 10, 3):
    print(d)

for i in range(10):
    print(i)
else :
    print("ok")

kelas = ['A', 'B', 'C']
murid = ['Supri', 'Agus', 'Setiawan']

for i in kelas:
    for j in murid:
        print(i, j)

print("pass in for loops")
for x in [0, 10, 11]:
    pass

# List
mylist = ['banana', 'apple', 'strawberry', 'banana', 'coconut', 'mete', 'almond']
print(mylist)
print(mylist[0])
print(mylist[-1])
print(mylist[-5:-1])
print(mylist[:-5])
print(mylist[-3:])


"""
# Input/Output (I/O)
reviewer = str(input("Berikan masukan anda : "))
print(reviewer)
print("Terimakasih untuk masukan yang diberikan, kami sangat menghargai ide anda dan akan kami pertimbangkan sepenuhnya! ")
"""