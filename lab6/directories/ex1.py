import os

def list_directories_and_files(path):
    print("List of directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nList of files:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    print("\nList of all directories with files:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            print(f"Directory: {dir_path}")
            for file in os.listdir(dir_path):
                print(f" - File: {os.path.join(dir_path, file)}")


path = input("Enter the path of the directory: ")


if os.path.exists(path):
    list_directories_and_files(path)
else:
    print("The specified path does not exist.")