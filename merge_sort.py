import random
import time



def generate_array(array_lenght, number_lenght):
    arr = [0] * array_lenght
    for i in range(0, array_lenght):
        arr[i]= random.randrange(1, number_lenght)
    return arr



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[mid:]
        right = arr[:mid]

        merge_sort(left)
        merge_sort(right)

        






if __name__ == "__main__":
    my_array = generate_array(10, 1000) 
    print('unsorted array : ', my_array)
    start_time = time.time()
    print('sorted array : ', merge_sort(my_array, my_array[0], len(my_array)//2))
    print("--- execution time --- %s seconds ---" % (time.time() - start_time))