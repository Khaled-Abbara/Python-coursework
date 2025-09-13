# Part 1

#  This is a function that calculates and prints the circumference of a circle
def print_circum(radius): # radius is the parameter
    pi = 3.14159 # Local variables
    print(2 * pi * radius) # circumference = 2 * pi * radius
    
# Three function calls with different radius values as argumants 
print_circum(3)
print_circum(7)
print_circum(11)


# Part 2

def online_store():

    # Inner function to calculate the price of selected items or combos
    def calculate_price(option):
        item1 = 200.0
        item2 = 400.0
        item3 = 600.0

        # Return price information based on selected option
        if option == "A":
            return "Item 1                      " + str(item1)
        if option == "B":
            return "Item 2                      " + str(item2)
        if option == "C":
            return "Item 3                      " + str(item3)
        
        # Combos apply a discount on total price
        if option == "D":
            return "Combo 1(Item 1 + 2)         " + str((item1 + item2) * 0.90)
        if option == "E":
            return "Combo 2(Item 2 + 3)         " + str((item2 + item3) * 0.90)
        if option == "F":
            return "Combo 3(Item 1 + 3)         " + str((item1 + item3) * 0.90)
        if option == "G":
            return "Combo 4(Item 1 + 2 + 3)     " + str((item1 + item2 + item3) * 0.75)
        
    # Inner function to print the receipt
    def recipt():
        print("Online Store")
        print("---------------------")
        print("Product(S)                  Price")
        print(calculate_price("A"))
        print(calculate_price("B"))
        print(calculate_price("C"))
        print(calculate_price("D"))
        print(calculate_price("E"))
        print(calculate_price("F"))
        print(calculate_price("G"))
        print("________________________")
        print("For Delivery Contact:98764678899")
        print(" ")
        
    # returns the output of the recipt function
    return recipt()

# this runs the program
online_store()