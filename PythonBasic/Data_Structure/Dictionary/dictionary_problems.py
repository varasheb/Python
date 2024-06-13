# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# 4. Write a Python program to iterate over dictionaries using for loops.

# 6. Write a Python program to remove a key from a dictionary.



# 10. Write a Python program to count the values associated with key in a
# dictionary.
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
# False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True

# 12. Write a Python program to check multiple keys exists in a dictionary.




def add_key_to_dict(d, key, value):
    d[key] = value
    return d



def iterate_over_dict(d):
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")



def remove_key_from_dict(d, key):
    if key in d:
        del d[key]
    return d


def count_success_true(data):
    count = 0
    for item in data:
        if 'success' in item and item['success'] == True:
            count += 1
    return count


def multiple_keys_exist(d, keys):
    return all(key in d for key in keys)




def main():

    # 2
    sample_dict = {0: 10, 1: 20}
    result = add_key_to_dict(sample_dict, 2, 30)
    print("Updated Dictionary:", result)
    
    # 4
    sample_dict = {1: 10, 2: 20, 3: 30}
    iterate_over_dict(sample_dict)
    

    # 6
    sample_dict = {1: 10, 2: 20, 3: 30}
    result = remove_key_from_dict(sample_dict, 2)
    print("Updated Dictionary:", result)
    
    # 10
    sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    result = count_success_true(sample_data)
    print("Count of success=True:", result)
    
    # 12
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    keys = ['a', 'b']
    result = multiple_keys_exist(sample_dict, keys)
    print("Do all keys exist?:", result)
    
    

main()