# Program that read two numbers and output the integer answer and remainder

# Code that asks for the user imput for numbers 'x' and 'y' and set them as integer
from math import remainder


x = int(input('Enter the first number: '))
y = int(input('Enter the second number you want to divide by: '))

# Recording the Answer from 'x//y' in the variable answer.
answer = int(x//y) #// gives the interger from the division
remainder = x%y # % gives the remainder from the division
print('{} divided by {} is {} with remainder  {} '.format(x, y, answer, remainder ))