n = int(input())
k = int(input())

p = int(input())
q = int(input())

a = n - k
b = p - q

if a == b:
    print("Equal")
elif a > b:
    print("Shekarestan")
else:
    print("Namakestan")
