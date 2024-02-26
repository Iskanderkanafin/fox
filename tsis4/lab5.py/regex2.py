import re

def find_abb_abbb(text):
    inoske = r'a(b{2,3})'
    suiriy = re.finditer(inoske,text)
    for match in suiriy:
        print("нашел",match.group(0))
        
saitama_input = input()
find_abb_abbb(saitama_input)

