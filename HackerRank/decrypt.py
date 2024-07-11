def minTime(files, numCores, limit):
    # print(files)
    # print(numCores)
    # print(limit)
    
    true_cores = min(numCores,limit)
    if true_cores > len(files):
        true_cores = len(files)
    
    sum = 0
    counter = true_cores
    files.sort(reverse=True)
    for i in files:
        # print(i)
        if counter <= 0:
            continue
        else:
            if i % true_cores == 0:
                sum += int(i/true_cores)
                print(sum)
            else:
                sum += i
                print(sum)
            
    # print("Sum: ", sum)
    
    return sum


print(minTime([3,
,5
,3
,1]
,5
,5)

    