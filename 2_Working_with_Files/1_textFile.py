# Example 1: Reading from a Text File
file_path = '2_Working_with_Files\example.txt'
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
    # lines = file.readlines()
    # for line in lines:
    #     print(line.strip())  # Strip removes extra newline characters




# Example 2: Writing to a Text File
file_path = '2_Working_with_Files\output.txt'
with open(file_path, 'w') as file:
    file.write("This is a test.")
