from math import log

def constant(N):
    return 1

def linear(N):
    return N

def superlinear(N):
    return N * log(N)

def superquadratic(N):
    return N** 2 * log(N)

def quadratic(N):
    return N ** 2

def cubic(N):
    return N ** 3

def exponential(N):
    return 2 ** N

def factorial(N):
    if N < 1:
        return 1
    return N * factorial(N - 1)

functions = {
    'O(1)': constant,
    'O(n)': linear,
    'O(n * log n)': superlinear,
    'O(n^2)': quadratic,
    'O(n^2 * log n)': superquadratic,
    'O(n^3)': cubic,
    #'O(2^n)': exponential,
    #'O(n!)': factorial,
}

def find_best_match(data):
    best_match = None
    best_fitness = None

    for name,f in functions.items():
        #print(name)
        k = best_multiplier(data, f)
        #print(k)
        fitness = calculate_fitness(data, f, k)
        if best_fitness == None or fitness < best_fitness:
            best_fitness = fitness
            best_match = name
    return best_match




def best_multiplier(data, f):
    sumOfX = 0.0
    sumOfY = 0.0
    for point in data:
        sumOfX += float(f(point[0]))
        sumOfY += float(point[1])
    return sumOfY / sumOfX

def calculate_fitness(data, f, k):
    error = 0
    for point in data:
        error += (k * float(f(point[0])) - float(point[1])) ** 2
    return error

def noisify(f, n):
    return max(f(i) + randint(-50, 50), 1)

if __name__ == '__main__':
    from random import randint
    for name, f in functions.items():
        test_array = []
        for i in range(1, 50):
            test_array.append([i, noisify(f, i)])
        #print(test_array)
        discovered_best_match = find_best_match(test_array)
        print('Generated %s detected as %s'%(name, discovered_best_match))
