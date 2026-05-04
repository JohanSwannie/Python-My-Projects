from random import randint

import math

# * Set up a list of numbers

numbers_list = []

for _ in range(50):
   number = randint(1, 250)
   numbers_list.append(number)
   
# * Determine the smallest number in the list - The longer way

smallest_number = math.inf

for x in numbers_list:
   if x < smallest_number:
      smallest_number = x
      
print(f"The smallest number in the list is {smallest_number}")

# * Determine the smallest number in the list - The short way

print(f"The smallest number in the list is {min(numbers_list)}")
   
# * Determine the biggest number in the list - The longer way

biggest_number = -math.inf

for x in numbers_list:
   if x > biggest_number:
      biggest_number = x
      
print(f"The biggest number in the list is {biggest_number}")

# * Determine the biggest number in the list - The short way

print(f"The biggest number in the list is {max(numbers_list)}")

   
   
