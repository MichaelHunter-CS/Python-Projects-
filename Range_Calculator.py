'''
Calculating the range
'''

def range_calc(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    # Calculating the range
    range = highest - lowest

    return lowest, highest, range

if __name__ == '__main__':
    donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
    lowest, highest, range = range_calc(donations)
    print("The lowest value is: {0}. The highest value is: {1}. The range is: {2}".format(lowest, highest, range))