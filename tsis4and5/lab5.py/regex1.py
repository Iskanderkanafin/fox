import re

def find_ab(text):
    garou = r'ab*' 
    matches = re.finditer(garou, text)
    for match in matches:
        print("нашел", match.group(0))

uchiha_input = input()


find_ab(uchiha_input)
