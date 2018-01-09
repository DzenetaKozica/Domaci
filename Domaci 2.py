#Zadatak1============================================================================
def sumaP(niz):
    suma=0
    d=len(niz)
    i=1
    while i< d:
        suma=suma+niz[i]
        i=i+2
    return suma
#Glavni program pozivanje
niz=input("Unesite niz brojeva, elemente odvajati zarezom  ")
sumapr=sumaP(niz)
print "Suma parnih elemenata niza je=", sumapr

#Zadatk2============================================================================
def sumaEl(niz):
    suma=0
    d=len(niz)
    i=0
    while i< d:
        suma=suma+niz[i]
        i=i+1
    return suma
#Glavni program pozivanje
niz=input("Unesite niz brojeva, elemente odvajati zarezom ")
sumael=sumaEl(niz)
print "Suma elemenata niza je=", sumael

#zadatak3============================================================================
def proizvodEl(niz):
    suma=1
    d=len(niz)
    i=0
    while i< d:
        suma=suma*niz[i]
        i=i+1
    return suma
#Glavni program
niz=input("Unesite niz brojeva, elemente odvajati zarezom ")
prel=proizvodEl(niz)
print "Proizvod elemenata niza je=", prel


#ZADATAK4============================================================================
def noviNiz(niz1,niz2):
    nov=[]
    n1=len(niz1)
    n2=len(niz2)
    i=0
    k=0
    if n1<n2:
        while i<n1:
            nov.insert(k,niz1[i])
            k=k+1
            nov.insert(k, niz2[i])
            i=i+1
            k=k+1
        while i<n2:
            nov.insert(k, niz2[i])
            i+=1
            k+=1
    elif n1>n2:
        while i<n2:
            nov.insert(k, niz1[i])
            k=k+1
            nov.insert(k, niz2[i])
            i=i+1
            k=k+1
        while i<n1:
            nov.insert(k, niz1[i])
            i+=1
            k+=1
    else:
        while i<n1:
            nov.insert(k, niz1[i])
            k=k+1
            nov.insert(k, niz2[i])
            i=i+1
            k=k+1
    return nov

#Glavni program pozivanje
niz1=input("Unesite prvi niz  elemente odvajati zarezom ")
niz2=input("Unesite drugi niz  elemente odvajati zarezom ")
opcija=raw_input("Unesite opciju (p-prvi niz ili d-drugi niz) ")
proba=[]
if opcija=="p":
    proba=noviNiz(niz1, niz2)
elif opcija=="d":
    proba=noviNiz(niz2,niz1)
else:
    print"pogresna opcija"
j=0
s=len(proba)
while j<s:
    print (proba[j])
j=j+1

#ZADATAK5============================================================================
rec=raw_input("Unesite recenicu ")
i=0
s=len(rec)
while i<s:
    if rec[i]==" ":
        i+=1
    else:
        print rec[i]
        i+=1


#ZADATAK6============================================================================
a=int(input("Unesi broj tacaka:"))
i=0
lista_x=[]
lista_y=[]
listak=[]
while i<a:
    x=raw_input("Unesite  koordinate X,Y :")
    x1=x.split(",")
    lista_x.append(float(x1[0]))
    lista_y.append(float(x1[1]))
    i+=1
n=int(input("Unesi stepen polinoma :"))
i1=0
while i1<n:
    s=1
    t=1
    a1=1
    j=0
    while j<n:
        if j!=i1:
            s=s*(a1-lista_x[j])
            t=t*(lista_x[i1]-lista_y[j])
        j+=1
    listak.append((s/t)*lista_y[i1])
    i1+=1

print "Polinom P(X)=",round(listak[0],2),"*X^",n,
m=n
j1=1
while j1<len(listak):
    if listak[j1]>0:
        print "+",round(listak[j1],2),"*X^",m-1,
    else:
        print round(listak[j1],2), "*X^", m-1,
    j1+=1
    m-=1
print "+",a1

#ZADATAK7 AJNC ============================================================================
import random
a=int(random.uniform(0,51))

def deliKartu(karte,listaRandom):
    i=0
    while i==0:
        r = int(random.uniform(0, 51))
        a = listaRandom.count(r)
        if a==0:
            i=1
        else:
            i=0
    pov=[]
    pov.append(karte[r])
    pov.append(r)
    return pov

def vrednost(lista,spil):
    i = 0
    vri = 0
    b=0
    while i < len(lista):
        if int(spil[lista[i]])!=1:
            vri = vri + int(spil[lista[i]])
        else:
            b+=1
        i += 1
    j=0
    while j<b:
        if vri>=12:
            vri=vri+1
        else:
            vri=vri+10
        j+=1

    return vri

def stampa(lista):
    i=0
    while i<len(lista):
        print lista[i]
        i+=1

def uslov1(vrr,vri):
    if (vrr<21 and vri<21):
        return 1
    else:
        return 0

