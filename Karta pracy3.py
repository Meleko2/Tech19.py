#zad 1
n = int(input())
for i in range(n):
  print(i**3+3, end=" ")

#zad 2
for i in range(105,1000,15):
  print(i, end=" ")

#zad 3
n = int(input())
for i in range(1,n+1):
  if n%i == 0:
    print(i, end=" ")

#zad 4
suma = 0
for i in range(10,100):
  suma = suma + i
print(suma)

#zad 5
n = int(input())
suma = n*(n+1)/2 #suma cyfr od 1 do n
for i in range(n-1):
  x = int(input())
  suma = suma - x
print("Nie podałeś", suma)

#zad 6
n = int(input())
a = 0
b = 1
print(a, end=" ")
print(b, end=" ")
for i in range(n-1):
    a, b = b, a+b
    print(b , end=' ')
  



        




