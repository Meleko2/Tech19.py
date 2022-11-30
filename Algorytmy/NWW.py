a = int(input())
b = int(input())

c = a*b

#a*b=NWD*NWW
#Obliczanie NWW = a*b/nwd
#Odejmwanie

while a != b:
  if a>b:
    a-=b
  else:
    b-=a

nww = c//b
print(f"NWW tych liczb wynosi: {nww}")


#NWW w modulo

while b > 0:
  a = b
  b = a%b

print(f'nww tych liczb to: {c//a}')