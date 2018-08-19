def mergesort(arr):
    def worker(low, high):
        if low >= high:
            return
        midpoint = ((high + low) // 2) + 1
        worker(low, midpoint - 1)
        worker(midpoint, high)
        buffer1 = arr[low : midpoint]
        buffer2 = arr[midpoint: high + 1]
        i1 = 0
        i2 = 0
        j = low
        def should_take_from_buffer_1():
            if i2 >= len(buffer2):
                return True
            if i1 >= len(buffer1):
                return False
            return buffer1[i1] < buffer2[i2]
        def copyFromBuffer2():
            arr[j] = buffer2[i2]
            j += 1
            i2 += 1
        while j <= high:
            if should_take_from_buffer_1():
                arr[j] = buffer1[i1]
                j += 1
                i1 += 1
            else:
                arr[j] = buffer2[i2]
                j += 1
                i2 += 1
    worker(0, len(arr) - 1)
    return arr


if __name__=='__main__':
    print(''.join(merge_sort(list('MERGESORT'))))
