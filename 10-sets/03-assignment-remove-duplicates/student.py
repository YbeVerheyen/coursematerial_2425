def remove_duplicates(xs):
    seen = set()
    newxs = []
    for i in xs:
        if i not in seen:
            newxs.append(i)
            seen.add(i)
    return newxs
    