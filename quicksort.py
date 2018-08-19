from random import randint

def quicksort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def worker(low, high):
        if low >= high:
            return # One element left
        pivotIndex = randint(low, high)
        pivot = arr[pivotIndex]
        swapCount = 1
        swap(pivotIndex, low)
        pivotIndex = low
        topIndex = high
        while pivotIndex < topIndex:
            if arr[pivotIndex + 1] < pivot:
                swap(pivotIndex, pivotIndex + 1)
                pivotIndex += 1
            else:
                swap(pivotIndex + 1, topIndex)
                topIndex -= 1
            swapCount += 1
        # Sort low
        worker(low, pivotIndex - 1)
        # Sort high
        worker(pivotIndex + 1, high)
        
                
    worker(0, len(arr) - 1)
    
    return arr

if __name__=='__main__':
    print(''.join(quicksort(list('QUICKSORT'))))
