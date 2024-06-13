# 9. Write a Python program to print a dictionary in table format.


def print_dict_table(d):
    print("{:<10} {:<10}".format('Key', 'Value'))
    for key, value in d.items():
        print("{:<10} {:<10}".format(key, value))

def main():
    sample_dict = {1: 10, 2: 20, 3: 30}
    print_dict_table(sample_dict)

main()
    