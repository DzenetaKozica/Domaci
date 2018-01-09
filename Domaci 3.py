#Zadatak1============================================================================
import math
#Sfera
class Sfera:
    broj=0
    def __init__(self, x = 0, y = 0,z=0,r=1):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        Sfera.broj += 1

    @staticmethod
    def broj_sfera():
        return (Sfera.broj)

    def zapremina(self):
        v=float(self.r)
        return (4/3)*v**3*math.pi

# Glavni program pozivanje

print Sfera.broj_sfera()
sfera=Sfera(0,0,0,4.0)
globus=Sfera(1.0,1.0,1.0,12)
bilijarska_lopta=Sfera(10.0,10.0,10.0,10.0)
jedinicna_sfera=Sfera()
print Sfera.broj_sfera()
print "Zapremina sfere je", sfera.zapremina()
print "Zapremina globusa je", globus.zapremina()
print "Zapremina bilijarske_lopte je", bilijarska_lopta.zapremina()
print "Zapremina jedinicne_sfere je", jedinicna_sfera.zapremina()

#Zadatak2============================================================================
import math
#Tacka
class Tacka:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def pomeranje(self,x_pomeraj,y_pomeraj):
        self.x=self.x+x_pomeraj
        self.y = self.y + y_pomeraj
    def rastojanjeDo(self,t):
        dx=(self.x-t.x)**2
        dy = (self.y - t.y)**2
        return math.sqrt(dx+dy)
#Duz
class Duz:
    def __init__(self,p=0,k=0):
        self.p=p
        self.k=k
    def kreiraj_duz(self,xp,yp,xk,yk):
        p=Tacka(xp,yp)
        k=Tacka(xk,yk)
        d=Duz(p,k)
        return d
    def duzinaDuzi(self):
        return self.p.rastojanjeDo(self.k)
    def str(self):
        print self.p.x,self.p.y,self.k.x,self.k.y,
# Glavni program pozivanje
xp=float(input("Unesite x koordinatu pocetne tacke"))
yp=float(input("Unesite y koordinatu pocetne tacke"))
xk=float(input("Unesite x koordinatu krajnje tacke"))
yk=float(input("Unesite y koordinatu krajnje tacke"))
p=Tacka(xp,yp)
k=Tacka(xk,yk)
druga_duz=Duz(k,p)
druga_duz1=druga_duz.kreiraj_duz(10,12,15,16)
prva_duz=Duz(p,k)
print "Prva duz je sa sledecim koordinatama (x_pocetni,y_pocetni,x_krajnji,y_krajnji) " ,prva_duz.str()
print "Druga duz je sa sledecim koordinatama(x_pocetni,y_pocetni,x_krajnji,y_krajnji)",druga_duz1.str()
dx=float(input("Unesite dx"))
dy=float(input("Unesite dy"))
k.pomeranje(dx,dy)
nova_duz=Duz(p,k)
print "Nova duz (x_pocetni,y_pocetni,x_krajnji,y_krajnji) ", nova_duz.str()

#Zadatak3============================================================================
import math

#Tacka
class Tacka:

    def __init__(self, x = 0, y = 0, z=0, ID=0):
        self.x = x
        self.y = y
        self.z = z
        self.ID=ID

    def rastojanjeDo(self,t):
        dx=(self.x-t.x)**2
        dy = (self.y - t.y)**2
        return math.sqrt(dx+dy)

    def veceZ(self,t):
        if self.z >= t.z:
            return self
        else:
            return t

    def manjeZ(self, t):
        if self.z <= t.z:
            return self
        else:
            return t

    def str(self):
        print  self.x ,self.y, self.z, self.ID

