import json

with open('expected_data.json') as file:
    expected_data = json.load(file)
    file.close()

valid_specialty = {
    "name" : "NEUMOLOGIA"
}

invalid_specialty = {}
