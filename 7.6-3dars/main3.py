#  misol linki   https://www.codewars.com/kata/59b44d00bf10a439dd00006f/train/python




def add(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    result = []
    running_sum = 0

    for num in lst:
        running_sum += num
        result.append(running_sum)

    return result


print(add([1, 2, 3, 4, 5]))
print(add([1]))
print(add([]))
