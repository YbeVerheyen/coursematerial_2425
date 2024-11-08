# write your code here
def split_name(full_name):
    for i in range(len(full_name)):
        if full_name[i] == " ":
            first_name = full_name[0:i]
            last_name = full_name[i+1:]

            return first_name, last_name
    
#print(split_name("Walter White"))