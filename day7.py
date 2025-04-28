# #Loops   
# # 
# # #looping means doing the same task again and agian until a condition is met 


# # types:
# # for loop
# # while loop




# #for loops and while loops


# Names = ['monika','bhavani','jahanavi','priti']
# # print(Names)


# # for a in Names:    #simple looping concepts
# #     print(a)

# # for a in "Priti":    #loop with strings
# #     print(a)


# Names = ['monika','bhavani','jahanavi','priti']

# # for a in Names:     #the break statements
# #     print(a)
# #     if a == "jahanavi":
# #         break


# # for a in Names:     #the break statements
# #     print(a)
# #     if a == "bhavani":
# #         break



# # for a in Names:                               #the continue statement
# #     if a == 'bhavani':
# #         continue
# #     print(a)



# for i in range (5):
#     print(Names)


# for akash in range(1 , 11):
#     if akash == 5:
#         print("stopped loop")
#         break
#     print(f'execting loop {akash}')




# for akash in range(1 , 11):
#     if akash == 7:
#         print("to be continued")
#         continue
#     print(f' loop {akash}')



# for i in range(1,6):
#     if i == 3:
#         break
#     print(i)

# for i in range(1,6):
#     if i == 4:
#         continue
#     print(i)



#whilw loop ---> can execute a set of statements as log as a condition is true.


a = 1

# while a < 6:
#     print(a)
#     a += 1



# while a < 6:
#     print(a)
#     if a == 4:
#         break
#     a += 1


# a=0
# while a < 6:
#     print(a)
#     if a == 4:
#         continue
#     a += 1


# a = 0
# while a < 8:
#     a += 2
#     if a == 4:
#         continue
#     print(a)

# priti = 1
# while priti < 6:
#     print(priti)
#     priti += 1
# else:
#     print(" priti is no longer less than 6 digit")


# i = 1
# while i <= 10:
#     if i == 6:
#         print(" stopping loop")
#         break
#     print(i)
#     i+=1



i = 10
while i < 50:
    i += 10
    if i == 30:
        print("skipping number 30")
        continue
    print(i)


abc = 1
while abc <= 3:
    print("HI")
    abc += 1

i = 5
while i > 0:
    print(i)