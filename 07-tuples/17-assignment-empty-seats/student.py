# write your code here
def empty_seats(used_seats):
    count = 0
    for i in range(len(used_seats)-1):
        between = used_seats[i + 1] - used_seats[i] - 1
        if between > 0:
            count += between
    return count