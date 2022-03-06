
def binary(sorted_arr, tofind):
    left = 0
    right = len(sorted_arr)-1
    while left <= right:
        mid = (right + left) // 2
        if sorted_arr[mid] == tofind:
            return True
        elif sorted_arr[mid] < tofind:
            left = mid + 1
        else:
            right = mid - 1
    return False

