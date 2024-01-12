from math import * #поменял from и import местами
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus =>")) #поставил "" ,добавил float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2) # убрал math добавил sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #добавил float()
c=float(input("Sisesta ristküliku 2. külje pikkus => "))  #добавил float()
S=b*c
print("Ristküliku pindala", S)  #поставил ""
P=2*(b+c)
print("Ristküliku ümbermõõt", P) 
di=sqrt(b**2+c**2)  #убрал math
print("Ristküliku diagonaal", round(di,2)) #добавил скобку,добавил 2
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #добавил float()
d=2*r          
print("Ringi läbimõõt"+  str(d))  #добавил скобки,str
S=pi*r**2 # убрад() добавил *
print("Ringi pindala", round(S,2)) # добавил 2
C=2*pi*r        #добавил *
print("Ringjoone pikkus", round(C,2)) #добавил скобки,2
