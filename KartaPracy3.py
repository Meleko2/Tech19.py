
print("Zadanie 1")
n = int(input())
for i in range(n):
    print(i**3+3, end=" ")
print(" ")

print("Zadanie 2")
for i in range(105,1000):
    if i%15 == 0:
        print(i, end=" ")
print(" ")

print("Zadanie 3")
n = int(input())
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=" ")
print(" ")

print("Zadanie 4")
suma = 0
for i in range(10,100):
    suma = suma + i
print(suma)

