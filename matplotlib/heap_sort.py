import random
import time



def generate_array(array_lenght, number_lenght):
    arr = [0] * array_lenght
    for i in range(0, array_lenght):
        arr[i] = random.randrange(1, number_lenght)
    return arr



def heapify(arr, N, i):
    largest = i
    l = 2 * i + 1  
    r = 2 * i + 2
  
    if l < N and arr[largest] < arr[l]:
        largest = l
  
    if r < N and arr[largest] < arr[r]:
        largest = r
  
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
  
        heapify(arr, N, largest)
  
  
  
def heap_sort(arr):
    N = len(arr)
  
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)
  
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
  





if __name__ == "__main__":
    my_array = generate_array(10, 1000) 
    print('unsorted array : ', my_array)
    start_time = time.time()
    print('sorted array : ', heap_sort(my_array))
    print("--- execution time --- %s seconds ---" % (time.time() - start_time))