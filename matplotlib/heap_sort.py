import random
import time
from matplotlib import pyplot as plt, animation



def generate_array(array_lenght, number_lenght):
    arr = [0] * array_lenght
    for i in range(0, array_lenght):
        arr[i]= random.randrange(1, number_lenght)
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
    yield arr
  





if __name__ == "__main__":
    my_array = generate_array(100, 100) 

    generator = heap_sort(my_array)

    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort O(n\N{SUPERSCRIPT TWO})")
    bar_sub = ax.bar(range(len(my_array)), my_array, align="edge")
        
    ax.set_xlim(0, len(my_array))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]



    def update(my_array, rects, iteration):
    	for rect, val in zip(rects, my_array):
    		rect.set_height(val)
    	iteration[0] += 1
    	text.set_text(f"# of operations: {iteration[0]}")

    anim = animation.FuncAnimation(
		fig,
		func=update,
		fargs=(bar_sub, iteration),
		frames=generator,
		repeat=True,
		blit=False,
		interval=15,
		save_count=90000,
	)
	


    plt.show()
    plt.close()


    print('unsorted array : ', my_array)
    start_time = time.time()
    print('sorted array : ', heap_sort(my_array))
    print("--- execution time --- %s seconds ---" % (time.time() - start_time))