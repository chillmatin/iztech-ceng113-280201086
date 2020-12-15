import random

def get_rand_list(b,e,N):
    
    random_list = random.sample(range(b, e), N)   
    return random_list


def get_overlap(list1, list2):
    print(list1)
    print(list2)
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    print(intersection)

b = 0
e = 10
N = 5

get_overlap(get_rand_list(b,e,N), get_rand_list(b,e,N))
