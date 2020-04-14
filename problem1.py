print("""
   Şarkı Ekleme Uygulaması ==>
   İŞLEMLER ==>
   ********************************
   1 Şarkı Ekle
   2 Şarkı Sil
   3 Toplam Şarkı Zamanını Öğren
   4 Bütün Şarkılarımı Gör
   5 Şirket Güncelle
   "q" ÇIKIŞ
   ********************************
   """)
import sqlite3
from functools import reduce
liste=[]
con=sqlite3.connect("kütüphane.db")
cursor=con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS müzikler(isim TEXT,sanatçı TEXT,albüm TEXT,company TEXT,süre INT)")
def ekle(isim,sanatçı,albüm,company,süre):
    cursor.execute("Insert into müzikler Values(?,?,?,?,?)",(isim,sanatçı,albüm,company,süre))
    con.commit()
def sil(sanatçı):
    cursor.execute("Delete From müzikler where sanatçı=?",(sanatçı,))
    con.commit()
def topla():
    cursor.execute("Select süre From müzikler")
    data=cursor.fetchall()
    print("Şarkı Süreleri")
    toplam=0
    for i in data:
        liste.append(sum(i))
    print(sum(liste))
def verilegör():
    cursor.execute("Select isim,sanatçı,albüm,company,süre From müzikler")
    data=cursor.fetchall()
    print("İsim Sanatçı Albüm Şirket Süre")
    for i in data:
        print(list(i))
def güncelle(şirket,deger):
    cursor.execute("Update müzikler set company=? where company=?",(deger,şirket))
    con.commit()

while True:
    işlem=input("İşlemi Seçin ==>")
    if(işlem=="q"):
        break
    elif(işlem=="1"):
        isim=input(("Müzik İsim ==>"))
        sanatçı=input("Sanatçı İsim ==>")
        albüm=input(("Albüm İsim ==>"))
        company=input("Şirket İsim ==>")
        süre=int(input("Şarkı Süresi ==>"))
        ekle(isim,sanatçı,albüm,company,süre)
        if(ekle):
            print("Başarıyla Eklendi...")
        else:
            print("Başarısız ...")
    elif(işlem=="2"):
        sanatçı=input("Silmek İstediğiniz Sanatcinin İsmi ==>")
        sil(sanatçı)
    elif(işlem=="3"):
        topla()
    elif(işlem=="4"):
        verilegör()
    elif(işlem=="5"):
        şirket=input("Şirket Adı ==>")
        deger=input("Yeni Şirket Adı ==>")
        güncelle(şirket,deger)







