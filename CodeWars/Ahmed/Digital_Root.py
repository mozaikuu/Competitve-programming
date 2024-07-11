def digital_root(n): 
    n = str(n)
    # print("Initial = " , n)
    sum = 0
    for num in n:
        sum += int(num)
        # print("sum = " , sum)
    if sum > 9:
        # print(f"sum {sum} is more than 9")
        return digital_root(sum)
    else:
        # print("final = " , sum )    
        # print(sum)
        return sum
      
# digital_root(199)
print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))