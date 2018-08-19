def selectionsort(arr):
    bottom = 0
    while bottom < len(arr):
        smallest = arr[bottom]
        smallest_i = bottom
        for i in range(bottom + 1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_i = i
        for i in reversed(range(bottom, smallest_i)):
            arr[i + 1] = arr[i]
        arr[bottom] = smallest
        bottom += 1
        
    return arr

if __name__=='__main__':
    print(''.join(selectionsort(list('SELECTIONSORT'))))
