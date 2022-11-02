#Zad 1
print("ZADANIE 1")
n = int(input())
for i in range(n):
  print("*-|", end="")
print(' ')

#Zad 2
print("ZADANIE 2")
n = int(input())
for i in range(1, n+1):
  print("*"*i, end="")
  if i%2:
    print("||", end="")
  else:
    print("--", end="")
print(" ")

#Zad 3
print("ZADANIE 3")
n = int(input())
for i in range(1 ,n+1):
    print("*", end="")
    if i%2 == 1:
        print("|"*i, end="")
    else:
        print("-"*i , end="")
print(" ")

#pre - tabliczka mnozenia
for i in range(1,11): #wiersze
    for j in range(1,11): #kolumny
        print(i*j, end="\t")
    print()

#Pre na 2 petle

# *
# **
# ***
# ****
n = int(input())
for i in range(1,n):
    for j in range(i):
        print("*", end=" ")
    print()
print()

#pre
# *
# **
# ***
# ****

# ****
# ***
# **
# *
for i in range(1, n):
    for j in range(n-i):
        print("*", end=" ")
    print()
print()

#    *
#   **
#  ***
# ****
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(n-i-1, n):
        print("*", end="")
    print()
print()

# ****
#  ***
#   **
#    *
for i in range(n):
     for j in range(i):
        print(" ",end="")
     for k in range(i, n):
         print("*", end="")
     print()
print()

#PRE 2 sposob(if)

# *
# **
# ***
# ****
n = int(input())
for i in range(n):
     for j in range(n):
        if i >= j:
            print("*", end="")
        else:
            print(" ", end="")
     print()
print()

# ****
# ***
# **
# *
for i in range(n):
  for j in range(n):
    if i + j <= n - 1:
      print("*", end="")
    else:
      print(" ", end="")
  print()
print()

#    *
#   **
#  ***
# ****

# ****
#  ***
#   **
#    *

for i in range(n):
  for j in range(n):
    if j >= i:
      print("*", end="")
    else:
      print(" ", end="")
  print()

#diagonal
for i in range(n):
  for j in range(n):
    if i == j:
      print("*", end="")
    else:
      print(" ", end="")
  print()

#w druga strone sposob 2
for i in range(n):
  for j in range(n):
    if i + j == n - 1:
      print("*", end="")
    else:
      print(" ", end="")
  print()
print()

#w 2 strone sposob 1
for i in range(n):
  for j in range(n):
    if i == n - j - 1:
      print("*", end="")
    else:
      print(" ", end="")
  print()
print()

#Zad 4

#Zad 5
n = int(input())
for i in range(1, n):
  print("   ", "*")
  if i % 3 == 0:
    print("- - * - -")

#Zad 6

#Zad 7
