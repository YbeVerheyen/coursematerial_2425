# write your code here
from math import ceil
def pizza(n_people, slices_per_pizza):
    return ceil(n_people / slices_per_pizza)

print(pizza(10,8))