import random



def generate_array(array_lenght):
    arr = [0] * array_lenght
    for i in range(0, array_lenght):
        arr[i]= random.randrange(1, 100)
    return arr



def bubble_sort(arr):
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
    my_array = generate_array(20)
    print('unsorted array : ', my_array)
    print('sorted array : ', bubble_sort(my_array))