karte=['Srce Kec','Srce 2','Srce 3','Srce 4','Srce 5','Srce 6','Srce 7','Srce 8','Srce 9','Srce 10','Srce Zandar','Srce Dama','Srce Kralj',
       'Tref Kec', 'Tref 2', 'Tref 3', 'Tref 4', 'Tref 5', 'Tref 6', 'Tref 7', 'Tref 8', 'Tref 9', 'Tref 10','Tref Zandar', 'Tref Dama', 'Tref Kralj',
       'Pik Kec', 'Pik 2', 'Pik 3', 'Pik 4', 'Pik 5', 'Pik 6', 'Pik 7', 'Pik 8', 'Pik 9', 'Pik 10','Pik Zandar', 'Pik Dama', 'Pik Kralj',
       'Kocka Kec', 'Kocka 2', 'Kocka 3', 'Kocka 4', 'Kocka 5', 'Kocka 6', 'Kocka 7', 'Kocka 8', 'Kocka 9', 'Kocka 10', 'Kocka Zandar','Kocka Dama', 'Kocka Kralj']

spil = dict([('Srce Kec',1), ('Srce 2',2),('Srce 3',3), ('Srce 4',4),('Srce 5',5), ('Srce 6',6),('Srce 7',7), ('Srce 8',8),('Srce 9',9), ('Srce 10',10),('Srce Zandar',10), ('Srce Dama',10),('Srce Kralj',10),
             ('Tref Kec', 1), ('Tref 2', 2), ('Tref 3', 3), ('Tref 4', 4), ('Tref 5', 5), ('Tref 6', 6), ('Tref 7', 7),('Tref 8', 8), ('Tref 9', 9), ('Tref 10', 10), ('Tref Zandar', 10), ('Tref Dama', 10), ('Tref Kralj', 10),
             ('Pik Kec', 1), ('Pik 2', 2), ('Pik 3', 3), ('Pik 4', 4), ('Pik 5', 5), ('Pik 6', 6), ('Pik 7', 7),('Pik 8', 8), ('Pik 9', 9), ('Pik 10', 10), ('Pik Zandar', 10), ('Pik Dama', 10), ('Pik Kralj', 10),
             ('Kocka Kec', 1), ('Kocka 2', 2), ('Kocka 3', 3), ('Kocka 4', 4), ('Kocka 5', 5), ('Kocka 6', 6), ('Kocka 7', 7),('Kocka 8', 8), ('Kocka 9', 9), ('Kocka 10', 10), ('Kocka Zandar', 10), ('Kocka Dama', 10), ('Kocka Kralj', 10)])

ime=raw_input("Unesite vase ime  ")
listaIgrac=[]
listaRacunar=[]
listaRandom=[]
i=0
while i<2:
    pdi=[]
    pdi=deliKartu(karte,listaRandom)
    listaIgrac.append(pdi[0])
    listaRandom.append(pdi[1])
    i+=1
ra=0
while ra<2:
    pdr=[]
    pdr=deliKartu(karte,listaRandom)
    listaRandom.append(pdr[1])
    listaRacunar.append(pdr[0])
    ra+=1

vrr=vrednost(listaRacunar,spil)
vri=vrednost(listaIgrac,spil)
stampa(listaIgrac)
provera=int(uslov1(vrr,vri))
while provera==1:
    no = raw_input("Da li zelite jos da igrate? (DA ili NE) ")
    if no == "DA":
        a=deliKartu(karte,listaRandom)
        listaIgrac.append(a[0])
        listaRandom.append(a[1])
        ra=deliKartu(karte,listaRandom)
        listaRacunar.append(ra[0])
        listaRandom.append(ra[1])
        print "Nova karta je  ",a[0]
        vrr=vrednost(listaRacunar, spil)
        vri=vrednost(listaIgrac, spil)
        provera=int(uslov1(vrr,vri))
    else:
        print "Igrac se predaje"
        provera=0
        vri=vri+20

if vrr==21:
    print "Racunar je pobedio i vrednost njegovih karata je 21!"
elif vri==21:
    print "Igrac ",ime," je pobedio i vrednost njegovih karata je 21!"
elif vri<21:
    print "Igrac ",ime," je pobedio i vrednost njegovih karata je" ,vrednost(listaIgrac,spil)
elif vrr<21:
    print "Racunar je pobedio i vrednost njegovih karata je ",vrednost(listaRacunar,spil)
elif  vri>21 and vri>vrr:
    print "Igrac ",ime," je izgubio i vrednost njegovih karata je ", vrednost(listaIgrac,spil)
elif vrr>21 and vrr>vri:
    print "Racunar je izgubio i vrednost njegovih karata je ", vrednost(listaRacunar,spil)
elif vrr==vri:
    print "NEMA POBEDNIKA"

if no=="DA":
    print "Vrednost igraca je  ",vrednost(listaIgrac,spil)
dal=raw_input("Da li zelite da vidite protivnikove karte? (DA ili NE) ")
if dal=="DA":
    print "Sve karte koje je imao racunar"
    stampa(listaRacunar)
print 'Vrednost racunara', vrednost(listaRacunar,spil)