#Povrs
class Povrs:

    def __init__(self,ime,lista_tacaka,broj_tacaka):
        self.ime = ime
        self.lista_tacaka =lista_tacaka
        self.broj_tacaka=broj_tacaka

    def metaPodaci(self):
        for i in self.lista_tacaka:
            i.str()
        print  "Ime osobe koja analizira povrs: ",self.ime
        print "Broj tacaka povrsi: ",self.broj_tacaka

    def najblizaTacka(self,t):
        najbl=99999999999
        tacka=Tacka()
        for i in lista_tacaka:
            if i.ID!=t.ID:
                if t.rastojanjeDo(i)<najbl:
                    najbl=t.rastojanjeDo(i)
                    tacka=i
        return tacka.ID

    def srednjaPovrs(self):
        listax=[]
        listay=[]
        for j1 in self.lista_tacaka:
            listax.append(float(j1.x))
            listay.append(float(j1.y))
        xp1=[]
        xp1.append(float(listax[int(len(listax))-1]))
        xp2=[]
        i=0
        while i<int((len(listax)-1)):
            xp1.append(float(listax[i]))
            i+=1
            xp2.append(float(listax[i]))
        xp2.append(float(listax[0]))
        j=0
        sum=0
        while j<len(listax):
            sum+=listay[j]*(xp1[j]-xp2[j])
            j+=1
        re=[listay,xp1,xp2]
        sum1=float(sum)
        pov=sum1*0.5
        return pov

    def mini(self,lista):
        i=0
        mine=9999999999999999999999
        while i<len(lista):
            if (lista[i]<mine):
                mine=lista[i]
            i+=1
        return mine

    def maxi(self,lista):
        i = 0
        maxe =-99999999999999999
        while i < len(lista):
            if (lista[i] > maxe):
                maxe = lista[i]
            i += 1
        return maxe

    def MBBOX(self):
        listax = []
        listay = []
        for j1 in self.lista_tacaka:
            listax.append(float(j1.x))
            listay.append(float(j1.y))
        return [(self.mini(listax),self.maxi(listay)),(self.maxi(listax),self.maxi(listay)),(self.maxi(listax),self.mini(listay)),(self.mini(listax),self.mini(listay))]

    def vratiTacku(self,id):
        i=0
        d=len(self.lista_tacaka)
        while i<d:
            if lista_tacaka[i].ID==id:
                return lista_tacaka[i]
                i=i+d
            i+=1

    def interpolacija(self,i1,i2,t):
        a=self.vratiTacku(i1)
        b=self.vratiTacku(i2)
        if ((a.rastojanjeDo(t)+b.rastojanjeDo(t))==a.rastojanjeDo(b)):
            veca=a.veceZ(b)
            manja=a.manjeZ(b)
            x1=veca.z-manja.z
            d1=veca.rastojanjeDo(t)
            d=veca.rastojanjeDo(manja)
            x=(x1*d1)/d
            t.z=veca.z-x
            return t
        else:
            t.z="Tacka za interpolaciju nije na pravcu."
            return t
#Glavni program
n=int(input("Unesite broj tacaka  "))
i=0
lista_tacaka=[]
lista_id=[]
while i<n:
    x=raw_input("Unesite koordinate (nacin unosa je x,y,z) ")
    c=x.split(",")
    id=input("Unesite ID tacke  ")
    if lista_id.count(id)!= 0:
        print "Vec postoji taj ID molimo unesite drugi"
        id=id=input("Unesite ID tacke  ")
    lista_id.append(id)
    lista_tacaka.append(Tacka((float(c[0])),(float(c[1])),(float(c[2])),id))
    i+=1
ime=raw_input("Unesite ime operatera  ")
p=Povrs(ime,lista_tacaka,int(n))
a=Tacka()
a1=p.najblizaTacka(a)
print "Najbliza tacki a je tacka sa sledecim ID-ijem  ",a1
l=p.srednjaPovrs()
print "Srednja povrsina je=  ",l
print "Koordinate minimalnog obuhvatnog pravougaonika su (x,y)  ",p.MBBOX()
x1=raw_input("Unesite koordinate tacke koju zelite da interpolujete (nacin unosa je x,y) ")
c1=x1.split(",")
ti=Tacka((float(c1[0])),(float(c1[1])),0)
id1=input("Unesite ID prve tacke koja ucestvuje u interpolaciji ")
id2=input("Unesite ID druge tacke koja ucestvuje u interpolaciji ")
inter=p.interpolacija(id1,id2,ti).z
print "Interpolovana visina za trazenu tacku je  ",inter

#Zadatak4============================================================================

class Inzenjer:

    def __init__(self, ime="Pera", prezime="Peric", maticnibroj="00664", licenca="Nema licencu"):
        self._ime = ime
        self._prezime = prezime
        self._maticnibroj = maticnibroj
        self._licenca=licenca

    def dajIme(self):
        return self._ime

    def dajPrezime(self):
        return self._prezime

    def dajMaticnibroj(self):
        return self._maticnibroj

    def dajLicencu(self):
        return self._licenca

    def postaviIme(self,ime):
        self._ime = ime

    def postaviPrezime(self,prezime):
        self._prezime = prezime

    def postaviLicencu(self,licenca):
        self._licenca = licenca

    def postaviIme(self,maticnibroj):
        self._maticnibroj = maticnibroj

    def info(self):
        print self._ime,self._prezime,self._maticnibroj,self._licenca

class GeodetskiInzenjer(Inzenjer):

    def __init__(self, ime="Pera", prezime="Peric", maticnibroj="00664", licenca="Nema licencu",god_radni_staz=0):
        Inzenjer.__init__(self, ime, prezime,maticnibroj,licenca)
        self._god_radni_staz = god_radni_staz

    def dajGodStaz(self):
        return self._god_radni_staz

    def postaviGodStaz(self,godstaz):
        self._god_radni_staz = godstaz

    def infoLicenca(self):
        a=self.dajLicencu()
        if a=="Nema licencu":
            print "Inzenjer nema licencu"
        else:
            print "Licenca inzenjera je ",a

    def info(self):
        print self._ime,self._prezime,self._maticnibroj,self._licenca,self._god_radni_staz

