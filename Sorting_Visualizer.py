from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry("750x600")
root.config(bg='orange')

select_algorithm = StringVar()
arr = []

comparison_count = 0
swap_count = 0

comparison_label = None
swap_label = None
time_label = None

def update_counters():
    comparison_label.config(text=f"Comparisons: {comparison_count}")
    swap_label.config(text=f"Swaps: {swap_count}")
    root.update_idletasks()

# Bubble Sort
def bubble_sort(data, drawrectangle, delay):
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparison_count += 1
            drawrectangle(data, ['yellow' if x == j or x == j + 1 else 'red' for x in range(len(data))])
            update_counters()
            time.sleep(delay)
            if data[j] > data[j + 1]:
                swap_count += 1
                data[j], data[j + 1] = data[j + 1], data[j]
                drawrectangle(data, ['red' if x == j or x == j + 1 else 'blue' for x in range(len(data))])
                update_counters()
                time.sleep(delay)
    drawrectangle(data, ['blue' for _ in range(len(data))])
    update_counters()

# Selection Sort
def selection_sort(data, drawrectangle, delay):
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparison_count += 1
            drawrectangle(data, ['yellow' if x == j or x == min_idx else 'red' for x in range(len(data))])
            update_counters()
            time.sleep(delay)
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            swap_count += 1
            data[i], data[min_idx] = data[min_idx], data[i]
            drawrectangle(data, ['red' if x == i or x == min_idx else 'blue' for x in range(len(data))])
            update_counters()
            time.sleep(delay)
    drawrectangle(data, ['blue' for _ in range(len(data))])
    update_counters()

# Insertion Sort
def insertion_sort(data, drawrectangle, delay):
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0:
            comparison_count += 1
            drawrectangle(data, ['yellow' if x == j or x == j + 1 else 'red' for x in range(len(data))])
            update_counters()
            time.sleep(delay)
            if data[j] > key:
                swap_count += 1
                data[j + 1] = data[j]
                j -= 1
                drawrectangle(data, ['red' if x == j + 1 else 'blue' for x in range(len(data))])
                update_counters()
                time.sleep(delay)
            else:
                break
        data[j + 1] = key
        drawrectangle(data, ['blue' for _ in range(len(data))])
        update_counters()
    drawrectangle(data, ['blue' for _ in range(len(data))])
    update_counters()

# Merge Sort
def merge_sort(data, drawrectangle, delay):
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0

    def merge(arr, left, mid, right):
        global comparison_count, swap_count
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            comparison_count += 1
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
                swap_count += 1  # Count placement as swap
            k += 1
            drawrectangle(arr, ['yellow' if left <= x <= right else 'red' for x in range(len(arr))])
            update_counters()
            time.sleep(delay)
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
            swap_count += 1
            drawrectangle(arr, ['yellow' if left <= x <= right else 'red' for x in range(len(arr))])
            update_counters()
            time.sleep(delay)
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
            swap_count += 1
            drawrectangle(arr, ['yellow' if left <= x <= right else 'red' for x in range(len(arr))])
            update_counters()
            time.sleep(delay)

    def merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(arr, left, mid)
            merge_sort_recursive(arr, mid + 1, right)
            merge(arr, left, mid, right)

    merge_sort_recursive(data, 0, len(data) - 1)
    drawrectangle(data, ['blue' for _ in range(len(data))])
    update_counters()

# Quick Sort
def quick_sort(data, drawrectangle, delay):
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0

    def partition(arr, low, high):
        global comparison_count, swap_count
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparison_count += 1
            drawrectangle(arr, ['yellow' if x == j or x == high else 'red' for x in range(len(arr))])
            update_counters()
            time.sleep(delay)
            if arr[j] <= pivot:
                i += 1
                swap_count += 1
                arr[i], arr[j] = arr[j], arr[i]
                drawrectangle(arr, ['red' if x == i or x == j else 'blue' for x in range(len(arr))])
                update_counters()
                time.sleep(delay)
        swap_count += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        drawrectangle(arr, ['red' if x == i + 1 or x == high else 'blue' for x in range(len(arr))])
        update_counters()
        time.sleep(delay)
        return i + 1

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)

    quick_sort_recursive(data, 0, len(data) - 1)
    drawrectangle(data, ['blue' for _ in range(len(data))])
    update_counters()

