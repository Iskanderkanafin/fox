import re

def split_AA(text):
    rock_lee = re.findall('[A-Z][^A-Z]*', text)
    print(rock_lee)
sanji = input()
split_AA(sanji)