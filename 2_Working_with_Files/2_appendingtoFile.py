file_path = '2_Working_with_Files\log.txt'

def log_message(message):
    with open(file_path, 'a') as file:
        file.write('\n'+ message)

log_message("Error: File not found.")
log_message("Warning: Resource low.")
