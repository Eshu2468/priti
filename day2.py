#slicing in python extracting a specific portion or subset of the sequence like

#string 
#list
#tuple
'''
syntax:

sequence[start: end : step]

start -> index where slicing start(inclusive)
end -> index where slicing ends (exclusive)
step -> how many steps to skip


'''

akash = "Rajshekar - data analyst"

print(akash[0:4])

print(akash[2:7])
print(akash[:5])
print(akash[3:])
print(akash[::2])  #step
print(akash[::-1])  #reverse string


numbers = [10,20,30,40,50]

print(numbers[1:4])
print(numbers[:])
print(numbers[3:])
print(numbers[:4])
print(numbers[::-1])


email = "mounikapriti@durgasoft.com"
domain = email[email.index("@")+1:]
print(domain)

print(1000+7)