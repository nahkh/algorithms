def insertionsort(arr):
    result = []
    for value in arr:
        start = 0
        end = len(result)
        position = (start + end) // 2
        while start < end and position < len(result):
            if result[position] > value:
                end = position
            elif result[position] < value:
                start = position + 1
            else:
                break
            position = (start + end) // 2
            
        result.insert(position, value)

    return result
                

        
        

if __name__=='__main__':
    print(''.join(insertionsort('INSERTIONSORT')))
