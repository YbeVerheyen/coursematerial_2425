# write your code here
def cake3(eggs, flour, butter, sugar):
    e = eggs // 5
    f = flour // 250
    b = butter // 200
    s = sugar // 250
    
    return min( e, f, b, s)