class ElektrotehnickiInzenjer(Inzenjer):

    def __init__(self, ime="Pera", prezime="Peric", maticnibroj="00664", licenca="Nema licencu", br_projekata=0):
        Inzenjer.__init__(self, ime, prezime, maticnibroj, licenca)
        self._br_projekata = br_projekata

    def dajBrProjekata(self):
        return self._br_projekata

    def postaviBrProjekata(self, br_projekata):
        self._br_projekata = br_projekata

    def infoLicenca(self):
        a = self.dajLicencu()
        if a == "Nema licencu":
            print "Inzenjer nema licencu"
        else:
            print "Licenca inzenjera je ",a

    def info(self):
        print self._ime, self._prezime, self._maticnibroj, self._licenca, self._br_projekata

#Glavni program pozivanje

ime=raw_input("Unesite ime inzenjera  ")
prezime=raw_input("Unesite prezime inzenjera  ")
matic=raw_input("Unesite maticni broj inzenjera  ")
lic=raw_input("Unesite licencu inzenjera  ")
god=int(input("Unesite broj projekata  "))
a=ElektrotehnickiInzenjer(ime,prezime,matic,lic,god)
a.info()
print a.dajIme()

a.infoLicenca()
a.info()

##Zadatak5============================================================================

class Osoba:

    def __init__(self, ime="Pera", prezime="Peric", datum_rodjenja="01.01.1990.", adresa="Njegoseva 15"):
        self._ime = ime
        self._prezime = prezime
        self._datum_rodjenja = datum_rodjenja
        self._adresa=adresa

    def dajIme(self):
        return self._ime

    def dajPrezime(self):
        return self._prezime

    def dajDatumRodjenja(self):
        return self._datum_rodjenja

    def dajAdresu(self):
        return self._adresa

    def postaviIme(self,ime):
        self._ime = ime

    def postaviPrezime(self,prezime):
        self._prezime = prezime

    def postaviAdresu(self,adresa):
        self._adresa = adresa

    def postaviDatumRodjenja(self,datum_rodjenja):
        self._datum_rodjenja = datum_rodjenja

    def info(self):
        print self._ime,self._prezime,self._datum_rodjenja,self._adresa

class Djak(Osoba):

    def __init__(self, ime="Pera", prezime="Peric", datum_rodjenja="01.01.1990.", adresa="Njegoseva 15",naziv_skole="Sveti Sava",odeljenje="II-2",godina_upisa="2017"):
        Osoba.__init__(self, ime, prezime,datum_rodjenja,adresa)
        self._naziv_skole = naziv_skole
        self._odeljenje = odeljenje
        self._godina_upisa = godina_upisa

    def dajNazivSkole(self):
        return self._naziv_skole

    def dajOdeljenje(self):
        return self._odeljenje

    def dajGodinuUpisa(self):
        return self._godina_upisa

    def postaviNazivSkole(self,naziv_skole):
        self._naziv_skole = naziv_skole

    def postaviOdeljenje(self,odeljenje):
        self._odeljenje = odeljenje

    def postaviGodinuUpisa(self,godina_upisa):
        self._godina_upisa = godina_upisa

    def trenutniRazred(self):
        a=str(self.dajOdeljenje())
        a1=a.split("-")
        return a1[0]

    def obnavljanje(self,p):
        l=self.dajDatumRodjenja()
        l1=l.split(".")
        godr=int(l1[2])
        u=int(self.dajGodinuUpisa())
        brgod=2017-godr
        if p==brgod:
           print "Nije ponavljao"
        else:
            print "Ponavljao je"


    def info(self):
        print self._ime,self._prezime,self._datum_rodjenja,self._adresa,self._naziv_skole,self._odeljenje,self._godina_upisa

