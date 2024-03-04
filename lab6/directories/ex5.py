def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

my_list = ["zoro","garou","toji","bita","baki"]
file_name = input("Enter the file name to write the list: ")

write_list_to_file(my_list, file_name)
print("List has been written to the file successfully.")