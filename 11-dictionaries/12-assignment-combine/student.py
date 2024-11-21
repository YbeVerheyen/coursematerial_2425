def combine(d1, d2):
    result = {}
    #result[key] == d2[d1[key]]
    for word in d1:
        ned = d1[word]
        if ned in d2:
            result[word] = d2[ned]
    return result