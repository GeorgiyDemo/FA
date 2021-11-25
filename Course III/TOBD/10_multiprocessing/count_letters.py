from collections import Counter

def count_letters(file):
    
    with open(file,encoding="windows-1251") as fp:
        text = fp.read().lower()
        return Counter(text)
