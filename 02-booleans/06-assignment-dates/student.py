# write your code here
def is_valid_month(month):
    if month <= 12 and month >= 1:
        return True
    return False

def is_leap_year(year):
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        return True
    return False
    
def has_30_days(month):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return True
    return False

def has_31_days(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return True
    return False

def has_28_days(month, year):
    if month == 2 and not is_leap_year(year):
        return True
    return False

def has_29_days(month, year):
    if month == 2 and is_leap_year(year):
        return True
    return False


def is_valid_date(day, month, year):
    if has_31_days(month) and day >= 1 and day <= 31:
        return True
    if has_30_days(month) and day >=1 and day <=30:
        return True
    if has_29_days(month, year) and day >= 1 and day <=29:
        return True
    if has_28_days(month, year) and day >= 1 and day <=28:
        return True
    return False