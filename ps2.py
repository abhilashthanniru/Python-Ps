# max and min numbers in a function
def max_min_sum(list_passed):
    if len(list_passed)==0:
        print("Not a possible in empty list")
        return  
    max=list_passed[0]
    min=list_passed[0]
    sum=list_passed[0]
    for i in list_passed:
        max = i if i > max else max
        min = i if  i < min else min
        sum+=i
    return max ,min,sum
list1=[1,2,0.7,-32,11,0,-3]
tup1=max_min_sum(list1)
if tup1:
    print("max",tup1[0])
    print("min",tup1[1])
    print("sum",tup1[2])
else:
    print("Not a possible in empty list")

# find if an element exists in the list
# def list_passed(list1, search_num):
#     for i in list1:
#         if i== search_num:
#             return True
#     return False
# list1 = [1,2,0.7,-32,11,0,-3]
# search_num2=int(input("enter a number"))

# if list_passed(list1,search_num2):
#     print("found")
# else:
#     print("not found")

# # code for taking list by users
# list2=[]
# size_of_list=int(input("enter a size of list"))
# for i in range(size_of_list):
#     num1=float(input("enter a number"))
#     list2.append(num1)
# print(list2)

# feb 15
# count of characters
# str1=input("enter a string")
# res={}
# for k in str1:
#     if k in res:
#         res[k]+=1
#     else:
#         res[k]=1
# print(res)


# count of characters
# list1=["Deeksha","ammu","random"]
# final_res=[]
# for str in list1:
#     res={}
#     for k in str:
#         if k in res:
#             res[k]+=1
#         else:
#             res[k]=1

#     final_res.append({str:res})
# print(final_res)


# second largest numbers
# Disadvantages-Does not work for duplicate values.
list1=[4,8,9,10,-11,-3,6]   # this is one way to find second largest element
list1.sort()
print(list1)
print(list1[-2])


# another way to find second largest element
max, min, sum =  max_min_sum(list1)
second_largest=-1000
for i in list1:
    if i != max and i > second_largest:
        second_largest = i
print(second_largest)




# you have to find duplicates elemnts in tha list and unique elements
my_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8, 9]

duplicates = []
uniques = []

for num in my_list:
    if my_list.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
    elif my_list.count(num) == 1:
        uniques.append(num)

print("Duplicate Elements:", duplicates)
print("Unique Elements:", uniques)

# linear search


    

# Write a program to print numbers from -1 to -10
def numbers():
    for i in range(-1,-11,-1):
        print(i)
numbers()

for i in range(-1,-11,-1):
    print(i)

# sum of digits in a number and add when its is even
# def sum_of_digits(num):
#     sum=0
#     if num % 2 == 0:


# prime or not a prime
# def check_if_prime(num):
#     if num <=1:
#         return False
#     for i in range(2,num+1):
#         if num % i == 0:
#             return False
#     return True
# input=int(input("enter a number"))

# print (input,"prime number") if check_if_prime(input) else print(input,"not a prime number")



# range of numbers -check prime or not in certain range
def prime_range(num):
    if num <=1:
        return False
    for i in range(2, num + 1):
        return False
    return True

num1=int(input("enter a number"))
num2=int(input("enter a number"))
for num in range(num1,num2+1):
    print(num,"prime number") if prime_range(num) else print(num,"not a prime number")

# write a program to print sum of non-primes digits in a given number
def sum_nonprimes(n):
    primes={0,1,6,8,9,4}
    return 




# write a program to print max prime digit in a certain number









# compare first digit and last digit in a number (print equal if there are equal)
def compare_first_last_digit(n):
    n = str(n)  
    if n[0] == n[-1]:  
        return "Equal"
    else:
        return "Not Equal"

num = int(input("Enter a number: "))
print(compare_first_last_digit(num))


# print nth fibnocci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0  
    elif n == 2:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter N: "))
print(f"{num}th Fibonacci number:", fibonacci(num))

# print non-fibnocci numbers in a given range (1 to 100)





# reverse a number in a negative numbers
def reverse_number(n):
    if n >= 0:
        return int(str(n)[::-1])
    else:
        return -int(str(n)[:0:-1])

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))






# write a program to check the index
def search_a_num(list, search_num):
    """Search for a number in the list and print its index."""
    index = 0  
    for num in list:
        if num == search_num:
            return index  
        index += 1  
    return -1  

list = [2, 4, 6, 8, 10, 0.2, -3]
search_num = float(input("Enter a number to search: "))  

index = search_a_num(list, search_num)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

# max and min numbers in a function
def max_min_sum(list_passed):
    if len(list_passed)==0:
        print("Not a possible in empty list")
        return  
    max=list_passed[0]
    min=list_passed[0]
    sum=list_passed[0]
    for i in list_passed:
        max = i if i > max else max
        min = i if  i < min else min
        sum+=i
    return max ,min,sum
list1=[1,2,0.7,-32,11,0,-3]
tup1=max_min_sum(list1)
if tup1:
    print("max",tup1[0])
    print("min",tup1[1])
    print("sum",tup1[2])
else:
    print("Not a possible in empty list")

# find if an element exists in the list
# def list_passed(list1, search_num):
#     for i in list1:
#         if i== search_num:
#             return True
#     return False
# list1 = [1,2,0.7,-32,11,0,-3]
# search_num2=int(input("enter a number"))

# if list_passed(list1,search_num2):
#     print("found")
# else:
#     print("not found")

# # code for taking list by users
# list2=[]
# size_of_list=int(input("enter a size of list"))
# for i in range(size_of_list):
#     num1=float(input("enter a number"))
#     list2.append(num1)
# print(list2)

