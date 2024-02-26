import re
def find_stro_ki(text):
    gangster = r'[a-z]*_[a-z]*'
    toji = re.finditer(gangster,text)
    for match in toji:
        print("нашел", match.group(0))
madara_input = input("write")
find_stro_ki(madara_input)