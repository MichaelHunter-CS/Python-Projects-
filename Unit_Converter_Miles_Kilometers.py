'''
Unit converter: Miles and Kilometers
'''

def print_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')

def km_miles():
    km = float(input('Enter the distance in kilometers and we will convert it to miles for you: '))
    miles = km / 1.609

    print('The distance that you have entered', km, 'is the distance of', miles, 'in miles')

def miles_km():
    miles = float(input('Enter the distance in miles and we will convert it to kilometers for you: '))
    km = miles / 1.609

    print('The distance that you have entered', miles, 'is the distance of', km, 'in kilometers')

if __name__ == '__main__':
    print_menu()
    choice = input('Choose an option from the menu: ')
    if choice == '1':
        km_miles()

    if choice == '2':
        miles_km()