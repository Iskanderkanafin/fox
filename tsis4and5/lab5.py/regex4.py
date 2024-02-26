import re
def find_Abc(text):
    fushigura = r'[A-Z][a-z]+'
    hiruzen = re.finditer(fushigura , text)
    for match in hiruzen:
        print("нашел" , match.group(0))
shikamaru_input = input("write")
find_Abc(shikamaru_input)