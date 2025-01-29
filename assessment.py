#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""Python Skill Assessment (Total: 100 Marks)
Section 1: Basics (20 Marks)
Variable Manipulation (5 Marks)
Write a Python program to swap two numbers without using a third variable.

String Operations (5 Marks)
Write a program to count the number of vowels in a user-provided string.

List Operations (10 Marks)
Create a list of integers. Write a function to:

Find the maximum and minimum values in the list.
Reverse the list.
Section 2: Conditionals and Loops (30 Marks)
Prime Number Check (10 Marks)
Write a function to check if a given number is prime.

Pattern Printing (10 Marks)
Write a program to print the following pattern for n rows:

markdown
Copy
Edit
*
**
***
****
*****
Sum of Digits (10 Marks)
Write a Python function to calculate the sum of the digits of a given positive integer.

Section 3: Functions and Problem-Solving (30 Marks)
Palindrome Check (10 Marks)
Write a function to check if a given string is a palindrome (case insensitive).

Fibonacci Sequence (10 Marks)
Write a function to generate the first n terms of the Fibonacci sequence.

Custom Function (10 Marks)
Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.

Section 4: File Handling (20 Marks)
Reading and Writing to a File (20 Marks)
Write a program to:
Create a text file named test.txt and write some lines of text into it.
Read the file and display its content on the screen."""


# In[3]:


#1
a = 5
b = 10 

a,b = b,a

print("a-",a)
print("b-",b)


# In[8]:


#2
s = input("enter the string-")
count = 0
for i in s.lower():
    if i in "aeiou":
        count += 1
print(count)


# In[34]:


#3

import time

def max_min(numbers):
    if len(numbers) == 0:
        print("The list is empty")
        return None, None  # Return None values if list is empty

    min_val = numbers[0]
    max_val = numbers[0]
    
    for i in numbers:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    return max_val, min_val

# Input Handling
while True:
    try:
        int_numbers = input("Enter numbers separated by spaces: ")
        num = list(map(int, int_numbers.split()))  # Convert input to list of integers
        break
    except ValueError:
        print("Invalid input! Please enter only integers.")

# Measure execution time
start_time = time.time()  # Start time
maxi, mini = max_min(num)
end_time = time.time()  # End time

# Output Results
print("----------")
print(f"Max: {maxi}")
print(f"Min: {mini}")
print(f"Execution Time: {end_time - start_time:.15f} seconds")


# In[52]:


#4 
import time
start_time = time.time()
number = int(input("Enter the number - "))

if number == 0 or number == 1 or number == 2:
    print("Prime No")

for i in range(2,number):
    if number % i == 0:
        print("Not a Prime No")
        break
else:
    print("Prime No")
    
end_time = time.time()
final = end_time - start_time

print(final)
    

        
        


# In[53]:


#5

n = 6
for i in range(n):
    print("*" * i)
    


# In[55]:


#6
def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

num = [10,3,24,2]
sum_list(num)
    


# In[73]:


#7

def is_palindrome(s):
    return s == s[::-1]

test_string = "MADAM"
if is_palindrome(test_string):
    print(f"'{test_string}' is a palindrome.")
else:
    print(f"'{test_string}' is not a palindrome.")


# In[80]:


def fib(n):
    a = 0
    b = 1
    seq = [a]
    for i in range(n):
        a, b = b, a + b
        seq.append(a)
    return seq

print(fib(100))


# In[ ]:





# In[87]:


#9
def only_even(n):
    final_list = []
    for i in numbers:
        if i % 2 == 0:
            final_list.append(i)
            
    return final_list
 
    

num = input("Enter the number with spaces")
numbers = list(map(int,num.split()))
only_even(num)


# In[90]:


with open("test.doc","w") as file:
    file.write("hello ")
    file.write("shakeel")
    
with open("test.doc","r")as file:
    content = file.read()
    print(content)

