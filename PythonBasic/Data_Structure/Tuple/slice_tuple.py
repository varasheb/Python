# 9. Write a Python program to slice a tuple.

def slice_tuple(my_tuple, start, stop, step):
    sliced_tuple = my_tuple[start:stop:step]
    return sliced_tuple

def main():
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    start = 2
    stop = 8
    step = 2
    sliced_tuple = slice_tuple(my_tuple, start, stop, step)
    print("Sliced tuple:", sliced_tuple)

main()

