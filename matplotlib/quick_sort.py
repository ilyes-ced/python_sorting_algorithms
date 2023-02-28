import random
import time
from matplotlib import pyplot as plt, animation



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
    yield array





if __name__ == "__main__":
    my_array = generate_array(100, 100) 

    generator = quick_sort(my_array, 0, len(my_array)-1)

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
    print('sorted array : ', quick_sort(my_array, 0, len(my_array)-1))
    print("--- execution time --- %s seconds ---" % (time.time() - start_time))