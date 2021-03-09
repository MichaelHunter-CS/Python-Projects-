'''
Find the factors of an integer
'''

def factors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

if __name__ == '__main__':
    number = input("Enter the number that you wish to find the factors of: ")
    number = float(number)

    if number > 0 and number.is_integer():
        factors(int(number))
    else:
        print("You need to enter a positive number, please try again")