import random


array_lenght = 20
arr = [0] * array_lenght
#arr = [5, 7, 6, 2, 3, 7, 4, 4, 9, 63]


def generate_array():
    for i in range(0, array_lenght):
        arr[i]= random.randrange(1, 100)
generate_array()





run = True
while(run):
    co = 0
    for i in range(array_lenght-1):
        if(arr[i] > arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            co += 1
        if(co == 0):
            run = False


print(arr)