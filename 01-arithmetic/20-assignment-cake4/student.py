# write your code here
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    eggs_for_cake = eggs // eggs_per_cake
    flour_for_cake = flour // flour_per_cake
    butter_for_cake = butter // butter_per_cake
    sugar_for_cake = sugar // sugar_per_cake

    return min(eggs_for_cake, flour_for_cake, butter_for_cake, sugar_for_cake)

    print (cake4(10,500, 400, 500, 5, 250, 200, 250))