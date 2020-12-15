numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]

set1 = set(numbers1)
set2 = set(numbers2)

onesubtwo = set1 - set2
twosubone = set2 - set1
onesubtwo.update(twosubone)

set1.update(set2)
union = set1
intersection = union - onesubtwo

print(union, intersection)