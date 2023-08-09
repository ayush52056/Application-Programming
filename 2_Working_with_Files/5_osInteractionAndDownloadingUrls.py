import os
import requests

# Example: Working with Directories
current_dir = os.getcwd()
print("Files and directories in the current directory:")
print(os.listdir(current_dir))

new_dir = "new_directory"
os.mkdir(new_dir)
print(f"Directory '{new_dir}' created successfully!")

os.rmdir(new_dir)
print(f"Directory '{new_dir}' removed successfully!")

# Example: Checking File Existence
file_path = "example.txt"
if os.path.exists(file_path):
    print(f"File '{file_path}' exists!")
else:
    print(f"File '{file_path}' does not exist.")

some_path = "some_directory"
if os.path.isfile(some_path):
    print(f"'{some_path}' is a regular file.")
elif os.path.isdir(some_path):
    print(f"'{some_path}' is a directory.")
else:
    print(f"'{some_path}' does not exist or is not a file/directory.")

# Example: Downloading URLs
def download_url(url, save_as):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_as, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded '{url}' as '{save_as}' successfully.")
    else:
        print(f"Failed to download '{url}'. Status code: {response.status_code}.")

# Download an image from a URL
url = "https://example.com/sample_image.jpg"
save_as = "downloaded_image.jpg"
download_url(url, save_as)

# Download a text file from a URL
url = "https://example.com/sample_text.txt"
save_as = "downloaded_text.txt"
download_url(url, save_as)
