def find_duplicates(xs):
    seen = set()
    dup = set()
    for i in xs:
        if i in seen:
            dup.add(i)
        seen.add(i)
    return list(dup)