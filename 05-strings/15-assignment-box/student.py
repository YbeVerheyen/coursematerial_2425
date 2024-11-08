# write your code here
def box(string):
    lenStr = len(string) * "-"
    return f"+-{lenStr}-+\n| {string} |\n+-{lenStr}-+"

print(box('halloween'))