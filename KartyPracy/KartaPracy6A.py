def NWD(a,b):
  while a!=b:
    if a>b:
      a-=b
    else:
      b-=a

#Zadania 1 - do zrozumienia
x = int(input("Podaj liczbe: "))
suma = 0
while x > 0:
  suma += x % 10
  x //= 10

print(suma)

#Zadania 2
x = int(input("Podaj liczbe: "))
temp = 0
for i in range(1,x):
  if x%i == 0:
    temp+=1
if temp<3:
  print("tak")
else:
  print("nie")
    
#Zadania 3 - doskonale- dzielniki dodane do siebie daja ta liczbe nie liczac jej samej
n = int(input("Podaj liczbe: "))
suma = 0
for i in range(1,n):
  if i%n == 0:
    suma+=i
if suma==n:
  print("Jest doskonala")
else:
  print("Nie jest doskonala")

#Zadania 4 - wzglednie pierwsze- ich nwd = 1
x = int(input("Podaj liczbe1: "))
y = int(input("Podaj liczbe2: "))
NWD(x, y)
if x==1:
  print("Liczby sa wzglednie pierwsze")
else:
  print("Liczby nie sa wzglednie pierwsze")

#Zadania 5
m = int(input("Podaj liczbe: "))
for i in range(10,20):
  x = m
  y = i
  NWD(x, y)
  if x==1:
    print(f"Wzglednie pierwsze: {m}, {i}")
    
#Zadania 6
a=int(input("Licznik: "))
b=int(input("Mianownik: "))
c=a
d=b
a,b=x,y
NWD(x, y)
a//=x
b//=y
print(f"Skrocony ulamek {c}/{d} == {a}/{b}")

#Zadania 7
a = int(input("Licznik: "))
b = int(input("Mianownik: "))
calosci=a//b
reszta=a%b
if reszta==0:
  print(f"Ulamek niewlasciwy to: {calosci}")
else:
  print(f"Ulamek niewlasciwy to: {calosci} i {reszta}/{b}")