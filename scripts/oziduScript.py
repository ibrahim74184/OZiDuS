import datetime
import os
import schedule
import sqlite3
import sys
import time

from gtts import gTTS
from pygame import mixer

con = sqlite3.connect('../zildata.sqlite3')
cursorObj = con.cursor()


def zilCal(mp3Yolu, anlikcalma=False):
    global zilturleri
    if anlikcalma:
        try:
            mixer.init()
            mixer.music.load("../mp3file/"+mp3Yolu)
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
                mixer.music.load("../mp3file/"+dosyamp3)
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
    gun=t.strftime("%w")
    if gun==0:
        gun=7

    cursorObj.execute('SELECT * FROM saat WHERE gun_id='+gun)
    saatler = cursorObj.fetchone()
    if saatler!=None:
        zilturleri=dict(zip(list(saatler), [d[0] for d in cursorObj.description]))
        for s in saatler:
            if s!=None and s!=int(gun):
                schedule.every().day.at(s).do(lambda: zilCal('default.mp3'))

    schedule.every().day.at("22:00").do(lambda: kapat())


def kapat():
    con.close()
    sys.exit()

# -------------ANA PROGRAM--------------

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
