import os

def generate_files():
    ascii_A = ord('A')
    for i in range(26):
        letter = chr(ascii_A + i)
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the content of {file_name}\n")
            
        print(f"File {file_name} has been created.")
generate_files()