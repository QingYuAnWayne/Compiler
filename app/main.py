import Function
import os

dirlist = []
files = os.listdir('.')
for f in files:
    file = f
    token = ""
    for line in file:
        i = 0
        while i < len(line):
            token = ""
            if line[i].isspace():
                i += 1
                continue
            if line[i].isalpha():
                try:
                    while line[i].isalnum():
                        token += line[i]
                        i += 1
                except IndexError:
                    pass
                symbol = Function.reserver(token)
                if symbol == 'Unknown':
                    print("Ident("+token+")")
                else:
                    print(symbol)
            elif line[i].isdigit():
                while line[i].isdigit():
                    token += line[i]
                    i += 1
                print("Int("+token+")")










