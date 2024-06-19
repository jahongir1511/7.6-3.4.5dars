# misol linki        https://www.codewars.com/kata/53d2697b7152a5e13d000b82/train/python


def copy_list(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    return lst[:]

# Example usage:
t = [1, 2, 3, 4]
t_copy = copy_list(t)

t[1] += 5
print("Original list:", t)
print("Copied list:", t_copy)
