# 3. Write a Python script to concatenate following dictionaries to create a new
# one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

def main():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    result = concatenate_dicts(dic1, dic2, dic3)
    print("Concatenated Dictionary:", result)
    
main()