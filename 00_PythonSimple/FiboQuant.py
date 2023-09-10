quant = 0

def addQuant():
    global quant
    quant += 1

def fiboQuant(n):
   global quant
   if n <= 1:
       addQuant()
       print("chamada: ", quant)
       return n
   else:
       addQuant()
       print("chamada: ", quant)
       return(fiboQuant(n-1) + fiboQuant(n-2))

inp = int(input("Insira um valor: "))
print("\n")
for i in range(inp):
    print(fiboQuant(i))

print("\nQuantidade de chamadas: ", quant)
