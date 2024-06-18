import json


# JSON string
json_data = '{"name": "Virat Koli", "age": 30, "city": "Banglore"}'

# Parse JSON string to Python dictionary
data = json.loads(json_data)
print(data)

# Access data
print(data['name']) 
print(data['city'])



# Serialization of Json
data = {"name": "Rohit", "age": 38 , "city":"Mumbai"}
json_string = json.dumps(data)
print(type(json_string))


# Nested JSON string
nested_json_data = '''
{
    "name": "Ramesh",
    "age": 30,
    "address": {
        "city": "Wonderland",
        "street": "Rabbit Hole",
        "pin": "12345"
    },
    "hobbies": ["reading", "chess", "gardening"]
}
'''

data = json.loads(nested_json_data)


print(data['address']['city']) 
print(data['hobbies'][1])