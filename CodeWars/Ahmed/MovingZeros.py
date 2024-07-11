# print([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])

def move_zeros(arr):
    i=0
    while i < len(arr):
        count = i+1     
        if arr[i] == 0:
            if arr[count]!=0:
                arr[i] = arr[count]
                arr[count] = 0
            elif count == 0:
                count +=1
                if count == len(arr):
                    return arr
                
            
        i+=1
            
    return arr

print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
# print([9, 9, 9, 9, 1, 2, 1, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# print([9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))