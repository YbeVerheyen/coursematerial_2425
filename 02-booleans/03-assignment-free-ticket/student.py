# write your code here
def free_ticket(age):
    if age < 12:
        return True
    elif age >= 65:
        return True
    else:
        return False

print(free_ticket(65))