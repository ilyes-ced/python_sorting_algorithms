import random
import time



def generate_array(array_lenght, number_lenght):
    arr = [0] * array_lenght
    for i in range(0, array_lenght):
        arr[i]= random.randrange(1, number_lenght)
    return arr



def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1
 
 
 
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array




if __name__ == "__main__":
    my_array = generate_array(10, 1000) 
    print('unsorted array : ', my_array)
    start_time = time.time()
    print('sorted array : ', quick_sort(my_array, 0, len(my_array)-1))
    print("--- execution time --- %s seconds ---" % (time.time() - start_time))