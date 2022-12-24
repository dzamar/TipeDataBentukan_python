#Nama file: TugasTipeBentukan_KelasC_Cholid_Dzamar.py
#Deskripsi: Tugas mata kuliah Dasar Pemrograman tentang Tipe Bentukan
#Pembuat: Cholid Machfudz(24060119140141) & Dzamar Maulana(24060119120033)
#Tanggal: 11 Desember 2022

#DEFINISI DAN SPESIFIKASI TYPE
#type pecahanc: <bil:integer, n: integer >=0 ,d: integer>0>
#   < bil:integer n:integer>=0, d:integer>0 > n adalah pembilang (numerator) dan d adalah penyebut (denumerator). Penyebut sebuah pecahan tidak boleh nol.

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#pecahanc:integer, integer>=0, integer>0 --> pecahan
#   pecahanc(bil,n,d) membentuk sebuah pecahan dari pembilang n dan penyebut d, dengan n dan d integer
#Realisasi dalam Python

# Mendifinisikan Tipe Pecahan Campuran
def pecahanc(bil,n,d):
    return [bil,n,d]

#DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI 
#bil: pecahan --> integer
#   bil(P) memberikan nilai bilangan dari pecahan campuraan tersebut
#Realisasi dalam Python
def bil(P):
    return P[0]

#Pemb: pecahan --> integer>0
#   Pemb(P) memberikan numerator pembilang n dari pecahan tersebut
#Realisasi dalam Python
def pemb(P):
    return P[1]

#Peny: pecahan --> integer>0
#   Peny(P) memberikan denumerator penyebut d dari pecahan tersebut
#Realisasi dalam Python
def peny(P):
    return P[2]  

#KonversiPecahan(P)
#Mengubah pecahan campuran ke pecahan biasa
def KonversiPecahan(P):
    if peny(P)==0:
        return("error")
    elif (bil==0):
        return(pemb(P),peny(P))
    else:
        pembb=(peny(P)*bil(P))+pemb(P)
        return(pembb,peny(P))

#Aplikasi
print(KonversiPecahan(pecahanc(1,1,2)))

#KonversiReal(P)
#Program pecahan ke desimal
def KonversiReal(P):
    if peny(P)==0:
        return("error")
    elif (bil==0):
        return(pemb(P)/peny(P))
    else:
        return((peny(P)*bil(P)+pemb(P))/peny(P))
#Aplikasi
print(KonversiReal(pecahanc(1,1,2)))

#AddP(P1,P2)
#menambah 2 pecahan campuran
def AddP(P1,P2):
    peny2=peny(P1)*peny(P2)
    return (bil(P1)+bil(P2),(peny2/peny(P1)*pemb(P1))+(peny2/peny(P2)*pemb(P2)),peny2)
#Aplikasi
print("\nAddP(P1,P2)")
print(AddP(pecahanc(1,1,2),pecahanc(1,2,3)))

#SubP(P1,P2)
#pengurangan peacahan campuran
def SubP(P1,P2):
    peny2=peny(P1)*peny(P2)
    return (bil(P1)+bil(P2),(peny2/peny(P1)*pemb(P1))-(peny2/peny(P2)*pemb(P2)),peny2)
#Aplikasi
print(SubP(pecahanc(1,1,2),pecahanc(1,2,3)))

#DivP(P1,P2)
#Pembagian pecahan campuran
def DivP(P1,P2):
   return((peny(P1)*bil(P1)+pemb(P1))*peny(P2),peny(P1)*(peny(P2)*bil(P2)+pemb(P2)))
#Aplikasi
print(DivP(pecahanc(1,1,2),pecahanc(1,1,2)))

#MulP(P1,P2)
#mengalikan pecahan campuran P1 dan P2
def MulP(P1,P2):
    return((peny(P1)*bil(P1)+pemb(P1))*(peny(P2)*bil(P2)+pemb(P2)),peny(P2)*peny(P1))
#Aplikasi
print(MulP(pecahanc(1,1,2),pecahanc(1,1,2)))

#IsEqP?(P1,P2)
#Membandingkan apakah P1 dan P2 sama
def IsEqP(P1,P2):
    if (P1==P2) or (peny(P1)%peny(P2)==0 and pemb(P1)%pemb(P2)==0) or (peny(P2)%peny(P1)==0 and pemb(P2)%pemb(P1)==0):
        return(True)
    else:
        return(False)
#Aplikasi
print("\nIsEqP?(P1,P2)")
print(IsEqP(pecahanc(1,1,2),pecahanc(1,1,2)))

