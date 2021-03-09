'''
-b formula
'''

def roots(a, b, c):
    D = (b*b - 4*a*c)**0.5
    pos_x = (-b + D) / (2**a)
    neg_x = (-b - D) / (2**a)

    print('pos_ans: {0}'.format(pos_x))
    print('neg_ans: {0}'.format(neg_x))

if __name__ == '__main__':
    a = input('Enter the value of a: ')
    b = input('Enter the value of b: ')
    c = input('Enter the value of c: ')
    roots(float(a), float(b), float(c))