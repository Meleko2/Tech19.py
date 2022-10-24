print("Zadanie 1")
for i in range(1,31):
    print(i, end=" ")
print(" ")


print("Zadanie 2")
a = int(input("Podaj liczbe: "))
for i in range(1 ,a):
    if i%2==1:
        print(i**2, end=" ")
print(' ')


print("Zadanie 3")
for i in range(1000,10000):
    if i%379==0:
        print(i, end=" ")
print(" ")


print("Zadanie 4")
for i in range(100,1000):
    if i%5==0 or i%6==0 or i%11==0:
        print(i, end=" ")
print(" ")


print("Zadanie 5")
suma=0
a = int(input())
for i in range(1, a):
    b = int(input())
    suma = suma + i
print(suma)


print("Zadanie 6")
suma=0
k = int(input("Podaj liczbe: "))
for i in range(1, k):
    if i%2==0:
        suma=suma+i
print(suma)
print(" ")


print("Zadanie 7")
suma=0
m = int(input("Podaj liczbe: "))
for i in range(1, m):
    if i%2==1 and i>9 and 1<100:
        suma=suma+i
print(suma)
print(" ")


print("Zadanie 8")
W0 = int(input())
L = int(input())
WX = 0
suma = W0
for i in range(0, L * 12):
    WX = suma * 0.06 * (1/12)
    suma = suma + WX
print(round(suma))
print(' ')

print("Zadanie 9")
a = int(input("Podaj ilosc liczb: "))
b = 21
suma = 0 
for i in range(0, a+1):
    for j in range(0, i, b):
        suma = suma + j
        j = j + 100
print(f"Suma to: {suma}")


from math import sqrt
print("Zadanie 10")
#IDK



