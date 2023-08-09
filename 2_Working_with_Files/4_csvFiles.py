import csv

file_path = '2_Working_with_Files\data.csv'

# Writing data to CSV file
data = [["Name", "Age", "Country"],
        ["Alice", 30, "USA"],
        ["Bob", 25, "Canada"],
        ["Charlie", 22, "Paris"]]

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Reading data from CSV file
with open(file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))


# import json

# def read_json_file(file_path):
#     with open(file_path, 'r') as json_file:
#         data = json.load(json_file)
#         print(data)

# # Usage
# read_json_file('data.json')
