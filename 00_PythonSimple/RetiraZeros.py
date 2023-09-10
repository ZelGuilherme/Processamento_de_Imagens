def soma(a, b):
    return (a + b)

a = int(input())
b = int(input())

res = soma(a,b)

newRes = str(res).replace("0", "")

print(newRes)
