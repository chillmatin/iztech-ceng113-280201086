def get_reversed(liste):
    if len(liste) == 0: 
        return []
    return [liste[-1]] + get_reversed(liste[:-1])

print(get_reversed([1,2,3,4]))
