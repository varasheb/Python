import json

def find_address_by_pincode(pincode):
    with open('/home/lucky/Bridgelabz-Python/PythonAdvance/pincodes.json', 'r') as file:

        data = json.load(file)
    
    
    for entry in data:
        if entry['pincode'] == pincode:
            return entry
    
    return "Address not found for the given pincode."

def print_all_city(state):
    state=state.upper()
    with open('/home/lucky/Bridgelabz-Python/PythonAdvance/pincodes.json', 'r') as file:

        data = json.load(file)
    
    city=set()
    for entry in data:
        if entry['stateName'] == state:
           city.add(entry['taluk'])        
    print(len(city))

#====================================================
if __name__ =="__main__":
    pincode = 560061
    address = find_address_by_pincode(pincode)
    print(f"Address for pincode {pincode}: {address}")

    # pincode = int(input("Enter your pin code :"))
    address = find_address_by_pincode(pincode)
    print(f"Address for pincode {pincode}: {address}")

    print_all_city("Karnataka")



    count=set(i for i in range(1,100))
    count.add(10)
    print(count)


