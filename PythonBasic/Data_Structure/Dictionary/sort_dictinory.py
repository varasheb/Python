# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

def bubble_sort_ascending(d):
    items = list(d.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][1] > items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    return dict(items)

def bubble_sort_descending(d):
    items = list(d.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][1] < items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    return dict(items)

def main():
    sample_dict = {1: 20, 2: 5, 3: 15}
    asc = bubble_sort_ascending(sample_dict)
    desc = bubble_sort_descending(sample_dict)
    print("Ascending:", asc)
    print("Descending:", desc)

main()