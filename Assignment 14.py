print("**************************************************************LIST COMPREHENSION & GENERATOR EXPRESSION**************************************************************")
#Q.1- Write a python program to print the cube of each value of a list using list comprehension. 
l=[]
n=int(input('enter no.of values '))
for i in range (n):
    a=int(input())
    l.append(a)
l2=[]
l2=[i**3 for i in l]
print(l2)

#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
n=int(input('Enter range '))
lst1=[j for i in range (2,n) for j in range (i*2,n,i) ]
lst2=[x for x in range(2,n) if x not in lst1 or  x==2 ]
print(lst2)

#Q.3- Write the main differences between List Comprehension and Generator Expression.
'''In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The type of data returned by list comprehensions and generator expressions differs.
The generator yields one item at a time — thus it is more memory efficient than a list.
list_comp = [x ** 2 for x in range(10) if x % 2 == 0]
gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)
print(list_comp)
print(gen_exp)
'''
print("**************************************************************LAMBDA & MAP**************************************************************")
#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2, 36.5, 37.3, 37.8]
lam_f=list(map(lambda c:(c*(9/5)+32),Celsius))
print(lam_f)

#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
l=[2,8,9,12]
def square():
    lam_square=list(map(lambda x:x**2,l))
    print(lam_square)
s=square()

print("**************************************************************FILTER & REDUCE**************************************************************")

#Q.1- Filter out all the primes from a list.
lst=[1,2,3,4,5,6,8,7,9,10]
def is_prime(n):
    if n==2 or n==3:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
f = list(filter(is_prime, lst))
print(f)

#Q.2- Write a python program to multiply all the elements of a list using reduce.
from functools import *
lst = [1,6,8,9]
r = reduce(lambda x,y : x*y, lst)
print(r)

