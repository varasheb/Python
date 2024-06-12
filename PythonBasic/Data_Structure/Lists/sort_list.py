# 5. Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


def sort_tuples(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][-1] > items[j][-1]:
                items[i], items[j] = items[j], items[i]
    return items

def main():
    items = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_items = sort_tuples(items)
    print("Sorted list of tuples:", sorted_items)


main()
