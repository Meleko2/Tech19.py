#Odfejmowanie

a = int(input())
b = int(input())

while a != b:
  if a>b:
    a-=b
  else:
    b-=a
print(f"NWD tych liczb to {a}")


#Modulo
while b > 0:
  a = b
  b = a%b
print(f"NWD tych liczb to {a}")

#Tabelka jak to dziala w odejmowaniu




#Tabelka jak to dziala w modulo
while b>0:
  print(f"{a}\t\t{b}\t\t{a%b}")
  