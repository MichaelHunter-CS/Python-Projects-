'''
Frequency Table that is sorted based on the smallest number at the top and the largest number at the bottom
'''

from collections import Counter

def frequency_table(numbers):
    table = Counter(numbers)
    numbers_freq = table.most_common()
    numbers_freq.sort()

    print("Numbers\tFrequency")
    for number in numbers_freq:
        print("{0}\t{1}".format(number[0], number[1]))

if __name__ == '__main__':
    scores = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
    frequency_table(scores)