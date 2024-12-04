def remove_empty_lines(source, destination):
    with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
    
        for line in src:
            if line.strip('\n'):
                dest.writelines(line)