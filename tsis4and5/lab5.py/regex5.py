import re
def find_hard(text):
    gats = r'.*a.*b$'
    bita = re.finditer(gats, text)
    for match in bita:
      print("нашел",match.group(0))
smoker=input("write")
find_hard(smoker)
      
    
