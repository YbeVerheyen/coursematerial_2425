# write your code here 
#def subtuple(xs, ys):
#    return str(ys) in str(xs)
   # 2,3,4 in (1,2,3,4,5)

#print(subtuple((1,2,3,4,5),(2,3,4)))

def subtuple(xs, ys):
    if not ys:
        return True
    for i in range(len(xs) - len(ys) + 1): 
        if xs[i:i + len(ys)] == ys:
            return True 
    return False

#print(subtuple((1,2,3,4,5), (2,3,4)))  # Output: True
