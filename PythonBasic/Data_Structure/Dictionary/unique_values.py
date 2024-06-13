# 7. Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


def unique_values(dicts):
    unique_vals = set()
    for d in dicts:
        for value in d.values():
            unique_vals.add(value)
    return unique_vals

def main():
    
    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                   {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    result = unique_values(sample_data)
    print("Unique Values:", result)

main()