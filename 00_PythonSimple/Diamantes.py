inp = input("Insira <, . ou >:")
num = 0

inp = inp.replace(".","")

for x in inp:
    if inp.find("<>") != -1:
        inp = inp.replace("<>","",1)
        print(inp)
        num += 1

print("\n\nQuantidade de diamantes: ", num)