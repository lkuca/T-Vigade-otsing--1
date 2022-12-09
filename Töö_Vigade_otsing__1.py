from math import * #import * from math

print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #"", float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2) # change to math
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")#-)
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #float
c=float(input("Sisesta ristküliku 2. külje pikkus => "))#float
S=b*c
print("Ristküliku pindala", S)#changed ""
P=2*(b+c)#cahnged formula
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2)#** **
print("Ristküliku diagonaal", round(di, 2))#+,2
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => '))#+float
d=2*r
print("Ringi läbimõõt", d)
S=pi*r**2#() **
print("Ringi pindala", round(S, 2))
C=2*pi*r#()
print("Ringjoone pikkus", round(C, 2))#+,2 +)