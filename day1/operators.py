# '''

# Operators are the special symbols or 
# keywords in programming language that performs operations on variables and values


# 3 types
# arithemetic
# logical
# comparison

# '''

# a=5
# b=10

# print(a+b)  #addidtion
# print(a-b)  #subtractiom
# print(a*b)     #multiplication
# print(a/b)     #division  (float)
# print(a//b)    #floor division (int)
# print(a%b)     #modulus (remainder)
# print(a**b)    #exponentiation (sq)

# """
# logical operators  (true or false)

# and  ===> returns a true value when both conditions are true  
# or  ===> returns a true value if one condition meets with requirement
# not  ==> reverse the result

# """

# x = 10


# print(x > 5 and x < 20)
# print(x > 5 or x > 8)
# print(not(x > 50))


# print( x > 20  and x < 20)


'''
comparison operators

==  equal to 
!= not equal to 
>
<
<=
>=


'''

#assignments operator

# +=
# -=
# *=
# /=
# //=
# %=
# **=


# m = 10
# # m+=10

# print(m)

# m+=10
# print(m)

# m-=2
# print(m)

# m*=4
# print(m)

# m//=8
# print(m)

# m/=3
# print(m)

# if , else and elif

x = 10
y = 20


if x < y:
    print("x is greather then y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")


score = 50

if score >=90:
    print("grade A+")
elif score >= 80:
    print("grade A")
elif score >= 70:
    print("grade B")
elif score >= 60:
    print("Grade C")
else:
    print("Fail")


age = 30

if age < 13:
    print("child")
elif age < 20:
    print ("Teenager")
elif age < 60:
    print("Adult")
else:
    print("senior citizen")


char = 'b'

if char in ['a','e','i', 'o', 'u']:
    print("Vowel")
else: 
    print("consonant")



# question:

# 1. write a python program to check if number is even or odd

# 2.
# age based ticket price:
# age < 5 : free 
# age 5 - 18 : rs 100
# age 19 -60 : rs 200
# age > 60 : rs 150

# write a pragram that prints ticket price based on age

