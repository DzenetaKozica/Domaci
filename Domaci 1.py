#zadatak 1

print "Здраво, геоинформатичари!"
#zadatak 2

a = input("Unesite ceo broj: ")
b = input("Unesite ceo broj: ")
print "Zbir, %s \nRazlika, %s \nProizvod, %s \nCeo broj pri deljenju,%s \nOstatak pri deljenju, %s "%(a+b,a-b,a*b,a%b,a//b)
#Zadatak3#

S1 =input("Unesite stepene:")
M1= input ("Unesite minute:")
SEK1 = input("Unesite sekunde:")

P1= float(S1)+float(M1)/60+ float(SEK1)/3600

S2 =input("Unesite stepene:")
M2= input ("Unesite minute:")
SEK2 = input("Unesite sekunde:")

P2= float(S2)+float(M2)/60+ float(SEK2)/3600
u=P1-P2
print "Ugao izmedju dva pravca je", "%.4f" % round(u,4)

#zadatak4

B1 =int(input("Unesite prvi cetvorocifren broj:"))
B2= int(input ("Unesite drugi cetvorocifren broj:"))
tot=0
while(B2>0):
    dig=B2%10
    tot=tot+dig
    B2=B2//10
print("Suma cifara drugogo cetvorocifrenog broja je:",tot)

P=0
NP=0
P=P+B1%10+(B1/100)%10
NP=NP+(B1/10)%10+(B1/1000)
RAZ=P-NP
print ("Razlika cifara na parnom i neparnom mestu:",RAZ)

#Zadatak5
PET =int(input("Unesite petocifreni broj:"))
for i in range (1,6):
 max=PET%10
 u = (PET / 10) % 10
 if u> max:
  max==u
 i=i+1
print ("Najveca cifra u petocifrenom broju je:",max)

#Zadatak6
lista=[]
i=1
b=0
for i in range (1,6):
 u =input("Unesite karakter")
 lista.append(u)
 i=i+1
 if isinstance(u,int):
     b=b+1
print ("Lista je", lista)
print ("Cifre su se pojavile:",b ,"puta")

#Zadatk7
import math
x1= int(input("Unesite X koordinatu prve tacke trogla:"))
y1= int(input("Unesite Y koordinatu prve tacke trogla:"))
x2= int(input("Unesite X koordinatu druge tacke trogla:"))
y2= int(input("Unesite Y koordinatu druge tacke trogla:"))
x3= int(input("Unesite X koordinatu trece tacke trogla:"))
y3= int(input("Unesite Y koordinatu trece tacke trogla:"))
x0= int(input("Unesite X koordinatu tacke koju proveravamo:"))
y0= int(input("Unesite Y koordinatu tacke koju proveravamo:"))

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
b = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
c = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)

s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

a1 = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
b1 = math.sqrt((x0 - x3)**2 + (y0 - y3)**2)
c1 = math.sqrt((x0 - x2)**2 + (y0 - y2)**2)

s1 = (a+c1+b1)/2
area1 = math.sqrt(s1*(s1-a)*(s1-b1)*(s1-c1))

s2 = (a1+b1+c)/2
area2 = math.sqrt(s2*(s2-a1)*(s2-b1)*(s2-c))

s3  = (a1+b+c1)/2
area3 = math.sqrt(s3*(s3-a1)*(s3-b)*(s3-c1))

zbir = area1+area2+area3
if area==zbir :
 print ("Da, tacka se nalazi unutar trougla")
else:
 print ("Ne, tacka se ne nalazi unutar trougla")

#Zadatak 8

import random
ZB=random.randint(0,100)
print "--------IGRA:Pogodi broj---------\n"
ime = input ("Unesite vase ime:")
print( ime + ' zamisljeni broj se nalazi u intervalu izmedju 1 i 100')
pokusaj=0

while pokusaj < 50:
    broj=int(input("Vas broj je:"))
    pokusaj = pokusaj + 1
    if broj < ZB:
        print("Vas broj je manji od zamisljenog broja")
    if broj > ZB:
        print("Vas broj je veci od zamisljenog broja")
    if broj==ZB:
        pokusaj = str(pokusaj)
        print('Bravo, ' + ime + '! Pogodio si moj broj iz ' + pokusaj + ' puta!')









