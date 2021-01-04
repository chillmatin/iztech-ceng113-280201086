def hailstone(x, sequence = []):
    sequence.append(x)
    if x == 1:
        return sequence
    elif x % 2 == 0:
        x = x / 2
    elif x % 2 == 1:
        x = 3*x + 1

    return hailstone(x, sequence)
        
print(hailstone(11))
