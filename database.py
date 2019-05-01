import pymysql

class Database:
    def __init__(self):
        host = #Host
        user = #Username
        password = #password
        db = #Database Name
        self.con = pymysql.connect(
            host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()


##########  Slider   ####################

    def sliderlistele(self):
        self.cur.execute("select * from slider")
        result = self.cur.fetchall()
        return result
    
    def sliderekle(self,slider_bilgisi):
        self.cur.execute(
            "INSERT INTO slider (slider_yolu) VALUES (%s)", slider_bilgisi)
        self.con.commit()

    def slidersil(self,id):
        self.cur.execute("delete from slider where slider_id=%s", id)
        self.con.commit()
        
   
##########  Duyuru   ####################

    def duyurulistele(self):
        self.cur.execute("select * from duyuru")
        result = self.cur.fetchall()
        return result

    def duyuruekle(self,duyuru_icerik):
        self.cur.execute(
            "INSERT INTO duyuru (duyuru_icerik) VALUES (%s)", duyuru_icerik)
        self.con.commit()

    def duyurusil(self,id):
        self.cur.execute("delete from duyuru where duyuru_id=%s", id)
        self.con.commit()

    def duyuruduzenle(self,data):
        self.cur.execute(
            "UPDATE duyuru SET duyuru_icerik=%s  WHERE duyuru_id=%s", data)
        self.con.commit()


##########  Etkinlik   ####################

    def etkinliklistele(self):
        self.cur.execute("select * from etkinlik")
        result = self.cur.fetchall()
        return result

    def etkinlikbilgileri(self, numara):
        self.cur.execute(
            "SELECT * FROM etkinlik WHERE etkinlik_id=%s", numara)
        result = self.cur.fetchone()
        return result

    def etkinlikekle(self,etkinlik_icerik):
        self.cur.execute(
            "INSERT INTO etkinlik (etkinlik_baslik,etkinlik_icerik,etkinlik_tarih,etkinlik_konum) VALUES (%s, %s, %s, %s)", etkinlik_icerik)
        self.con.commit()

    def etkinliksil(self,id):
        self.cur.execute("delete from etkinlik where etkinlik_id=%s", id)
        self.con.commit()

    def etkinlikduzenle(self,data):
        self.cur.execute(
            "UPDATE etkinlik SET etkinlik_baslik=%s, etkinlik_icerik=%s, etkinlik_tarih=%s , etkinlik_konum=%s  WHERE etkinlik_id=%s", data)
        self.con.commit()