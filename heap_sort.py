import random
import time



def generate_array(array_lenght, number_lenght):
    arr = [0] * array_lenght
    for i in range(0, array_lenght):
        arr[i]= random.randrange(1, number_lenght)
    return arr



def heap_sort(arr):
    run = True
    while(run):
        co = 0
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                co += 1
        if(co == 0):
            run = False
    return arr






if __name__ == "__main__":
    my_array = generate_array(10, 1000) 
    print('unsorted array : ', my_array)
    start_time = time.time()
    print('sorted array : ', heap_sort(my_array))
    print("--- execution time --- %s seconds ---" % (time.time() - start_time))