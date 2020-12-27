from time import sleep

def timer(t):
    if t == 0: return print("Time's up!")
    else: print(t, 'seconds')
    sleep(1)
    return timer(t-1)

timer(10)