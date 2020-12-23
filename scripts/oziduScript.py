import sys, os, time, schedule, datetime, sqlite3
from pygame import mixer
from gtts import gTTS

kok_dizin=os.path.dirname(os.getcwd())

con = sqlite3.connect(os.path.join(kok_dizin, 'zildata.sqlite3'))
cursorObj = con.cursor()
zilbasligi={0:"toplanma_saati",1:"ders_baslangic",2:"ogretmen_saat",3:"ders_bitis"}
zilturleri={}

def zilCal(mp3Yolu, anlikcalma=False):
    global zilturleri
    if anlikcalma:
        try:
            mixer.init()
            mixer.music.load(os.path.join(kok_dizin,"mp3file",mp3Yolu))
            mixer.music.play()
        except:
            print("MP3 dosyası bulunamadı!")       
        cursorObj.execute('UPDATE cal_duyur SET mp3yolu=NULL')
        con.commit()
    else:
        cursorObj.execute('SELECT zilaktif FROM cal_duyur')
        zil = cursorObj.fetchone()
        if bool(zil[4]):            
            simdi=datetime.datetime.now()
            zaman=simdi.strftime("%H:%M")
            cursorObj.execute('SELECT yol FROM melodipath WHERE melodiad="'+zilturleri[zaman][:3]+'"')
            yol = cursorObj.fetchone()
            try:
                if yol[0]==None:
                    dosyamp3="default.mp3"
                else:
                    dosyamp3=yol[0]
                mixer.init()
                mixer.music.load(os.path.join(kok_dizin,"mp3file",dosyamp3))
                mixer.music.play()
            except:
                print("MP3 dosyası bulunamadı!")       
            print(zaman,"zil çaldı.")

def duyuruYap(metin):
    try:        
        tts = gTTS(metin, lang="tr")
        tts.save("duyuru.mp3")       
        mixer.init()
        mixer.music.load("duyuru.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.1)
        mixer.music.stop()
        mixer.quit()
        os.remove("duyuru.mp3")
    except:  
        print("Google API'si devre dışı")
    finally:
        cursorObj.execute('UPDATE cal_duyur SET metin=NULL')
        con.commit()

def gunlukZilleriKur():
    global zilturleri
    t=datetime.datetime.now()
    gun=int(t.strftime("%w"))-1
    if gun==-1:
        gun=6

    cursorObj.execute('SELECT toplanma_saati,ders_baslangic,ogretmen_saat,ders_bitis FROM saat WHERE ders_gun='+str(gun))
    saatler = cursorObj.fetchall()   
    if saatler!=None:
        for s in saatler:
            for n in range(4):
                if s!=None and s[n]!="00:00:00":
                    zilturleri.update({s[n]: zilbasligi[n]})
                    schedule.every().day.at(s[n]).do(lambda: zilCal('default.mp3'))

    schedule.every().day.at("22:00").do(lambda: kapat())
    print(zilturleri)
    
def kapat():
    con.close()
    sys.exit()

#-------------ANA PROGRAM--------------
gunlukZilleriKur()
while True:
    schedule.run_pending()
    cursorObj.execute('SELECT * FROM cal_duyur')
    cal_duyur=cursorObj.fetchone()
    if cal_duyur[1]!=None:
        duyuruYap(cal_duyur[1])
    elif cal_duyur[2]!=None:
        zilCal(cal_duyur[2], True)
    elif cal_duyur[3]==1:
        schedule.clear()
        gunlukZilleriKur()
        cursorObj.execute('UPDATE cal_duyur SET guncellendi=0')
        con.commit()
    time.sleep(7)
