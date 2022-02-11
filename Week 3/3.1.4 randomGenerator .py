#Program that prints out a random number between 1 and 10
import random

from numpy import number
print('Please type two numbers to generate a random number between them')
number1 = int(input('Please choose number: '))
number2 = int(input('Please choose another number: ',))
randomNumber = random.randint(number1,number2)

print('The random number between {} and {} is {}'.format(number1, number2, randomNumber) )