# feb 15
# count of characters
# str1=input("enter a string")
# res={}
# for k in str1:
#     if k in res:
#         res[k]+=1
#     else:
#         res[k]=1
# print(res)


# count of characters
# list1=["Deeksha","ammu","random"]
# final_res=[]
# for str in list1:
#     res={}
#     for k in str:
#         if k in res:
#             res[k]+=1
#         else:
#             res[k]=1

#     final_res.append({str:res})
# print(final_res)


# second largest numbers
# Disadvantages-Does not work for duplicate values.
list1=[4,8,9,10,-11,-3,6]   # this is one way to find second largest element
list1.sort()
print(list1)
print(list1[-2])


# another way to find second largest element
max, min, sum =  max_min_sum(list1)
second_largest=-1000
for i in list1:
    if i != max and i > second_largest:
        second_largest = i
print(second_largest)




# you have to find duplicates elemnts in tha list and unique elements
my_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8, 9]

duplicates = []
uniques = []

for num in my_list:
    if my_list.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
    elif my_list.count(num) == 1:
        uniques.append(num)

print("Duplicate Elements:", duplicates)
print("Unique Elements:", uniques)

# linear search


    

# Write a program to print numbers from -1 to -10
def numbers():
    for i in range(-1,-11,-1):
        print(i)
numbers()

for i in range(-1,-11,-1):
    print(i)

# sum of digits in a number and add when its is even
# def sum_of_digits(num):
#     sum=0
#     if num % 2 == 0:


# prime or not a prime
# def check_if_prime(num):
#     if num <=1:
#         return False
#     for i in range(2,num+1):
#         if num % i == 0:
#             return False
#     return True
# input=int(input("enter a number"))

# print (input,"prime number") if check_if_prime(input) else print(input,"not a prime number")



# range of numbers -check prime or not in certain range
def prime_range(num):
    if num <=1:
        return False
    for i in range(2, num + 1):
        return False
    return True

num1=int(input("enter a number"))
num2=int(input("enter a number"))
for num in range(num1,num2+1):
    print(num,"prime number") if prime_range(num) else print(num,"not a prime number")

# write a program to print sum of non-primes digits in a given number
def sum_nonprimes(n):
    primes={0,1,6,8,9,4}
    return 




# write a program to print max prime digit in a certain number









# compare first digit and last digit in a number (print equal if there are equal)
def compare_first_last_digit(n):
    n = str(n)  
    if n[0] == n[-1]:  
        return "Equal"
    else:
        return "Not Equal"

num = int(input("Enter a number: "))
print(compare_first_last_digit(num))


# print nth fibnocci number
def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0  
    elif n == 2:
        return 1  
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter N: "))
print(f"{num}th Fibonacci number:", fibonacci(num))

# print non-fibnocci numbers in a given range (1 to 100)





# reverse a number in a negative numbers
def reverse_number(n):
    if n >= 0:
        return int(str(n)[::-1])
    else:
        return -int(str(n)[:0:-1])

num = int(input("Enter a number: "))
print("Reversed number:", reverse_number(num))






# write a program to check the index
def search_a_num(list, search_num):
    """Search for a number in the list and print its index."""
    index = 0  
    for num in list:
        if num == search_num:
            return index  
        index += 1  
    return -1  

list = [2, 4, 6, 8, 10, 0.2, -3]
search_num = float(input("Enter a number to search: "))  

index = search_a_num(list, search_num)
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

# max and min numbers in a function
def max_min_sum(list_passed):
    if len(list_passed)==0:
        print("Not a possible in empty list")
        return  
    max=list_passed[0]
    min=list_passed[0]
    sum=list_passed[0]
    for i in list_passed:
        max = i if i > max else max
        min = i if  i < min else min
        sum+=i
    return max ,min,sum
list1=[1,2,0.7,-32,11,0,-3]
tup1=max_min_sum(list1)
if tup1:
    print("max",tup1[0])
    print("min",tup1[1])
    print("sum",tup1[2])
else:
    print("Not a possible in empty list")

# find if an element exists in the list
# def list_passed(list1, search_num):
#     for i in list1:
#         if i== search_num:
#             return True
#     return False
# list1 = [1,2,0.7,-32,11,0,-3]
# search_num2=int(input("enter a number"))

# if list_passed(list1,search_num2):
#     print("found")
# else:
#     print("not found")

# # code for taking list by users
# list2=[]
# size_of_list=int(input("enter a size of list"))
# for i in range(size_of_list):
#     num1=float(input("enter a number"))
#     list2.append(num1)
# print(list2)

# feb 15
# count of characters
# str1=input("enter a string")
# res={}
# for k in str1:
#     if k in res:
#         res[k]+=1
#     else:
#         res[k]=1
# print(res)


# count of characters
# list1=["Deeksha","ammu","random"]
# final_res=[]
# for str in list1:
#     res={}
#     for k in str:
#         if k in res:
#             res[k]+=1
#         else:
#             res[k]=1

#     final_res.append({str:res})
# print(final_res)


# second largest numbers
# Disadvantages-Does not work for duplicate values.
list1=[4,8,9,10,-11,-3,6]   # this is one way to find second largest element
list1.sort()
print(list1)
print(list1[-2])


# another way to find second largest element
max, min, sum =  max_min_sum(list1)
second_largest=-1000
for i in list1:
    if i != max and i > second_largest:
        second_largest = i
print(second_largest)




# you have to find duplicates elemnts in tha list and unique elements
my_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 8, 9]

duplicates = []
uniques = []

for num in my_list:
    if my_list.count(num) > 1 and num not in duplicates:
        duplicates.append(num)
    elif my_list.count(num) == 1:
        uniques.append(num)

print("Duplicate Elements:", duplicates)
print("Unique Elements:", uniques)

# linear search