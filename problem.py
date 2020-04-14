import sqlite3
con=sqlite3.connect("market1.db")
cursor=con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ürün(isim TEXT,fiyat INT,ortak TEXT)")
liste=[]
def ekle(isim,fiyat,ortak):
    cursor.execute("Insert into ürün Values(?,?,?)",(isim,fiyat,ortak))
    con.commit()
def sil(isim):
    cursor.execute("Delete From ürün where isim=?",(isim,))
    con.commit()
def gör():
    cursor.execute("Select * From ürün")
    data=cursor.fetchall()
    for i in data:
        print(list(i))
def ortaki(ortak):
    cursor.execute("Select * From ürün where ortak=?",(ortak,))
    data=cursor.fetchall()
    for i in data:
        print(i)
while True:
    işlem=input("İşlemi Seçin ==>")
    if(işlem=="q"):
        break
    elif(işlem=="1"):
        isim=input("İsim :")
        fiyat=int(input("Fiyat :"))
        ortak=input("Grup :")
        ekle(isim,fiyat,ortak)
    elif(işlem=="2"):
        isim=input("Silmek İstediğiniz Eşyanın İsimi")
        sil(isim)
    elif(işlem=="3"):
        gör()
    elif(işlem=="4"):
        ortak=input("Ortak Adı Giriniz ==>")
        ortaki(ortak)