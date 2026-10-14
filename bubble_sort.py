def bubble_sort(arr):
    n = len(arr)
    sorted_arr = list(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = (
                    sorted_arr[j + 1],
                    sorted_arr[j]
                )
                swapped = True

        if not swapped:
            break

    return sorted_arr