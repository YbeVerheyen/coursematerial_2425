def remove_duplicate_lines(source, destination):
    with open(source, 'r', encoding='utf-8') as src:
        new_src = src.readlines()
    
    if len(new_src) <= 1:
        save = new_src
    else:
        save = [new_src[0]]
        for i in range(1,len(new_src)):       #i = line
            if new_src[i] != new_src[i-1]:
                save.append(new_src[i])
    with open(destination, 'w', encoding='utf-8') as dest:
        dest.writelines(save)

remove_duplicate_lines('test.txt', 'dest.txt')