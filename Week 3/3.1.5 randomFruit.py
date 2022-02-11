# This program prints out random fruits from a list
import random
fruits = ['Apple', 'Banana', 'Pear', 'Orange', 'Avocado', 'Guava']

#We want a random number between and length -1
index = random.randint(0, len(fruits)-1)

#The fruit chosen will be the fruits list with the random index number
fruit = fruits[index]
print ('Here is your random fruit. {}!'.format(fruit))