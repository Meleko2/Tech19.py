#algorytm sprawdzajacy czy liczba jest pierwsza
# wersja 1
n = int(input())
for i in range(2,n):
  if n%i==0:
    print("Liczba nie jest pierwsza")
    exit(0)
print("Liczba jest pierwsza")

#wersja 2
flaga = True
for i in range(2,n):
  if i%n==0:
    flaga=False
if flaga == True:
  print("Licbza jest pierwsza")
else:
  print("Liczba nie jest pierwsza")

#Wersja 3-the best
from math import sqrt
n = int(input())
for i in range(2, int(sqrt(n))+1):
  if n%i==0:
    print("Liczba nie jest pierwsza")
  else:
    print("Liczba jest pierwsza")
  
#2. generator liczb pierwszych- liczby pierwsze w przewdziale[p, q]
p = int(input())
q = int(input())
for i in range(p, q+1):
  flaga = True
  for j in range(2,int(i**0,5)+1):
    if i%j == 0:
      flaga = False
    if flaga:
      print(i, end=" ")

#3. generator liczb pierwszych - poczatkowe k liczb pierwszych
k = int(input())
while True:
  k-=1
  if k == 0:
    break


#3-2 sposob
n = int(input())
x=2
while 1:
  flaga = True
  for i in range(2, int(x**0.5)+1):
    if x%i == 0:
      flaga=False
    if flaga:
      print(x, end=" ")
      


    
  bo sie penda psozmnialo
  //Tablice - (zmienna do trzymania wielu zmiennych
int[] T = new int[5];
T[0] = 3;
T[1] = 5;
T[2] = 6;
T[3] = 7;
T[4] = 10;


for (int i = 0; i < T.Length; i++)
{
    Console.WriteLine(T[i]);
}

Console.WriteLine();

//To taki niezalecany zapis
int[] A = { 2, 3, 5, 8, 13, 21, 34, 55 };
for (int i = 0; i < A.Length; i++)
{
    Console.WriteLine($"K[{i}] = {A[i]}");
}

int[] G;
G = new int[] { 1, 3, 5 };

Console.WriteLine();

//Znajdz maksymalna wartosc tablicy [4,5,8,9,7,6]
int[] L = new int[]
{ 4, 5, 8, 9, 7, 6 };

int maks = 0;
for (int i = 0; i < L.Length; i++)
{
    if (L[i] > maks)
    {
        maks = L[i];
    }
}
Console.WriteLine($"Najwieksza wartosc w tej talbicy to: {maks}");

Console.WriteLine();

//Znajdz najnizsza wartosc w talibcy [6,2,1,3,9,5]
int[] H = new int[]
{6,2,1,3,9,5,};

int minimum = L[0];
for (int i = 0; i < H.Length; i++)
{
    if (H[i]<minimum)
    {
        minimum = H[i];
    }
}
Console.WriteLine($"Najmniejsza wartosc w tej talbicy to: {minimum}");
    





