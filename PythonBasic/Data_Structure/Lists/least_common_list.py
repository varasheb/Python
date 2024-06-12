# 9. Write a Python function that takes two lists and returns True if they have at
# least one common member.

def has_common_member(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8, 9]
    print("Common member between list1 and list2:", has_common_member(list1, list2))

main()