#IsLtP?(P1,P2)
#Membandingkan apakah P1 lebih kecil dari P2
def IsLtP(P1,P2):
    PP1=(peny(P1)*bil(P1)+pemb(P1))/peny(P1)
    PP2=(peny(P2)*bil(P2)+pemb(P2))/peny(P2)
    if (PP1<PP2):
        return("P1 lebih kecil dari P2")
    else :
        return("False")
#Aplikasi
print("\nIsLtP?(P1,P2)")
print(IsLtP(pecahanc(1,1,2),pecahanc(1,2,4)))

#IsGtP?(P1,P2): 
# membandingkan apakah P1 lebih besar dari P2
def IsGtP(P1,P2):
    PP1=(peny(P1)*bil(P1)+pemb(P1))/peny(P1)
    PP2=(peny(P2)*bil(P2)+pemb(P2))/peny(P2)
    if (PP1>PP2):
        return("P1 lebih besar dari P2")
    else :
        return("False")
#Aplikasi
print(IsGtP(pecahanc(1,1,2),pecahanc(1,2,4)))


#-----------------------------------------------------------------------


#DEFINISI DAN SPESIFIKASI TANGGAL
#type tanggal: <D1: tanggal, D2: tanggal>
#   didalam D terdapat <hr,tgl,bln> dimana hr adalah hari, bln adalah bulan, dan thn adalah tahun.

# make_date, membuat tipe tanggal dengan 3 masukan.
def make_date(hr,bln,thn):
    return[hr,bln,thn]

# hr(D) menginisialisasi tipe tanggal hari
def hr(D):
    return D[0]

# bln(D) menginisialisasi tipe tanggal bulan
def bln(D):
    return D[1]

# thn(D) menginisialisasi tipe tanggal tahun
def thn(D):
    return D[2]

# mendefinisikan untuk bulan dengan jumlah hari 30, 31, dan 29
bsr=(1,3,5,7,8,10,12) #bln dengan jumlah hari 31
kcl=(4,6,9,11) #bln dengan jumlah hari 30
feb=(2) #bln februari dengan jumlah hari 28/29

# MEnentukan hari setelahnya
def NextDay(D):
    if hr(D)<=31 and bln(D)!=2:
        if (hr(D) < 30 and bln(D) in kcl) or (hr(D) < 31 and bln(D) in bsr):
            return (hr(D)+1,bln(D),thn(D))
        elif (hr(D) == 30 and bln(D) in kcl) or (hr(D) == 31 and bln(D) in bsr) and bln(D) != 12:
            return (1, bln(D)+1, thn(D))
        elif (hr(D) == 30 and bln(D) in bsr and bln(D) == 12) or (hr(D) == 31 and bln(D) in bsr and bln(D) == 12):
            return (1,1,thn(D)+1)
        else:
            return ("Masukkan salah")
    elif hr(D)<=29 and bln(D)==2:
        if (hr(D)<28) or (isKabisat(D) and hr(D)<29):
            return (hr(D)+1,bln(D),thn(D))
        elif (hr(D)==28) or (isKabisat(D) and hr(D)==29) and bln !=12:
            return (1,bln(D)+1,thn(D))
        elif (hr(D) == 28 and not isKabisat(D) and bln(D) == 12) or (hr(D) == 29 and isKabisat(D) and bln(D) in bsr and bln(D) == 12):
            return (1,1,thn(D)+1)
        else:
            return ("Masukkan salah")
    else:
        return("Masukkan salah")

# MEnentukan hari sebelumnya
def Yesterday(D):
    if hr(D)<=31 and bln(D)<=12:
        if hr(D) > 1:
            return (hr(D)-1,bln(D),thn(D))
        elif (hr(D) == 1 and bln(D) in kcl and bln(D)==8):
            return (31, bln(D)-1, thn(D))
        elif (hr(D) == 1 and bln(D) in bsr) and bln(D) != 1 and bln(D) != 3 and bln(D)!=8:
            return (30, bln(D)-1, thn(D))
        elif hr(D) == 1 and bln(D) == 1:
            return (31,12,thn(D)-1)
        else:
            return ("Masukkan salah")

    elif hr(D)==1 and bln(D)==3:
        if isKabisat(D):
            return (29,2,thn(D))
        if not isKabisat(D):
            return (28,2,thn(D))
        else:
            return ("Masukkan salah")
    else:
        return("Masukkan salah")

# Menentukan hari apakah kabisat
def isKabisat(D):
    return thn(D) % 400==0 or (thn(D) % 4==0 and thn(D) % 100>=1)

def IsEqD(D1,D2):
    if hr(D1)==hr(D2) and bln(D1) == bln(D2) and thn(D1)==thn(D2):
        return("Tanggal bernilai sama")
    else:
        return("Tanggal berbeda")

