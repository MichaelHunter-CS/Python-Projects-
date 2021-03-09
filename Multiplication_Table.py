'''
Multiplication Table
'''

def multi_table(num1):
    for i in range(1, 11):
        print('{0} X {1} = {2}'.format(num1, i, num1 * i))

if __name__ == '__main__':
    num1 = input("Enter a number")
    multi_table(float(num1))