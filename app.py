from flask import Flask,render_template,request,json,redirect,url_for
from database import Database

app = Flask(__name__)


#-----Anasayfa-----

@app.route("/")
def index():
    db = Database()
    duyuru=db.duyurulistele()
    etkinlik=db.etkinliklistele()
    return render_template("index.html",duyuru=duyuru,etkinlik=etkinlik)
    
@app.route("/admin")
def admin():
    db = Database()
    result=db.duyurulistele()
    return render_template("admin.html",result=result)


#--------Etkinlik----------

@app.route("/etkinlik")
def etkinlik():
    db = Database()
    result=db.etkinliklistele()
    return render_template("etkinlik.html",result=result)

@app.route('/etkinlikekleme',methods = ['POST'])
def  etkinlikekleme():
   if request.method == 'POST':
      db = Database()
      etkinlik_baslik = request.form['etkinlik_baslik']
      etkinlik_icerik = request.form['etkinlik_icerik']
      etkinlik_tarihi = request.form['etkinlik_tarihi']
      etkinlik_konum = request.form['etkinlik_konum']
      etkinlik_bilgisi = (etkinlik_baslik,etkinlik_icerik,etkinlik_tarihi,etkinlik_konum)
      db.etkinlikekle(etkinlik_bilgisi)
      return redirect('etkinlik')

@app.route('/etkinliksil/<int:numara>')
def etkinliksil(numara):
    db = Database()
    db.etkinliksil(numara)
    return redirect('/etkinlik')

@app.route('/etkinlikbilgileri/<int:numara>')
def etkinlikbilgileri(numara):
    db = Database()
    sonuc = db.etkinlikbilgileri(numara)
    return render_template("etkinlikduzenle.html",sonuc=sonuc)

@app.route("/etkinlikduzenle")    
def etkinlikduzenle():
    return render_template("etkinlikduzenle.html") 

@app.route('/etkinlikduzenleme',methods = ['POST'])
def  etkinlikduzenleme():
   if request.method == 'POST':
      db = Database()
      etkinlik_id = request.form['etkinlik_id']
      etkinlik_baslik = request.form['etkinlik_baslik']
      etkinlik_icerik = request.form['etkinlik_icerik']
      etkinlik_tarihi = request.form['etkinlik_tarihi']
      etkinlik_konum = request.form['etkinlik_konum']
      etkinlik_bilgisi = (etkinlik_baslik,etkinlik_icerik,etkinlik_tarihi,etkinlik_konum,etkinlik_id)
      db.etkinlikduzenle(etkinlik_bilgisi)
      return redirect('etkinlik')


#--------Duyuru-----------

@app.route('/duyuruekleme',methods = ['POST'])
def  duyuruekleme():
   if request.method == 'POST':
      db = Database()
      duyuru_icerik = request.form['duyuru_icerik']
      db.duyuruekle(duyuru_icerik)
      return redirect('admin')

@app.route('/duyurusil/<int:numara>')
def duyurusil(numara):
    db = Database()
    db.duyurusil(numara)
    return redirect('admin')


if __name__ == "__main__":
   app.run(debug = True)