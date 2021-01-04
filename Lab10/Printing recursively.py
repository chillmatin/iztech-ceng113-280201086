def count(n):
    if n <= 0:
        return
    print(n)
    return count(n-1)

count(5)