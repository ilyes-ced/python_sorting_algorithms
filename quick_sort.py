import random
import time



def generate_array(array_lenght, number_lenght):
    arr = [0] * array_lenght
    for i in range(0, array_lenght):
        arr[i]= random.randrange(1, number_lenght)
    return arr



def parition():
    print('gg')


def quick_sort(arr):
    low = 0
    high = len(arr) - 1
    pivot = arr[high]
    for i in range(high):
        if(1):
            print('hello')






if __name__ == "__main__":
    my_array = generate_array(10, 1000) 
    print('unsorted array : ', my_array)
    start_time = time.time()
    print('sorted array : ', quick_sort(my_array))
    print("--- execution time --- %s seconds ---" % (time.time() - start_time))