import re

def godjo(text):
    zabudza = r'[ ,.]'
    replaced_text = re.sub(zabudza, ':', text)
    print(replaced_text)
satoru = input()
godjo(satoru)