class Zaposlen(Osoba):

    def __init__(self, ime="Pera", prezime="Peric", datum_rodjenja="01.01.1990.", adresa="Njegoseva 15",kompanija="RGZ",departman="II",lista_zakljucenja=[],lista_prekida=[]):
        Osoba.__init__(self, ime, prezime,datum_rodjenja,adresa)
        self._kompanija = kompanija
        self._departman = departman
        self._lista_zakljucenja = lista_zakljucenja
        self._lista_prekida = lista_prekida

    def dajKompaniju(self):
        return self._kompanija

    def dajDepartman(self):
        return self._departman

    def dajListuZakljucenja(self):
        return self._lista_zakljucenja

    def dajListuPrekida(self):
        return self._lista_prekida

    def postaviKompaniju(self,kompanija):
        self._kompanija = kompanija

    def postaviDepartman(self,departman):
        self._departman = departman

    def postaviListuZakljucenja(self,lista_zakljucenja):
        self._lista_zakljucenja = lista_zakljucenja

    def postaviListuPrekida(self,lista_prekida):
        self._lista_prekida = lista_prekida

    def radniStaz(self):
        listaz=self.dajListuZakljucenja()
        listap=self.dajListuPrekida()
        i=0
        brrd=0
        while i<len(listap):
            z=listaz[i]
            p=listap[i]
            z1=z.split(".")
            p1=p.split(".")
            d1=int(z1[0])
            m1=int(z1[1])
            g1 = int(z1[2])
            d2 = int(p1[0])
            m2 = int(p1[1])
            g2 = int(p1[2])
            if d1<=d2:
                d=d2-d1
            else:
                d=d2-d1+30
                m2=m2-1
            if m1 <= m2:
                 m=m2-m1
            else:
                m=m2-m1+12
                g2=g2-1
            g=g2-g1
            brm=m+g*12
            brrd=brrd+brm*30+d
            i+=1
        return brrd

    def info(self):
        print self._ime,self._prezime,self._datum_rodjenja,self._adresa,self._kompanija,self._departman,self._lista_zakljucenja,self._lista_prekida

#Glavni program pozivanje
recnik1 = {'Prvi razred':7, 8:'Drugi razred', 9:'Treci razred' , 10:'Cetvrti razred',11:'Peti razred',12: 'Sesti razred',13:'Sedmi razred', 14:'Osmi razred'}
recnik2 = {'I':'Prvi razred', 'II':'Drugi razred', 'III':'Treci razred' , 'IV':'Cetvrti razred','V':'Peti razred','VI': 'Sesti razred','VII':'Sedmi razred', 'VIII':'Osmi razred'}
kontr=raw_input("Unesite oznaku za koju vrstu osobe hocete da unosite podatke (D-djak, Z-zaposlen)  ")
if kontr=="D":
    ime = raw_input("Unesite ime djaka  ")
    prezime = raw_input("Unesite prezime djaka  ")
    datumr = raw_input("Unesite datum rodjenja djaka (dan.mesec.godina)  ")
    adresa = raw_input("Unesite adresu djaka  ")
    skola = raw_input("Unesite naziv skole u koju djak ide  ")
    odeljenje = raw_input("Unesite odeljenje u koje djak trenutno ide (razred - odeljenje (npr. I-1, II-2, III-3....)  " )
    datumup = raw_input("Unesite godinu upisa  ")
    dj=Djak(ime,prezime,datumr,adresa,skola,odeljenje,datumup)
    r=dj.trenutniRazred()
    print "Djak trenutno ide u  ",recnik2[r]
    dj.obnavljanje(recnik1[recnik2[r]])
    dj.info()

elif kontr=="Z":
    lista_z=[]
    lista_p=[]
    ime = raw_input("Unesite ime zaposlenog  ")
    prezime = raw_input("Unesite prezime zaposlenog  ")
    datumr = raw_input("Unesite datum rodjenja zaposlenog (dan.mesec.godina)  ")
    adresa = raw_input("Unesite adresu zaposlenog  ")
    kompanija = raw_input("Unesite naziv kompanije  ")
    departman = raw_input("Unesite naziv departmana  ")
    brf=int(input("Unesite broj firmi u kojima je zaposlen do sada radio.  "))
    i=0
    while i<brf:
        datum_zakljucenja = raw_input("Unesite datum zakljucenja radnog odnosa (dan.mesec.godina: 12.2.2008)  ")
        datum_prekida = raw_input("Unesite datum prekida radnog odnosa (dan.mesec.godina: 13.8.2010)  ")
        lista_z.append(datum_zakljucenja)
        lista_p.append(datum_prekida)
        i+=1
    nr=raw_input("Da li zaposlen trenutno negde radi(DA ili NE)  ")
    if nr=="DA":
        datum_zakljucenja=raw_input("Unesite datum zakljucenja novog ugovora (dan.mesec.godina: 12.2.2008)  ")
        datum_prekida = raw_input("Unesite danasnji datum (dan.mesec.godina: 12.8.2018)  ")
        lista_z.append(datum_zakljucenja)
        lista_p.append(datum_prekida)
    za = Zaposlen(ime, prezime, datumr, adresa, kompanija, departman, lista_z,lista_p)
    lis=[za.radniStaz()/30,za.radniStaz()%30]
    print "Radni staz zaposlenog je tacno ",lis[0] , " meseci i ", lis[1], "dana."
    za.info()
else:
print "Pogresno ste uneli oznaku za osobu"