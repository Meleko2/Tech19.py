# Program dodajacy 2 ulamki

a = int(input("Podaj licznik:"))
b = int(input("Podaj mianownik:"))

c = int(input("Podaj licznik:"))
d = int(input("Podaj mianownik: "))

mianownik_w1 = b
mianonik_w2 = d

#nww / b = iloczyn gotowy

ilocz = b*d

while b!=d:
  if d>b: 
    d-=b
  else:
    b-=d

wsp_mian = ilocz//b


licznik = licznik1 + licznik2

print(f"{licznik} \ {wsp_mian}")