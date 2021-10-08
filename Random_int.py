import random

def randomNumberList(no, start, end):
    result = []

    for i in range(no):
        temp = random.randint(start, end)
        result.append(temp)
    return result

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
if len(list2) > len(list1):
    no = len(list2) - len(list1)
    start = list2[0]
    end = list2[-1]
    list1.append(randomNumberList(no, start, end))
print(list1)
