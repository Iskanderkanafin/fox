import re
def vstavka(text):
    torfin = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    print(torfin)
askelat = input()
vstavka(askelat)