#zad 1
a=int(input())
if a % 3 == 0:
  print("tak")
else:
  print('nie')
#zad 2
a = int(input())
if a%17 == 0 and a>=100 and a<1000:
  print('tak')
else:
  print('nie')
#zad 3
wiek=int(input("Ile masz lat"))
if wiek>=18:
  print('tak')
else:
  print('nie')
#zad 4
limit=20
waga = int(input())
if waga>limit:
    print('nie')
else:
    print('tak')
#zad 5
a = int(input())
b = int(input())
c = int(input())
if a < c < b or a > c > b :
    print("TAK")
else :
    print("NIE")