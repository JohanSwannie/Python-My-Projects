# * Create a Calculator function with addition, subtraction, multiplication, and division

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def new_calculation():
    num1 = float(input("What's the first number?: "))
    for symbol in calc_dict:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = calc_dict[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    return answer

def ongoing_calculation(answer):
    for symbol in calc_dict:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num3 = float(input("What's the next number?: "))
    calculation_function = calc_dict[operation_symbol]
    new_answer = calculation_function(answer, num3)
    print(f"{answer} {operation_symbol} {num3} = {new_answer}")
    answer = new_answer
    return answer

calc_dict = {
    "+": add,   
    "-": subtract,
    "*": multiply,
    "/": divide
}

answer = new_calculation()

def determine_calculation(answer):
    return input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'q' to quit: ").lower()    

while True:
    current_calculation = determine_calculation(answer)
    if current_calculation == "y":
        answer = ongoing_calculation(answer)
    elif current_calculation == "n":
        answer = new_calculation()
    elif current_calculation == "q":
        break   
    
print("Thanks for using my Calculator - Goodbye!")