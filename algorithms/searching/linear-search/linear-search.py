def linear_search(array, target):
    n = len(array)
    for i in range(0, n):
        if  array[i] == target:
            return True
    return False