# Menentukan hari apakah D1 sebelum D2
def IsBefore(D1,D2):
    if thn(D1)<thn(D2):
        return True
    elif thn(D1)==thn(D2) and bln(D1)<bln(D2):
        return True
    elif thn(D1)==thn(D2) and bln(D1)==bln(D2) and hr(D1)<hr(D2):
        return True
    else:
        return False

# Menentukan hari apakah D1 lebih cepat D2
def IsAfter(D1,D2):
    if thn(D1)>thn(D2):
        return True
    elif thn(D1)==thn(D2) and bln(D1)>bln(D2):
        return True
    elif thn(D1)==thn(D2) and bln(D1)==bln(D2) and hr(D1)>hr(D2):
        return True
    else:
        return False



#---------------------------------------------------------------------------------------
def program():
    print("\n\n-----------------------------")
    print("Dibuat Oleh: \nCholid Mahfudz Zaelani (24060119140141)\nDzamar Maulana Ibrahim (24060119120033)")
    print("\n-----------------------------\n")
    pilih=int(input("Pilih Tipe Bentukan : \n1. Pecahan\n2. Tanggalan\nPilihan ?  "))
    if (pilih==1):
        print("\n-------------Program Pecahan\nMasukkan 2 pecahan sebagai inputan----------------")
        print("\nMasukkan Pecahan ke-1\n")
        bil1 = int(input("Masukan bilangan 1 : "))
        n1 = int(input("Masukkan Pembilang 1 : "))
        d1 = int(input("Masukkan Penyebut 1 : "))
        P1=[bil1,n1,d1]
        print("\nMasukkan Pecahan ke-2\n")
        bil2 = int(input("Masukan bilangan 2 : "))
        n2 = int(input("Masukkan Pembilang 2 : "))
        d2 = int(input("Masukkan Penyebut 2 : "))
        P2=[bil2,n2,d2]

        print("\nPecahan Biasa dari",P1,"adalah",KonversiPecahan(P1))
        print("\nPecahan Biasa dari",P2,"adalah",KonversiPecahan(P2))
        print("\nDesimal dari",P1,"adalah",KonversiReal(P1))
        print("\nDesimal dari",P2,"adalah",KonversiReal(P2))
        print("\nAdd dari",P1,"dan",P2,"adalah",AddP(P1,P2))
        print("\nSub dari",P1,"dan",P2,"adalah",SubP(P1,P2))
        print("\nDiv dari",P1,"dan",P2,"adalah",DivP(P1,P2))
        print("\nMul dari",P1,"dan",P2,"adalah",MulP(P1,P2))
        print("\nIsEqP?",P1,"dan",P2,"adalah",IsEqP(P1,P2))
        print("\nIsLtP?",P1,"dan",P2,"adalah",IsLtP(P1,P2))
        print("\nIsGtP?",P1,"dan",P2,"adalah",IsGtP(P1,P2))
        print("\n\n")

        x=str(input("Apakah ulang (y/n) ? "))
        if x=="Y" or x=="y":
            return(program())
        else :
            return("\n\nTerimakasih\n")

    elif (pilih==2):
        print("\n-------------Program Tanggalan\nMasukkan 2 tanggal sebagai inputan----------------")
        print("\nMasukkan Tanggal ke-1\n")
        hr1 = int(input("Masukan Tanggal : "))
        bln1 = int(input("Masukkan Bulan : "))
        thn1 = int(input("Masukkan Tahun : "))
        D1=[hr1,bln1,thn1]
        print("\nMasukkan Tanggal ke-2\n")
        hr2 = int(input("Masukan Tanggal : "))
        bln2 = int(input("Masukkan Bulan : "))
        thn2 = int(input("Masukkan Tahun : "))
        D2=[hr2,bln2,thn2]

        print("\nNextDay dari",D1,"adalah",NextDay(D1))
        print("\nNextDay dari",D2,"adalah",NextDay(D2))
        print ("\nYesterday dari",D1,"adalah",Yesterday(D1))
        print ("\nYesterday dari",D2,"adalah",Yesterday(D2))
        print ("\nApakah",D1,"merupakan Kabisat ? ",isKabisat(D1))
        print ("\nApakah",D2,"merupakan Kabisat ? ",isKabisat(D2))
        print ("\nApakah",D1,"dan",D2,"sama ? ",IsEqD(D1,D2))
        print ("\nApakah",D1,"lebih lambat dari",D2," ? ",IsBefore(D1,D2))
        print ("\nApakah",D1,"lebih cepat dari",D2," ? ",IsAfter(D1,D2))
        print("\n\n")

        x=str(input("Apakah ulang (y/n) ? "))
        if x=="Y" or x=="y":
            return(program())
        else :
            return("\n\nTerimakasih\n")



print(program())

    