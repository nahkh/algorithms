def bubblesort(arr):
    def swap(i, j):
        arr[i],arr[j] = arr[j], arr[i]
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                swap_occurred = True
                swap(i, i - 1)
    return arr

if __name__=='__main__':
    print(''.join(bubblesort(list('BUBBLESORT'))))
