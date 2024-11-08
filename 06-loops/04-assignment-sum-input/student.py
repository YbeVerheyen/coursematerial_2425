# write your code here
def sum_input():
    som = 0
    getal = 1
    while getal != 0:
        getal = int(input("Enter integer: "))
        som += getal
    print(f"The sum equals {som}.")