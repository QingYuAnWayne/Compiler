import Function
import sys


def main():
    position = sys.argv[1]
    # position = "F:\\Python codes\\Compiler\\1.txt"
    with open(position , 'r') as file:
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
                    try:
                        while line[i].isdigit():
                            token += line[i]
                            i += 1
                    except IndexError:
                        pass
                    token = int(token, 10)
                    print("Int("+str(token)+")")

                else:#识别符号
                    token += line[i]
                    i += 1
                    try:
                        if token == ':' and line[i] == '=':
                            print("Assign")
                            i += 1
                        else:
                            symbol = Function.reserver(token)
                            if symbol == 'Unknown':
                                return
                            else:
                                print(symbol)
                    except IndexError:
                        pass
    return 0

if __name__ == '__main__':
    main()
                










