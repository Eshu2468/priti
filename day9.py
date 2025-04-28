# # #functions

# # '''
# # Syntax

# def name_function(name):
#      print(f"hello, {name}!")

# name("manideep")


# '''


def greet(name):
    print(f"hello, {name}!")

# syntax
# def function_name(parameter):
#     return value 

def durgasoft(name):
    message = f"Hello, {name}! Welcome to python learning"
    return message

output =  durgasoft("Priti")
print(output)

akash = durgasoft("Akash")
print(akash)

bhavani = durgasoft("Bhavani")
print(bhavani)

A = durgasoft("Jahanavi")
print(A)


print(durgasoft("rajashekar"))

#add
def add(a,b):
    return a + b


print("sum is:" , add(10,4))

#online shopping
def calculated_discounts(price,discounted_percent):
    discount = (price * discounted_percent) / 100
    final_price = price - discount
    return final_price

print(calculated_discounts(10000,10))
print(calculated_discounts(7500,5))
print(calculated_discounts(20000,20))



import sys
print(dir(sys))

print(sys.builtin_module_names)
import math
print(dir(math))

print(math.sqrt(144))




x = lambda a: a+10

print(x(90))
print(x(29))
print(x(70))



data = [("a",85),("b",92),("c",76)]
# sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

# print(sorted_data)

def generate_ranks(data):
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    for rank, (name,score) in enumerate(sorted_data, start=1):
        print(f"Rank {rank} : {name} - {score}")

generate_ranks(data)