# Heap Sort
def heap_sort(data, drawrectangle, delay):
    global comparison_count, swap_count
    comparison_count = 0
    swap_count = 0

    def heapify(arr, n, i):
        global comparison_count, swap_count
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n:
            comparison_count += 1
            if arr[l] > arr[largest]:
                largest = l
            drawrectangle(arr, ['yellow' if x == l or x == i else 'red' for x in range(len(arr))])
            update_counters()
            time.sleep(delay)

        if r < n:
            comparison_count += 1
            if arr[r] > arr[largest]:
                largest = r
            drawrectangle(arr, ['yellow' if x == r or x == i else 'red' for x in range(len(arr))])
            update_counters()
            time.sleep(delay)

        if largest != i:
            swap_count += 1
            arr[i], arr[largest] = arr[largest], arr[i]
            drawrectangle(arr, ['red' if x == i or x == largest else 'blue' for x in range(len(arr))])
            update_counters()
            time.sleep(delay)
            heapify(arr, n, largest)

    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        swap_count += 1
        data[i], data[0] = data[0], data[i]
        drawrectangle(data, ['red' if x == i or x == 0 else 'blue' for x in range(len(data))])
        update_counters()
        time.sleep(delay)
        heapify(data, i, 0)
    drawrectangle(data, ['blue' for _ in range(len(data))])
    update_counters()

# Algorithm mapping
algorithm_dict = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort
}

# Generate array function
def Generate_array():
    global arr
    lowest = int(lowest_Entry.get())
    highest = int(highest_Entry.get())
    size = int(arrsize_Entry.get())
    arr = []
    for _ in range(size):
        arr.append(random.randrange(lowest, highest + 1))
    drawrectangle(arr, ['red' for _ in range(len(arr))])

# Draw array bars appropriately spaced and text centered above bars
def drawrectangle(arr, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width / (len(arr) + 1)
    border_offset = 30
    spacing = 10
    normalized_array = [i / max(arr) for i in arr]
    for i, height in enumerate(normalized_array):
        x0 = i * bar_width + border_offset + spacing
        y0 = canvas_height - height * 340
        x1 = (i + 1) * bar_width + border_offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        # Center text above each bar to avoid overlap
        canvas.create_text((x0 + x1) / 2, y0 - 5, anchor='s', text=str(arr[i]), font=('Arial', 9))
    root.update_idletasks()

# Sorting handler including timing
def sorting():
    global arr
    if not arr:
        return
    algo = select_algorithm.get()
    sorting_function = algorithm_dict.get(algo)
    if sorting_function:
        start_time = time.time()
        sorting_function(arr, drawrectangle, sortingspeed.get())
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_label.config(text=f"Time Taken: {elapsed_time:.2f} seconds")

# GUI Setup
options_frame = Frame(root, width=700, height=300, bg='green')
options_frame.grid(row=0, column=0, padx=10, pady=10)

canvas = Canvas(root, width=700, height=350, bg='grey')
canvas.grid(row=1, column=0, padx=10, pady=5)

Label(options_frame, text="Algorithm Choice: ").grid(row=0, column=0, padx=10, pady=10)

algomenu = ttk.Combobox(options_frame, textvariable=select_algorithm, values=list(algorithm_dict.keys()), width=15)
algomenu.grid(row=0, column=1, padx=5, pady=5)
algomenu.current(0)

sortingspeed = Scale(options_frame, from_=0.01, to=2.0, length=100, digits=2, resolution=0.01, orient=HORIZONTAL, label="Sorting Speed (seconds delay)")
sortingspeed.grid(row=0, column=2, padx=10, pady=10)
sortingspeed.set(0.1)  # default speed

Button(options_frame, text="Start Sorting", command=sorting, bg='red', height=5).grid(row=0, column=3, padx=5, pady=5)

lowest_Entry = Scale(options_frame, from_=5, to=20, resolution=1, orient=HORIZONTAL, label="Lower Limit")
lowest_Entry.grid(row=1, column=0, padx=5, pady=5)
lowest_Entry.set(5)

highest_Entry = Scale(options_frame, from_=20, to=100, resolution=1, orient=HORIZONTAL, label="Upper Limit")
highest_Entry.grid(row=1, column=1, padx=5, pady=5)
highest_Entry.set(100)

arrsize_Entry = Scale(options_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Array size")
arrsize_Entry.grid(row=1, column=2, padx=5, pady=5)
arrsize_Entry.set(10)

Button(options_frame, text="Generate Array", command=Generate_array, bg='blue', height=5).grid(row=1, column=3, padx=10, pady=10)

# Comparison and Swap Labels
comparison_label = Label(root, text="Comparisons: 0", bg='orange', font=('Arial', 12, 'bold'))
comparison_label.grid(row=2, column=0, sticky=W, padx=20)

swap_label = Label(root, text="Swaps: 0", bg='orange', font=('Arial', 12, 'bold'))
swap_label.grid(row=2, column=0, sticky=E, padx=20)

# Time taken label
time_label = Label(root, text="Time Taken: 0.00 seconds", bg='orange', font=('Arial', 12, 'bold'))
time_label.grid(row=3, column=0, sticky=W, padx=20)

root.mainloop()
