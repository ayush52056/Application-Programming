import os

def search_files(directory, extension):
    matching_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                matching_files.append(os.path.join(root, file))
    return matching_files

def main():
    print("Welcome to File Search Utility!")
    directory = input("Enter the directory path: ")
    extension = input("Enter the file extension (e.g., .txt, .py, etc.): ")

    matching_files = search_files(directory, extension)

    if matching_files:
        print("Matching files found:")
        for file in matching_files:
            print(file)
    else:
        print("No matching files found.")

if __name__ == "__main__":
    main()
