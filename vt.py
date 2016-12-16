import sqlite3



vtDosya="plaka.db"
vtSayfa="aidatlar"
vtSutun=""" "plaka","aidat"  """



def kur():
    dosya=sqlite3.connect(vtDosya)
    imlec=dosya.cursor()
    try:
        imlec.execute("""create table {0} ({1})""".format(vtSayfa,vtSutun))
    except:
        pass
    dosya.commit()
    dosya.close()
kur()

def yaz(sutun):
    dosya=sqlite3.connect(vtDosya)
    imlec=dosya.cursor()
    imlec.execute("""insert into {0} values ({1}) """.format(vtSayfa,sutun))
    dosya.commit()
    dosya.close()

def sayfaAl():
        dosya=sqlite3.connect(vtDosya)
        imlec=dosya.cursor()
        imlec.execute("""select * from {} """.format(vtSayfa))
        data=imlec.fetchall()
        dosya.close()
        return data


plaka= input("Plaka >>> ")
aidat= input("Aidat >>> ")

yaz(sutun=""" "{}","{}" """.format(plaka,aidat))
