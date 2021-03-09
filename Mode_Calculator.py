'''
Calculating the Mode
'''

from collections import Counter

def mode_calc(numbers):
    count = Counter(numbers)
    mode = count.most_common(1)
    return mode[0][0]

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    mode = mode_calc(scores)
    print("The mode score over is {0}".format(mode))