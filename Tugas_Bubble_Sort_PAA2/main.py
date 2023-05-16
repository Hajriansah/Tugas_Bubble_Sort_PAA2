# Optimized Selection sort in Python

def selectionSort(array):
    # loop through each element of array
    for i in range(len(array)):

        # find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # swap the minimum element with the first element of the unsorted array
        array[i], array[min_index] = array[min_index], array[i]

        print("Iterasi Ke-", i)

data = [6, 24, 18, -7, 32]
print("Data : ", data)

selectionSort(data)

print('Sorted Array in Ascending Order:')
print(data)
