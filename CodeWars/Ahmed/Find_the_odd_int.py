def find_it(seq):
    for elem in seq:
        i = 0
        count = 0
        while i < len(seq):
            if elem == seq[i]:
                count += 1
            i +=1
        if count%2 != 0:
            return elem
        
        
print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))