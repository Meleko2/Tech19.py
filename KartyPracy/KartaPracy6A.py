#Zadania 1 - do zrozumienia
x = int(input())
suma = 0
while x > 0:
  suma += x % 10
  x //= 10

print(suma)

#Zadania 2
x = int(input())
temp = 0
for i in range(1,x):
  if x%i == 0:
    temp+=1
if temp<3:
  print("tak")
else:
  print("nie")
    
#Zadania 3 - doskonale- dzielniki dodane do siebie daja ta liczbe nie liczac jej samej
n = int(input())
suma = 0
for i in range(1,n):
  if i%n == 0:
    suma+=i
if suma==n:
  print("Jest doskonala")
else:
  print("Nie jest doskonala")

#Zadania 4 - wzglednie pierwsze- ich nwd = 1
x = int(input())
y = int(input())
while x!=y:
  if x>y:
    x-=y
  if y>x:
    y-=x
if x==1:
  print("Liczby sa wzglednie pierwsze")
else:
  print("Liczby nie sa wzglednie pierwsze")

#Zadania 5
m = int(input())
for i in range(10,20):
  x = m
  y = i
  while y>0:
    x,y=y, x%y
  if x==1:
    print(f"Pasuje dla: {m}, {i}")
    
#Zadania 6
a=int(input())
b=int(input())
a,b=x,y
while x!=y:
  if x>y:
    x-=y
  else:
    y-=x
a//=x
b//=y
print(f"Skrocony ulamek {a}/{b}")