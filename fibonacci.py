# Function
def fibonacci_sequence(number):
    if number <= 1:
        return number
    else:
        return(fibonacci_sequence(number - 1) + fibonacci_sequence(number - 2))

# Main Program
terms_number = int(input("Enter how many terms you want entered: "))
if terms_number <= 0:
    print("You must enter a positive number, please try again")
else:
    print("Fibonacci sequence: ")
    for i in range(terms_number):
       print(fibonacci_sequence(i))
