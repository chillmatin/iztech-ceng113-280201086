def get_evens(liste):

    if len(liste) == 1:
        if liste[0] % 2 == 0: return 1
        else: return 0

    return get_evens([liste[-1]]) + get_evens(liste[:-1])
            
print(get_evens([0, 1, 2, 3, 4, 5]))