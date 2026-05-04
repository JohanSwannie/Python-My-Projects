
def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a // b

print("Use my simple Calculator")
print("1 = Add | 2 = Subtract | 3 = Multiply | 4 = Divide")

while True:
   choice = int(input("Choose your operation - 1 | 2 | 3 | 4   "))
   if choice == 1 or choice == 2 or choice == 3 or choice == 4:
      break
   
while True:
   try:
      num1 = int(input("Please choose your first number   "))
      break
   except ValueError:
      print("That is not a valid number")
   
while True:
   try:
      num2 = int(input("Please choose your first number   "))
      break
   except ValueError:
      print("That is not a valid number")
      
match choice:
   case 1:
      print(f"{num1} + {num2} = {add(num1, num2)}")
   case 2:
      print(f"{num1} - {num2} = {subtract(num1, num2)}")
   case 3:
      print(f"{num1} times {num2} = {multiply(num1, num2)}")
   case 4:
      print(f"{num1} divided by {num2} = {divide(num1, num2)}")
