# Question 1

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)

def countup(number):
    if number >= 0:
        print("Blastoff!")
    else:
        print(number)
        # Recursively call countup with number + 1
        countup(number + 1) 

# Here it chooses between countup or countdown based on input
def countup_or_countdown():
    num = int(input("Enter a number: "))

    if num > 0:
        countdown(num)
    elif num < 0:
        countup(num)
    else:
        countup(num) 
        # If input is 0, also count up 
        # (will immediately print 'Blastoff!')

countup_or_countdown()




# Question 2

def number_division():

    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    if divisor != 0:
        answer = dividend / divisor
        print("The result is ", answer)
    else:
        print("You can't divide a number that is more than zero with zero")


number_division()


# How to catch errors with try-except!
# Here is an example code

def number_division__():
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))
    
        product = dividend / divisor

        print("The answer is", product)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed in python!")
        print("There is no number that is more than zero that can be divided by zero")
        print("")
    except ValueError:
        print("Error: Please enter valid integers.")

# Python’s try-except is similar to JavaScript’s try-catch, 
# and both are used to handle errors without crashing the program. 
# I often use try-catch in JavaScript to manage exceptions, 
# and the same logic applies in Python, making it easy to write more robust, 
# error-resistant code.

