import random
import time



def generate_array(array_lenght, number_lenght):
    arr = [0] * array_lenght
    for i in range(0, array_lenght):
        arr[i]= random.randrange(1, number_lenght)
    return arr



def merge_sort(arr, left, mid):
    run = True
    while(run):
        co = 0
        for i in range(len(arr)-1):
            if(arr[i] > arr[i+1]):
                mid= (arr[i] + arr[i+1])/2
                merge_sort(arr, arr[i], mid)
                merge_sort(array, mid+1, right)
                array + left + mid + right

                co += 1
        if(co == 0):
            run = False
    return arr






if __name__ == "__main__":
    my_array = generate_array(10, 1000) 
    print('unsorted array : ', my_array)
    start_time = time.time()
    print('sorted array : ', merge_sort(my_array, my_array[0], len(my_array)//2))
    print("--- execution time --- %s seconds ---" % (time.time() - start_time))