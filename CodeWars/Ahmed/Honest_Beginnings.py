# return masked string
cc="4613216431"
def maskify(cc):
  s=""
  i = 0
  if len(cc) <= 4:
    return cc
  else:
    while i < len(cc) - 4:
      s += "#"
      i += 1
    j = len(cc) - 4
    while j < len(cc):
      # print(j)
      s += cc[j]
      j += 1
    return s
  
print(maskify(cc))
    
    

