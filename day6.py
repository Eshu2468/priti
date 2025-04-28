#python dictionaries : used to store data value in key-value pair
#it is a collections of ordered data. changeable and do not allow duplicates

pythonn = {
   "institute":"Durgasoft",
   "Mode": "Online",
   "year":2025,
}


print(pythonn)
# print(pythonn['institute'])  #dictionary item are presented in key:value pairs and can be referred to by using key name.
# print(pythonn["Mode"])

print(len(pythonn))



#dictionaries will accpect in value any kind of data types
pythonn = {
   "institute":"Durgasoft",
   "Mode": "Online",
   "year":2025,
    "course": ["Da", "FSD","DevOps","Linux OS","Web dev"]
}

#Dictionaries will not allow duplicates

pythonn = {
   "institute":"Durgasoft",
   "Mode": "Online",
   "year":2025,
   "year": 2026
}

print(type(pythonn))

#dict()  constructor is a special method in a class that is automatically called when an object is create.

amulya = dict(name = "amulya", age = 25, country = "India" )

print(amulya)


#nested dict

company = {
   "emp1" : {
       "name": "amulya",
       "year": 2021
   },
   "emp2" : {
       "name":"prithi",
       "year": 2022
   },
   "emp3": {
       "name": "mahaboob",
       "year": 2024
   }
}
#loops to diplay value in vertical form
for x, obj in company.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

# print(company)
# print(company["emp3"])



'''quit
python collection (arrays)

1. list : is a collection of ordered data and changable. allow duplicate value.
2. Tuple ; is a collection of ordered data and it is not changeable and allow duplicates.
3. set : it is a collection of unordered data , it records only unquie values and doesn't allow duplicates
4. Dictionaries : collection of ordered data and changable and no duplicates
'''

# moha= [1,2,2,2,2,2,2,2,22,]  #list
# print(moha)
# pritii = {1,2,2,2,2,2,2,2,22}  #set
# print(pritii)
# a = (1,2,2,2,2,2,2,2,22)   #tuple
# print(a)


# moha.append(4)  #list
# print(moha)


# a.append(2000)  #tuple
# print(a)
# #it throws an error bcoz tuple in unchangeable or immutable

'''
list are mutable  and allow modifications after creation.
Tuples are immutable , prevents modifications after creation.
'''
