# def make_readable(sec): 
#     print(sec)
#     min = sec / 60 
#     print(min)
#     hr = min / 60
#     print(hr)
#     fixedhr = int(hr)
    
#     remainderhr = hr - fixedhr

#     remaindermin = remainderhr * 60

#     fixedmin = int(remaindermin)

#     remaindermin = remaindermin - fixedmin

#     remsec = remaindermin * 60

#     fixedsec = int(remsec)
    
#     if fixedhr >= 9:
#         fixedhr = "0" + str(fixedhr)
#     if fixedmin == 0:
#         fixedmin = "00"
#     if fixedsec == 0:
#         fixedsec = "00"
    
#     return f"{fixedhr}:{fixedmin}:{fixedsec}"



# print(make_readable(58))

def make_readable(sec): 
    # 1hr = 3600 sec
    # 1min = 60 sec
    hr = 0
    while sec >= 3600:
        sec = sec-3600
        hr += 1
    print(hr)
    min = 0
    while sec >= 60:
        sec = sec-60
        min += 1
    print(min)
    print(sec)
    
    if hr < 10:
        hr = "0" + str(hr)
    if min < 10:
        min = "0" + str(min)
    if sec < 10:
        sec = "0" + str(sec)
    
    return f"{hr}:{min}:{sec}"



print(make_readable(60))