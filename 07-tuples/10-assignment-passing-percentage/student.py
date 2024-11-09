# write your code here
def passing_percentage(grades):
    passed = sum(i >= 10 for i in grades)
    if not grades:
        return 0
    
    percentage = (passed / len(grades)) * 100
    
    return int(percentage)
