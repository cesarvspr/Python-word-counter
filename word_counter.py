import re
import string

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    counts.pop('[]', None)
    print("_________________________")
    return counts

def remove_lower(s):
    return ' '.join(w for w in s.split(' ') if not w.islower())

if __name__ == '__main__':
    print("running...")
    
    table = str.maketrans('', '', string.ascii_lowercase)




    # opcodes=input()
    f = open("opcodes_2.txt", "r")
    opcodes = f.read()
    # Transforma input em uma string
    opcodes_str = ''.join(opcodes)
    upper = remove_lower(opcodes_str)
    # Remove numeros da string
    # opcodes_reg = re.sub("\b[A-Z]{3}\b", "", opcodes_str)
    
    # opcodes_reg = re.sub("\d+", "", opcodes_str)
    opcodes_reg = re.sub("[a-z]", "", upper)
    opcodes_reg = re.sub("[0-9]", "", opcodes_reg)
  
    
    opcodes_reg3 = opcodes_reg
    # remove non capital
    opcodes_reg3.translate(table)
    # opcodes_re2 = re.sub("\b[A-Z]{2,}\b", "", opcodes_str)

    

    
    # print(opcodes_reg)
    
    print(word_count(opcodes_reg))