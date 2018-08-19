from bubblesort import *
from quicksort import *
from selectionsort import *
from insertionsort import *
from heapsort import *
from mergesort import *
from random import randint
from time import clock
from classifier import find_best_match


def in_order(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True

def random_array(n):
    test_array = []
    for i in range(n):
        test_array.append(randint(0, 1000000))
    return test_array;

def ascending_array(n):
    test_array = []
    for i in range(n):
        test_array.append(i)
    return test_array;

def descending_array(n):
    test_array = []
    for i in range(n):
        test_array.append(n - i)
    return test_array;

def benchmark(setup, f, ns, validate):
    results = []
    for n in ns:
        input_values = setup(n)
        start = clock()
        result = f(input_values)
        time_spent = int(round((clock() - start) * 1000))
        #print('N %i Time %i %s' % (n, time_spent, str(validate(result))))
        results.append([n, time_spent])
    return results


def run_for(f, test_cases):
    print('*' * 50)
    print('%s %s' % (f.__name__, setup.__name__))
    for test_case in test_cases:
        result = benchmark(test_case, f, range(10, 50, 1), in_order)
        best_match = find_best_match(result)
        
        


if __name__=='__main__':
    algorithms = [mergesort, quicksort, insertionsort, selectionsort, heapsort, bubblesort]
    max_name = max(map(lambda x : len(x.__name__), algorithms))
    test_cases = [random_array, ascending_array, descending_array]
    print('Sorting algorithm benchmark')
    print(' '*(max_name + 1) + '\t%s\t\t%s\t\t%s' % ('RAND', 'ASC','DESC'))
    for algorithm in algorithms:
        results = [algorithm.__name__]
        for test_case in test_cases:
            result = benchmark(test_case, algorithm, range(500, 5000, 500), in_order)
            best_match = find_best_match(result)
            results.append(best_match)
        print('\t'.join(map(lambda x : x.ljust(15), results)))
