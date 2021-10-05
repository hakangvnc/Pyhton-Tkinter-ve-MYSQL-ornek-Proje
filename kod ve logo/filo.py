from tkinter.ttk import*
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from PIL import Image, ImageTk
import time
import datetime
import random

vt = mysql.connector.connect(host="localhost",user="root",passwd="",database="hakanfilo")
yazi=("georgia",14)
yazi1=("arial",13)
ekran=Tk()
def giris():
    ekran.title("HKN.filo")
    ekran.geometry("850x800+250+0")

    #can=Canvas(ekran,width=800,height=600,background="white")
    #can.pack()

    resim1 = Image.open("logo1.png")
    yukle = ImageTk.PhotoImage(resim1)
    goruntu1 = Label(ekran, image=yukle)
    goruntu1.image = yukle
    goruntu1.place(x=200, y=0)

    yazi=("georgia",14)
    yazi1=("arial",13)
    def ekleme():
        global yazi
        global yazi1
        ekran1=Toplevel(ekran)
        ekran1.title("YENİ ARAÇ EKLEME")
        ekran1.geometry("600x600+260+10")
        konumx=60
        konumy=70
        l0=Label(ekran1,text="Yeni Araç Ekleme",fg="grey",font=("arial",18,"italic"))
        l0.place(x=konumx+150,y=konumy-50)

        l1=Label(ekran1,text="Araç plakasını giriniz :",font=(yazi))
        l1.place(x=konumx,y=konumy)
        e1=Entry(ekran1,text="plak",font=(yazi1),width=22)
        e1.place(x=konumx+300,y=konumy)

        l2=Label(ekran1,text="Araç türünü seçiniz :",font=(yazi))
        l2.place(x=konumx,y=konumy+40)
        liste_tur=["TIR","KAMYON","KAMYONET","OTOBUS","MİNİBUS","OTOMOBİL"]
        e2=ttk.Combobox(ekran1)
        e2['values']=liste_tur
        e2.config(font=(yazi1))
        e2.place(x=konumx+300,y=konumy+40)

        l3=Label(ekran1,text="Şase numarası giriniz :",font=(yazi))
        l3.place(x=konumx,y=konumy+80)
        e3=Entry(ekran1,text="sase",font=(yazi1),width=22)
        e3.place(x=konumx+300,y=konumy+80)

        l4=Label(ekran1,text="Araç markasını giriniz :",font=(yazi))
        l4.place(x=konumx,y=konumy+120)
        e4=Entry(ekran1,text="marka",font=(yazi1),width=22)
        e4.place(x=konumx+300,y=konumy+120)

        
        l5=Label(ekran1,text="Araç modelini giriniz :",font=(yazi))
        l5.place(x=konumx,y=konumy+160)
        e5=Entry(ekran1,text="model",font=(yazi1),width=22)
        e5.place(x=konumx+300,y=konumy+160)
        yakit=StringVar(value="Seçilmedi")
        l6=Label(ekran1,text="Araç yakıt türünü seçiniz :",font=yazi)
        l6.place(x=konumx,y=konumy+200)
        r1=Radiobutton(ekran1,text="BENZİN",variable=yakit,value="BENZİN",)
        r2=Radiobutton(ekran1,text="DİZEL",variable=yakit,value="MAZOT",)
        r1.place(x=konumx+320,y=konumy+200)
        r2.place(x=konumx+400,y=konumy+200)
        vites=StringVar(value="Seçilmedi")
        l7=Label(ekran1,text="Araç şanzıman tipini seçiniz :",font=yazi)
        l7.place(x=konumx,y=konumy+240)
        r3=Radiobutton(ekran1,text="MANUEL",variable=vites,value="MAMNUEL")
        r4=Radiobutton(ekran1,text="OTOMATİK",variable=vites,value="OTOMATİK")
        r3.place(x=konumx+320,y=konumy+240)
        r4.place(x=konumx+400,y=konumy+240)

        l8=Label(ekran1,text="Araç Üretim tarihini giriniz :",font=(yazi))
        l8.place(x=konumx,y=konumy+280)
        c1=Combobox(ekran1,width=4)
        c1['values'] = ("Gün", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", 
        "16", "17","18", "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
        c1.current(0)
        c1.config(font=yazi1)
        c1.place(x=konumx+300,y=konumy+280)
        c2 = Combobox(ekran1,width=4)
        c2['values'] = ("Ay" , "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        c2.current(0)
        c2.config(font=yazi1)
        c2.place(x=konumx+361,y=konumy+280)
        c3 = Combobox(ekran1,width=6)
        c3['values'] = ("Yıl","2020","2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007")
        c3.current(0)
        c3.config(font=yazi1)
        c3.place(x=konumx+422,y=konumy+280)
        #tarih birleştirme
        #ut_tarih=(c3.get()+"/"+c2.get()+"/"+c1.get())

        l9=Label(ekran1,text="Araç kilometre giriniz :",font=(yazi))
        l9.place(x=konumx,y=konumy+320)
        e6=Entry(ekran1,text="km",font=(yazi1),width=22)
        e6.place(x=konumx+300,y=konumy+320)
        durum=StringVar(value="Seçilmedi")  
        l10=Label(ekran1,text="Araç durumunu seçiniz",font=yazi)
        l10.place(x=konumx,y=konumy+360)
        r5=Radiobutton(ekran1,text="AKTİF",variable=durum,value="HAZIR")
        r6=Radiobutton(ekran1,text="PASİF",variable=durum,value="SERVİSDE")
        r5.place(x=konumx+320,y=konumy+360)
        r6.place(x=konumx+400,y=konumy+360)

        def kontrol():
            if(e1.get()=="" or e2.get()=="" or e3.get()=="" or e4.get()=="" or e5.get()=="" or yakit.get()=="Seçilmedi" or yakit.get()=="Seçilmedi" or c1.get()=="Gün" or c2.get()=="Ay" or c3.get()=="Yıl" or e6.get()=="" or durum.get()=="Seçilmedi"):
                uyarı=Label(ekran1,text="LÜTFEN BOŞ ALAN BIRAKMAYINIZ",font=yazi,fg="red")
                uyarı.place(x=konumx+80,y=konumy+400)
            else:
                ut_tarih=(c3.get()+"/"+c2.get()+"/"+c1.get())
                print(e1.get())
                print(e2.get())
                print(e3.get())
                print(e4.get())
                print(e5.get())
                print(yakit.get())
                print(vites.get())
                print(ut_tarih)
                print(e6.get())
                print(durum.get())
                mycursor=vt.cursor()
                sorgu1 = "INSERT INTO tum_araclar (arac_plaka,arac_tur,arac_sase,arac_marka,arac_model,arac_yakit,arac_vites,arac_uretim,arac_km,arac_durum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                deger1 = (e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),yakit.get(),vites.get(),ut_tarih,e6.get(),durum.get())
                mycursor.execute(sorgu1, deger1)
                vt.commit()
                messagebox.showinfo("BİLGİLENDİRME","KAYIT BAŞARILI BİR ŞEKİLDE GERÇEKLEŞTİRİLDİ")
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                ekran1.destroy()

        b1=Button(ekran1,text="KAYDET",command=kontrol,bg="grey",fg="white",font=yazi)
        b1.place(x=konumx+150,y=konumy+440,width=200,height=40)

    def kiralama():
        global yazi
        global yazi1
        ekran1=Toplevel(ekran)
        ekran1.title("ARAÇ KİRALAMA")
        ekran1.geometry("600x600+260+10")
        tablo1=Treeview(ekran1,selectmode="extended")
        tablo1.config(height=23)
        scrol=ttk.Scrollbar(ekran1,orient="vertical",command=tablo1.yview)
        scrol.place(x=585,y=5,height=480)
        tablo1.configure(yscrollcommand=scrol.set)

        tablo1["columns"] = ("plaka","Marka", "Model", "Yakıt Türü", "Şanzıman", "FİYAT")
        tablo1.column("#0",width=0,anchor='sw',stretch=tk.NO)
        tablo1.column("#1",width=100,anchor='sw')
        tablo1.column("#2",width=100,anchor='sw')
        tablo1.column("#3",width=100,anchor='sw')
        tablo1.column("#4",width=100,anchor='sw')
        tablo1.column("#5",width=100,anchor='sw')
        tablo1.column("#6",width=100,anchor='sw')

        tablo1.heading("#1", text="Plaka",anchor='sw')
        tablo1.heading("#2", text="Marka",anchor='sw')
        tablo1.heading("#3", text="Model",anchor='sw')
        tablo1.heading("#4", text="Yakıt Türü",anchor='sw')
        tablo1.heading("#5", text="Şanzıman",anchor='sw')
        tablo1.heading("#6", text="FİYAT",anchor='sw')
        def secilen_satır(deger):
            deger=tablo1.item(tablo1.selection())['values'][0]
            e22.delete(0,END)
            e22.insert(0,deger)
            return deger
        tablo1.bind('<ButtonRelease-1>',secilen_satır)
        tablo1.place(x=0,y=0)
        def tabloveri():
            mycursor=vt.cursor()
            sorgu2="select arac_plaka,arac_marka,arac_model,arac_yakit,arac_vites,arac_ucretleri.fiyatlar from tum_araclar  right join arac_ucretleri on tum_araclar.arac_tur=arac_ucretleri.arac_tur WHERE arac_durum='HAZIR'"
            mycursor.execute(sorgu2)
            sonuc2=mycursor.fetchall()
            for satir in range(len(sonuc2)):
                for sutun in range(1):
                    tablo1.insert("", 0,values=(sonuc2[satir]))
            vt.commit()
        tabloveri()

        def kiralama2():
            global yazi
            global yazi1
            ekran1=Toplevel(ekran)
            ekran1.title("ARAÇ KİRALAMA")
            ekran1.geometry("600x600+260+10")
            konumx=50
            konumy=70
            l20=Label(ekran1,text="İşlem yapılan araç :",font=yazi)
            l21=Label(ekran1,text=e22.get(),font=("impact",16,"italic"),fg="red")
            l20.place(x=konumx, y=(konumy-40))
            l21.place(x=konumx+300, y=(konumy-38))
            l9=Label(ekran1,text="TC kimlik numarası :",font=(yazi))
            l9.place(x=konumx, y=(konumy))
            e9=Entry(ekran1,font=(yazi1))
            e9.place(x=konumx+240, y=(konumy+5),width=230)
            l10=Label(ekran1,text="Ad :",font=(yazi))
            l10.place(x=konumx, y=(konumy+40))
            e10=Entry(ekran1,text="ad",font=yazi1)
            e10.place(x=konumx+240, y=(konumy+45),width=230)
            l11=Label(ekran1,text= "Soyad :",font=(yazi))
            l11.place(x=konumx, y=(konumy+80))
            e11=Entry(ekran1,text="soyad",font=(yazi1))
            e11.place(x=konumx+240, y=(konumy+85),width=230)
            l12=Label(ekran1,text="Telefon numarası :",font=(yazi))
            l12.place(x=konumx, y=(konumy+120))
            e12=Entry(ekran1,text="tel",font=(yazi1))
            e12.place(x=konumx+240, y=(konumy+125),width=230)
            l13=Label(ekran1,text="E-posta adresi :",font=(yazi))
            l13.place(x=konumx, y=(konumy+160))
            e13=Entry(ekran1,text="posta",font=(yazi1))
            e13.place(x=konumx+240, y=(konumy+165),width=230)
            l14=Label(ekran1,text="dogum tarihi :",font=(yazi))
            l14.place(x=konumx,y=(konumy+200))
            c4=Combobox(ekran1,width=4)
            c4['values'] = ("Gün", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13","14","15","16","17",
            "18","19","20","21","22","23","24","25","26","27","28","29","30","31")
            c4.current(0)
            c4.config(font=yazi1)
            c4.place(x=konumx+240, y=(konumy+205))
            c5 = Combobox(ekran1,width=4)
            c5['values'] = ("Ay" , "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
            c5.current(0)
            c5.config(font=yazi1)
            c5.place(x=konumx+310, y=(konumy+205))
            c6 = Combobox(ekran1,width=6)
            c6['values'] = ("Yıl","2020","2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
            "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993",
            "1992", "1991", "1990", "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981", "1980", "1979",
            "1978", "1977", "1976", "1975", "1974", "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966", "1965",
            "1964", "1933", "1962", "1961", "1960", "1959", "1958", "1957", "1956", "1954", "1953", "1952", "1951", "1950")
            c6.current(0)
            c6.config(font=yazi1)
            c6.place(x=konumx+380, y=(konumy+205))

            l15=Label(ekran1,text="Araç geri teslim tarihi :",font=(yazi))
            l15.place(x=konumx,y=(konumy+240))
            c7=Combobox(ekran1,width=4)
            c7['values'] = ("Gün", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13","14","15","16","17",
            "18","19","20","21","22","23","24","25","26","27","28","29","30","31")
            c7.current(0)
            c7.config(font=yazi1)
            c7.place(x=konumx+240, y=(konumy+245))
            c8 = Combobox(ekran1,width=4)
            c8['values'] = ("Ay" , "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
            c8.current(0)
            c8.config(font=yazi1)
            c8.place(x=konumx+310, y=(konumy+245))
            c9 = Combobox(ekran1,width=6)
            c9['values'] = ("Yıl","2020","2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030")
            c9.current(0)
            c9.config(font=yazi1)
            c9.place(x=konumx+380, y=(konumy+245))
            l16=Label(ekran1,text="Araç kilometre izni:",font=(yazi))
            l16.place(x=konumx, y=(konumy+280))
            e16=Entry(ekran1,text="kmizin",font=(yazi1))
            e16.place(x=konumx+240, y=(konumy+285),width=230)
            degisken=IntVar()
            l17=Checkbutton(ekran1,variable=degisken,onvalue=1,text="Kiralama sözleşmesini, aşılan her kilometre için 1 tl tutarı ödeyeceğimi\n ve araç hasar alması durumunda servisden cıkan karara göre masrafları\n kaşılamayı kabul ediyorum")
            l17.config(font=("georgia",10),width=60,activeforeground="red")
            l17.place(x=konumx,y=konumy+320)
            kutu3=Canvas(ekran1,width=180,height=50,bg="grey")
            kutu3.place(x=konumx+40,y=konumy+400)
            l18=Label(ekran1,text="TUTAR :",font=yazi2,bg="grey")
            mycursor=vt.cursor()
            sorgu5="select fiyatlar from arac_ucretleri where arac_tur=(select arac_tur from tum_araclar where arac_plaka=%s)"
            deger5=(e22.get(),)
            mycursor.execute(sorgu5,deger5)
            sonucab=mycursor.fetchone()
            sorgu9="select arac_plaka,arac_km from tum_araclar where arac_plaka=%s"
            deger9=(e22.get(),)
            mycursor.execute(sorgu9,deger9)
            sonucat=mycursor.fetchone()
            tutar=sonucab[0],"TL"
            l19=Label(ekran1,text=tutar,font=("impact",13),bg="grey",fg="red")
            l18.place(x=konumx+60,y=konumy+405)
            l19.place(x=konumx+130,y=konumy+403)
            def hesaplama():
                l19["text"]=""
                if(c7.get()=="Gün" or c8.get()=="Ay" or c9.get()=="Yıl"):
                    messagebox.showerror("UYARI","LÜTFEN BOŞ ALAN BIRAKMAYINIZ")
                else:
                    tarih1=datetime.datetime.today()
                    yil2=int(c9.get())
                    ay2=int(c8.get())
                    gun2=int(c7.get())
                    tarih2=datetime.datetime(year=yil2, month=ay2,day=gun2)
                    gunsayi=tarih2-tarih1
                    songun=gunsayi.days
                    songun=int(songun)+1
                    if(tarih2>=tarih1):
                        if(e16.get()==""):
                            otoizin=int(songun)*200
                            e16.insert(0,otoizin)
                        if(songun*200<int(e16.get())):
                            tutar=(1/2*(int(e16.get())-(int(songun)*200)))+(songun*int(sonucab[0]))
                        else:
                            tutar=(songun*int(sonucab[0]))
                    else:
                        messagebox.showinfo("UYARI","LÜTFEN ESKİ BİR TARİH SEÇMEYİNİZ")

                l19["text"]=float(tutar),"TL"
            def sozlesmekontrol():
                tarih1=datetime.datetime.today()
                yil2=int(c9.get())
                ay2=int(c8.get())
                gun2=int(c7.get())
                tarih2=datetime.datetime(year=yil2, month=ay2,day=gun2)
                gunsayi=tarih2-tarih1
                songun=gunsayi.days
                songun=int(songun)+1
                if(tarih2>=tarih1):
                    if(songun*200<int(e16.get())):
                        tutar=(1/2*(int(e16.get())-int(songun)*200))+(songun*int(sonucab[0]))
                    else:
                        tutar=(songun*int(sonucab[0]))
                if(e9.get()!="" or e10.get()!="" or e11.get()!="" or e12.get()!="" or e13.get()!="" or c4.get()!="Gün" or c5.get()!="Ay" or c6.get()!="Yıl"):
                    if(degisken.get()==1):
                        dog_tar=(c6.get()+"/"+c5.get()+"/"+c4.get())
                        tes_tar=(c9.get()+"/"+c8.get()+"/"+c7.get())
                        sorgu6="insert into musteriler (uye_tc,uye_ad,uye_soyad,uye_tel,uye_mail,uye_dogum) values (%s,%s,%s,%s,%s,%s)"
                        deger6=(e9.get(),e10.get(),e11.get(),e12.get(),e13.get(),dog_tar,)
                        mycursor.execute(sorgu6,deger6)

                        sorgu8="insert into kiralama_kayitlari (üye_tc, plan_teslim_tar, arac_izin_km, arac_plaka, arac_km, arac_tutar) values (%s,%s,%s,%s,%s,%s)"
                        deger8=(e9.get(),tes_tar,e16.get(),sonucat[0],sonucat[1],tutar,)
                        mycursor.execute(sorgu8,deger8)

                        sorgu10="update tum_araclar set arac_durum='KİRADA' where arac_plaka=%s"
                        deger10=(sonucat[0],)
                        mycursor.execute(sorgu10,deger10)

                        vt.commit()
                        messagebox.showinfo("BİLGİLENDİRME","İŞLEM BAŞARI İLE GERÇEKLEŞTİRİLDİ")
                        e9.delete(0,END)
                        e10.delete(0,END)
                        e11.delete(0,END)
                        e12.delete(0,END)
                        e13.delete(0,END)
                        e16.delete(0,END)
                        ekran1.destroy()
                    else:
                        messagebox.showerror("UYARI","LÜTFEN SÖZLEŞMEYİ KABUL EDİNİZ")
                else:
                    messagebox.showerror("UYARI","LÜTFEN BOŞ ALAN BIRAKMAYINIZ")
            b19=Button(ekran1,text="Hesapla",bg="grey",fg="white",font=yazi2,command=hesaplama)
            b19.place(x=konumx+80, y=(konumy+432),width=100,height=20)
            b2=Button(ekran1,text="KİRALA",bg="grey",fg="white",font=yazi2,command=sozlesmekontrol)
            b2.place(x=konumx+250, y=(konumy+402),width=200,height=50)


        def kontrol():
            if(e22.get()==""):
                messagebox.showerror("UYARI","PLAKA GİRMEDİNİZ")
            else:
                def sorgu3():
                    mycursor=vt.cursor()
                    sorgu3 = "select arac_plaka FROM tum_araclar where arac_plaka=%s and arac_durum='HAZIR'"
                    deger3=(e22.get(),)
                    mycursor.execute(sorgu3, deger3)
                    sonuc=mycursor.fetchone()
                    if(sonuc[0]!=e22.get()):
                        messagebox.showerror("UYARI","ARAÇ VERİTABANINDA  BULUNAMADI")
                        e22.delete(0,END)
                    elif(sonuc[0]==e22.get()):
                        kiralama2()
                        e22.delete(0,END)
                        ekran1.destroy()
                sorgu3()
                    
        l22=Label(ekran1,text="ARAÇ PLAKASI GİRİNİZ  :",font=("georgia",11))
        e22=Entry(ekran1,text="p",font=("impact",12),fg="red")
        b3=Button(ekran1,text="DEVAM ET",font=("georgia",11),command=kontrol,bg="grey",fg="white")
        l22.place(x=80,y=500)
        e22.place(x=290,y=500)
        b3.place(x=250,y=550)
    def teslim():
        ekran1=Toplevel(ekran)
        ekran1.title("ARAÇ TESLİM ALMA")
        ekran1.geometry("600x400+250+0")
        global yazi
        global yazi1
        konumx=50
        konumy=70
        la1=Label(ekran1,text="",font=yazi,fg="red")
        la1.place(x=konumx+120,y=konumy+250)
        def kmkontrol():
            mycursor=vt.cursor()
            sorgu11="select arac_km,arac_izin_km from kiralama_kayitlari where arac_plaka=%s and üye_tc=%s and arac_teslim_km=0 "
            deger11=(e24.get(),e23.get(),)
            mycursor.execute(sorgu11,deger11)
            sonuc11=mycursor.fetchone()
            if(mycursor.rowcount==1):
                izinkm=(int(sonuc11[0])+int(sonuc11[1]))
                if(izinkm<int(e25.get())):
                    asim="KM sınırınızı "+str(int(e25.get())-izinkm)+" km aşmışsınız."
                else:
                    asim="Km sınırınızı aşmamışsınız."
                la1["text"]=asim
            else:
                messagebox.showerror("UYARI","Kayıt bulunamadı. lütfen tekrar deneyiniz!")
        def teslim1():
            mycursor=vt.cursor()
            sorgu12="select arac_km,arac_izin_km,kayit_id from kiralama_kayitlari where arac_plaka=%s and üye_tc=%s and arac_teslim_km=0"
            deger12=(e24.get(),e23.get(),)
            mycursor.execute(sorgu12,deger12)
            sonuc12=mycursor.fetchone()
            if(mycursor.rowcount==1):
                izinkm=(int(sonuc12[0])+int(sonuc12[1]))
                if(izinkm<int(e25.get())):
                    asim=int(e25.get())-izinkm
                    mycursor=vt.cursor()
                    tarih=time.strftime("%Y-%m-%d %H:%M:%S")
                    servis_id_atama=random.randrange(1,21)
                    print(tarih)
                    sorgu13="update kiralama_kayitlari set km_ceza_tutar=%s,teslim_alınan_tar=%s,arac_teslim_km=%s  where kayit_id=%s "
                    deger13=(asim,tarih,e25.get(),sonuc12[2],)
                    mycursor.execute(sorgu13,deger13)

                    sorgu140="INSERT INTO servis_kayitlari(arac_plaka, hasar_id, arac_masraf) VALUES (%s,%s,'ÖDENMEDİ')"
                    deger140=(e24.get(),servis_id_atama,)
                    mycursor.execute(sorgu140,deger140)

                    sorgu15="update tum_araclar set arac_km=%s,arac_durum='SERVİSDE' where arac_plaka=%s"
                    deger15=(e25.get(),e24.get(),)
                    mycursor.execute(sorgu15,deger15)
                    vt.commit()

                    messagebox.showinfo("TESLİM","ARACINIZ TESLİM ALINDI")
                    ekran1.destroy()
                else:
                    tarih=time.strftime("%Y-%m-%d %H:%M:%S")
                    servis_id_atama=random.randrange(1,21)
                    print(tarih)
                    mycursor=vt.cursor()
                    sorgu13="update kiralama_kayitlari set teslim_alınan_tar=%s,arac_teslim_km=%s  where kayit_id=%s "
                    deger13=(tarih,e25.get(),sonuc12[2],)
                    mycursor.execute(sorgu13,deger13)

                    sorgu140="INSERT INTO servis_kayitlari(arac_plaka, hasar_id, arac_masraf) VALUES (%s,%s,'ÖDENMEDİ')"
                    deger140=(e24.get(),servis_id_atama,)
                    mycursor.execute(sorgu140,deger140)

                    sorgu15="update tum_araclar set arac_km=%s,arac_durum='SERVİSDE' where arac_plaka=%s"
                    deger15=(e25.get(),e24.get(),)
                    mycursor.execute(sorgu15,deger15)
                    vt.commit()
                    messagebox.showinfo("TESLİM","ARACINIZ TESLİM ALINDI")
                    e23.delete(0,END)
                    e24.delete(0,END)
                    e25.delete(0,END)
                    ekran1.destroy()
            else:
                messagebox.showerror("UYARI","Kayıt bulunamadı.Araç teslim alınmıs olabilir kiralama kayıtları menüsünden kontrol edebilirsiniz")
        l22=Label(ekran1,text="Araç Teslim Alma",font=("arial",20,"italic"),fg="grey")
        l22.place(x=konumx+130, y=(konumy-60))
        l23=Label(ekran1,text= "Müşteri TC no :",font=(yazi))
        l23.place(x=konumx, y=(konumy))
        e23=Entry(ekran1,font=(yazi1))
        e23.place(x=konumx+240, y=(konumy+5),width=230)
        l24=Label(ekran1,text="Araç plaka :",font=(yazi))
        l24.place(x=konumx, y=(konumy+40))
        e24=Entry(ekran1,text="plaka",font=(yazi1))
        e24.place(x=konumx+240, y=(konumy+45),width=230)
        l25=Label(ekran1,text="Araç kilometre :",font=(yazi))
        l25.place(x=konumx, y=(konumy+80))
        e25=Entry(ekran1,text="akm",font=(yazi1))
        e25.place(x=konumx+240, y=(konumy+85),width=230)
        b4=Button(ekran1,text="KM kontrol",bg="grey",fg="white",font=yazi2,command=kmkontrol)
        b5=Button(ekran1,text="Teslim Al",bg="grey",fg="white",font=yazi2,command=teslim1)
        b4.place(x=konumx+20,y=konumy+160,width=200,height=50)
        b5.place(x=konumx+260,y=konumy+160,width=200,height=50)
    def servis():
        ekran1=Toplevel(ekran)
        ekran1.title("SERVİS")
        ekran1.geometry("600x550+250+0")
        konumx=50
        konumy=50
        l26=Label(ekran1,text="Serviteki Araçlar",font=("arial",20,"italic"),fg="grey")
        l26.place(x=konumx+140,y=konumy-50)
        tablo2=Treeview(ekran1)
        tablo2.config(height=15)
        scrol2=ttk.Scrollbar(ekran1,orient="vertical",command=tablo2.yview)
        scrol2.place(x=553,y=40,height=325)
        tablo2.configure(yscrollcommand=scrol2.set)

        tablo2["columns"] = ("plaka","hasar", "masraf")
        tablo2.column("#0",width=0,anchor='sw')
        tablo2.column("plaka",width=100,anchor='sw')
        tablo2.column("hasar",width=300,anchor='sw')
        tablo2.column("masraf",width=100,anchor='sw')

        tablo2.heading("plaka", text="Plaka",anchor='sw')
        tablo2.heading("hasar", text="Hasar Açıklama",anchor='sw')
        tablo2.heading("masraf", text="Tutar",anchor='sw')
        tablo2.place(x=konumx,y=konumy-10)

        mycursor=vt.cursor()
        sorgu20="SELECT servis_kayitlari.arac_plaka,s_rapor,s_tutar from servis_kayitlari RIGHT JOIN masraflar on masraflar.s_id=servis_kayitlari.hasar_id where arac_plaka IN(select arac_plaka from tum_araclar where arac_durum='SERVİSDE')and arac_masraf='ÖDENMEDİ'"
        mycursor.execute(sorgu20)
        sonuc20=mycursor.fetchall()
        for satir in range(len(sonuc20)):
            for sutun in range(1):
                tablo2.insert("", 0,values=(sonuc20[satir]))
        vt.commit()

        l27=Label(ekran1,text="Toplam Tutar :",font=yazi)
        l27.place(x=konumx+60,y=konumy+350)
        can2=Canvas(ekran1,width=100,height=30)
        can2.config(bg="grey")
        can2.place(x=konumx+300,y=konumy+350)
        l28=Label(ekran1,text="TL",font=("impact",14),bg="grey",fg="red")
        l28.place(x=konumx+360,y=konumy+353)
        tumsec=IntVar()
        def tumsecfonk():
            if(tumsec.get()==1):
                mycursor=vt.cursor()
                sorgu23="SELECT sum(s_tutar) from masraflar where s_id in(SELECT hasar_id from servis_kayitlari WHERE arac_plaka in (select arac_plaka from tum_araclar where arac_durum='SERVİSDE') and arac_masraf='ÖDENMEDİ')"
                mycursor.execute(sorgu23)
                sonuc23=mycursor.fetchone()
                vt.commit()
                l28=Label(ekran1,text=sonuc23,font=("impact",13),bg="grey",fg="red")
                l28.place(x=konumx+320,y=konumy+355)
            else:
                pass
        def secilen_satır(deger):
            if(tumsec.get()!=1):
                deger=tablo2.item(tablo2.selection())['values'][2]
                l28=Label(ekran1,text=deger,font=("impact",13),bg="grey",fg="red")
                l28.place(x=konumx+320,y=konumy+355)
            else:
                pass

        tablo2.bind('<ButtonRelease-1>',secilen_satır)
        c30=Checkbutton(ekran1,variable=tumsec,onvalue=1,text="Tümünü seç",command=tumsecfonk)
        c30.config(font=("georgia",14),width=42,activeforeground="red")
        c30.place(x=konumx+200,y=konumy+320)

        onaylama=IntVar()
        l29=Checkbutton(ekran1,variable=onaylama,onvalue=1,text="Ödemeyi onaylıyorum")
        l29.config(font=("georgia",14),width=42,activeforeground="red")

        l29.place(x=konumx,y=konumy+390)
        def kayıt():
            if(onaylama.get()==1):
                if(tumsec.get()==1):
                    mycursor=vt.cursor()
                    sorgu24="update tum_araclar set arac_durum='HAZIR' where arac_durum='SERVİSDE'"
                    mycursor.execute(sorgu24)
                    sorgu25="update servis_kayitlari set arac_masraf='ÖDENDİ' WHERE arac_masraf='ÖDENMEDİ'"
                    mycursor.execute(sorgu25)
                    vt.commit()
                    messagebox.showinfo("BİLGİLENDİRME","İŞLEM BARŞARILI")
                    ekran1.destroy()
                else:
                    mycursor=vt.cursor()
                    sorgu25="update tum_araclar set arac_durum='HAZIR' where arac_plaka=%s"
                    deger25=(tablo2.item(tablo2.selection())['values'][0],)
                    mycursor.execute(sorgu25,deger25)
                    sorgu26="update servis_kayitlari set arac_masraf='ÖDENDİ' WHERE arac_plaka=%s"
                    deger26=(tablo2.item(tablo2.selection())['values'][0],)
                    mycursor.execute(sorgu26,deger26)
                    vt.commit()
                    messagebox.showinfo("BİLGİLENDİRME","İŞLEM BARŞARILI")
                    ekran1.destroy()
            else:
                messagebox.showinfo("UYARI","Lütfen Ödemeyi Onaylayınız")
        b6=Button(ekran1,text="TAMİR ET",bg="grey",fg="white",font=yazi2,command=kayıt)
        b6.place(x=konumx+150,y=konumy+430,width=200,height=40)

    def arac_durum():
        ekran1=Toplevel(ekran)
        ekran1.title("ARAÇ DURUM KONTROL")
        ekran1.geometry("600x400+250+0")
        konumx=50
        konumy=50
        l30=Label(ekran1,text="Araç Durum Kontrol",font=("arial",20,"italic"),fg="grey")
        l30.place(x=konumx+120,y=konumy-40)
        l31=Label(ekran1,text="Kontrol etmek isteginiz aracın\nplakasını giriniz",font=yazi)
        l31.place(x=konumx+110,y=konumy+10)
        e31=Entry(ekran1,text="plaka",font=("impact",14))
        e31.place(x=konumx+150, y=(konumy+80))
        l32=Label(ekran1,text="",font=yazi)
        l32.place(x=konumx+20,y=konumy+180)
        def kontrol2():
            mycursor=vt.cursor()
            sorgu26="select arac_durum,arac_plaka from tum_araclar where arac_plaka=%s"
            deger26=(e31.get(),)
            mycursor.execute(sorgu26,deger26)
            sonuc26=mycursor.fetchone()
            plaka=str(sonuc26[1])
            if(mycursor.rowcount==1):
                if(sonuc26[0]=="HAZIR"):
                    durum=plaka+"\n\n Plakalı aracınız kiralanmaya hazır durumdadır"
                    l32.place(x=konumx+40,y=konumy+180)
                elif(sonuc26[0]=="KİRADA"):
                    sorgu27="select plan_teslim_tar from kiralama_kayitlari where arac_plaka=%s ORDER BY kayit_id DESC LIMIT 1"
                    deger27=(e31.get(),)
                    mycursor.execute(sorgu27,deger27)
                    sonuc27=mycursor.fetchone()
                    durum=plaka+" Plakalı aracınız kiradadır \n\n"+str(sonuc27[0])+" Tarihinde teslim alınacaktır."
                    l32.place(x=konumx+80,y=konumy+180)
                elif(sonuc26[0]=="SERVİSDE"):
                    sorgu28="select s_rapor from masraflar where s_id=(select servis_id from kiralama_kayitlari where arac_plaka=%s ORDER BY kayit_id DESC LIMIT 1)"
                    deger28=(e31.get(),)
                    mycursor.execute(sorgu28,deger28)
                    sonuc28=mycursor.fetchone()
                    durum=plaka+" Plakalı aracınız servisdedir \n\n  Aracınızda "+str(sonuc28[0])+" yapılmıstır \n\n Servis bölümünden aracınızı hazır hale getirebilirsiniz"
                    l32.place(x=konumx+20,y=konumy+180)
            else:
                durum="Veri tabanında bu plakada herhangi bir arac bulunamadı.\n Lütfen plakayı kontrol ediniz"
            l32["text"]=durum
            vt.commit()
        b7=Button(ekran1,text="Kontrol Et",bg="grey",fg="white",font=yazi2,command=kontrol2)
        b7.place(x=konumx+150,y=konumy+120,width=200,height=40)

    def ucretler():
        ekran1=Toplevel(ekran)
        ekran1.title("KİRALAMA ÜCRETLERİ DÜZENLEME")
        ekran1.geometry("600x600+250+0")
        konumx=50
        konumy=50
        can3=Canvas(ekran1,width=600,height=600)
        can3.config()
        can3.place(x=0,y=0)
        l34=Label(ekran1,text="Kira Ücretleri Düzenleme",font=("arial",20,"italic"),fg="grey")
        l34.place(x=konumx+100,y=konumy-45)
        can3.create_rectangle(50,45,550,105,fill="grey",outline="white")
        bas1=Label(ekran1,text="ARAÇ TÜRLERİ",font=("georgia",16,"italic"),fg="black",bg="grey")
        bas2=Label(ekran1,text="GÜNCEL\nFİYATLAR",font=("georgia",14,"italic"),fg="black",bg="grey")
        bas3=Label(ekran1,text="YENİ\nFİYAT",font=("georgia",14,"italic"),fg="black",bg="grey")
        bas1.place(x=75,y=60)
        bas2.place(x=285,y=50)
        bas3.place(x=445,y=50)
        x3,y3,x4,y4=410,60,550,100
        for x in range(0,2):
            if(x==1):
                x3,y3,x4,y4=260,60,400,100
            for y in range(0,6):
                y3+=60
                y4+=60
                can3.create_rectangle(x3,y3,x4,y4,fill="grey",outline="grey")
        x1,y1,x2,y2=50,60,250,100
        for i in range(0,6):
            y1+=60
            y2+=60
            can3.create_rectangle(x1,y1,x2,y2,fill="grey",outline="grey")
        l35=Label(ekran1,text="OTOMOBİL",fg="white",font=yazi,bg="grey")
        l36=Label(ekran1,text="MİNİBÜS",fg="white",font=yazi,bg="grey")
        l37=Label(ekran1,text="OTOBÜS",fg="white",font=yazi,bg="grey")
        l38=Label(ekran1,text="KAMYONET",fg="white",font=yazi,bg="grey")
        l39=Label(ekran1,text="KAMYON",fg="white",font=yazi,bg="grey")
        l40=Label(ekran1,text="TIR",fg="white",font=yazi,bg="grey")
        l35.place(x=90,y=125)
        l36.place(x=100,y=185)
        l37.place(x=103,y=245)
        l38.place(x=90,y=305)
        l39.place(x=103,y=365)
        l40.place(x=130,y=425)

        mycursor=vt.cursor()
        fsorgu="select fiyatlar from arac_ucretleri order by tur_id asc"
        mycursor.execute(fsorgu)
        f2sorgu=mycursor.fetchall()
        l41=Label(ekran1,text=f2sorgu[0],fg="lightblue",font=("impact",19),bg="grey")
        l42=Label(ekran1,text=f2sorgu[1],fg="lightblue",font=("impact",19),bg="grey")
        l43=Label(ekran1,text=f2sorgu[2],fg="lightblue",font=("impact",19),bg="grey")
        l44=Label(ekran1,text=f2sorgu[3],fg="lightblue",font=("impact",19),bg="grey")
        l45=Label(ekran1,text=f2sorgu[4],fg="lightblue",font=("impact",19),bg="grey")
        l46=Label(ekran1,text=f2sorgu[5],fg="lightblue",font=("impact",19),bg="grey")
        l41.place(x=300,y=120)
        l42.place(x=300,y=180)
        l43.place(x=300,y=240)
        l44.place(x=300,y=300)
        l45.place(x=300,y=360)
        l46.place(x=300,y=420)
        e41=Entry(ekran1,fg="red",font=("impact",16),bg="grey",width=7)
        e42=Entry(ekran1,fg="red",font=("impact",16),bg="grey",width=7)
        e43=Entry(ekran1,fg="red",font=("impact",16),bg="grey",width=7)
        e44=Entry(ekran1,fg="red",font=("impact",16),bg="grey",width=7)
        e45=Entry(ekran1,fg="red",font=("impact",16),bg="grey",width=7)
        e46=Entry(ekran1,fg="red",font=("impact",16),bg="grey",width=7)
        e41.place(x=420,y=125)
        e42.place(x=420,y=185)
        e43.place(x=420,y=245)
        e44.place(x=420,y=305)
        e45.place(x=420,y=365)
        e46.place(x=420,y=425)
        kony=63
        for i in range(0,6):
            kony+=60
            l47=Label(ekran1,text="TL",fg="red",font=("impact",16),bg="grey")
            l47.place(x=510,y=kony)
        konyy=63
        for i in range(0,6):
            konyy+=60
            l47=Label(ekran1,text="TL",fg="red",font=("impact",16),bg="grey")
            l47.place(x=360,y=konyy)
        
        def kayıt():
            if(e41.get()!="" or e42.get()!="" or e43.get()!="" or e44.get()!="" or e45.get()!="" or e46.get()!=""):
                if(e41.get()!=""):
                    mycursor=vt.cursor()
                    sorgu4="update arac_ucretleri set fiyatlar=%s where tur_id=1"
                    deger4=(e41.get(),)
                    mycursor.execute(sorgu4,deger4)
                    vt.commit()
                if(e42.get()!=""):
                    mycursor=vt.cursor()
                    sorgu4="update arac_ucretleri set fiyatlar=%s where tur_id=2"
                    deger4=(e42.get(),)
                    mycursor.execute(sorgu4,deger4)
                    vt.commit()
                if(e43.get()!=""):
                    mycursor=vt.cursor()
                    sorgu4="update arac_ucretleri set fiyatlar=%s where tur_id=3"
                    deger4=(e43.get(),)
                    mycursor.execute(sorgu4,deger4)
                    vt.commit()
                if(e44.get()!=""):
                    mycursor=vt.cursor()
                    sorgu4="update arac_ucretleri set fiyatlar=%s where tur_id=4"
                    deger4=(e44.get(),)
                    mycursor.execute(sorgu4,deger4)
                    vt.commit()
                if(e45.get()!=""):
                    mycursor=vt.cursor()
                    sorgu4="update arac_ucretleri set fiyatlar=%s where tur_id=5"
                    deger4=(e45.get(),)
                    mycursor.execute(sorgu4,deger4)
                    vt.commit()
                if(e46.get()!=""):
                    mycursor=vt.cursor()
                    sorgu4="update arac_ucretleri set fiyatlar=%s where tur_id=6"
                    deger4=(e46.get(),)
                    mycursor.execute(sorgu4,deger4)
                    vt.commit()
                messagebox.showinfo("KAYIT","İŞLEM BAŞARI İLE GERÇEKLEŞTİ")
                ekran1.destroy()
            else:
                messagebox.showinfo("KAYIT","VERİ GİRİŞİ YAPILMADI")
        b8=Button(ekran1,text="KAYDET",bg="grey",fg="white",font=yazi2,command=kayıt)
        b8.place(x=200,y=500,width=200,height=40)
    def tum_araclar():
        ekran1=Toplevel(ekran)
        ekran1.title("TÜM ARAÇLAR")
        ekran1.geometry("1080x800+125+0")
        tablo3=Treeview(ekran1)
        tablo3.config(height=28)
        scrol3=ttk.Scrollbar(ekran1,orient="vertical",command=tablo3.yview)
        scrol3.place(x=1035,y=11,height=585)
        tablo3.configure(yscrollcommand=scrol3.set)

        tablo3["columns"] = ("Plaka", "Tür", "Şase no", "Marka","Model", "Yakıt Türü", "Şanzıman","Üretim tarihi" ,"KM","Durum")
        tablo3.column("#0",width=0,anchor='sw',stretch=tk.NO)
        tablo3.column("Plaka",width=100,anchor='sw')
        tablo3.column("Tür",width=100,anchor='sw')
        tablo3.column("Şase no",width=130,anchor='sw')
        tablo3.column("Marka",width=100,anchor='sw')
        tablo3.column("Model",width=100,anchor='sw')
        tablo3.column("Yakıt Türü",width=100,anchor='sw')
        tablo3.column("Şanzıman",width=100,anchor='sw')
        tablo3.column("Üretim tarihi",width=100,anchor='sw')
        tablo3.column("KM",width=100,anchor='sw')
        tablo3.column("Durum",width=100,anchor='sw')

        tablo3.heading("Plaka", text="Plaka",anchor='sw')
        tablo3.heading("Tür", text="Tür",anchor='sw')
        tablo3.heading("Şase no", text="Şase no",anchor='sw')
        tablo3.heading("Marka", text="Marka",anchor='sw')
        tablo3.heading("Model", text="Model",anchor='sw')
        tablo3.heading("Yakıt Türü", text="Yakıt Türü",anchor='sw')
        tablo3.heading("Şanzıman", text="Şanzıman",anchor='sw')
        tablo3.heading("Üretim tarihi", text="Üretim tarihi",anchor='sw')
        tablo3.heading("KM", text="KM",anchor='sw')
        tablo3.heading("Durum", text="Durum",anchor='sw')
        tablo3.place(x=20,y=10)
        def tabloveri2():
            mycursor=vt.cursor()
            sorgu29="select arac_plaka,arac_tur,arac_sase,arac_marka,arac_model,arac_yakit,arac_vites,arac_uretim,arac_km,arac_durum from tum_araclar"
            mycursor.execute(sorgu29)
            sonuc29=mycursor.fetchall()
            for satir in range(len(sonuc29)):
                for sutun in range(1):
                    tablo3.insert("", 0,values=(sonuc29[satir]))
            vt.commit()
        tabloveri2()
        def secilen_satır(deger):
            deger=tablo3.item(tablo3.selection())['values'][0]
            print(deger)
            degerbes.delete(0,END)
            degerbes.insert(0,deger)
            return deger
        tablo3.bind('<ButtonRelease-1>',secilen_satır)
        degerbes=Entry(ekran1)
        def güncelle():
            if(degerbes.get()==""):
                messagebox.showinfo("UYARI","LÜTFEN GÜNCELLEMEK İSTEDİĞİNİZ KAYDI SEÇİNİZ")
            else:
                ekran3=Toplevel(ekran1)
                ekran3.title("ARAÇ KAYDI GÜNCELLEME")
                ekran3.geometry("600x600+250+0")
                konumx=50
                konumy=80
                l49=Label(ekran3,text="ARAÇ KAYIT GÜNCELLEME",font=("arial",16,"italic"),fg="grey")
                l49.place(x=konumx+90,y=konumy-70)
                l50=Label(ekran3,text=degerbes.get(),font=("impact",14),fg="red")
                l50.place(x=konumx+330,y=konumy-40)
                l51=Label(ekran3,text="İşlem yapılan araç  :",font=yazi,fg="black")
                l51.place(x=konumx,y=konumy-40)
                l52=Label(ekran3,text="Araç plakasını giriniz :",font=(yazi))
                l52.place(x=konumx,y=konumy)
                e52=Entry(ekran3,text="plaka",font=(yazi1),width=22)
                e52.place(x=konumx+300,y=konumy)

                l53=Label(ekran3,text="Araç türünü seçiniz :",font=(yazi))
                l53.place(x=konumx,y=konumy+40)
                liste_tur=["TIR","KAMYON","KAMYONET","OTOBüS","MİNİBüS","OTOMOBİL"]
                e53=ttk.Combobox(ekran3)
                e53['values']=liste_tur
                e53.config(font=(yazi1))
                e53.place(x=konumx+300,y=konumy+40)

                l54=Label(ekran3,text="Şase numarası giriniz :",font=(yazi))
                l54.place(x=konumx,y=konumy+80)
                e54=Entry(ekran3,text="sase",font=(yazi1),width=22)
                e54.place(x=konumx+300,y=konumy+80)

                l55=Label(ekran3,text="Araç markasını giriniz :",font=(yazi))
                l55.place(x=konumx,y=konumy+120)
                e55=Entry(ekran3,text="marka",font=(yazi1),width=22)
                e55.place(x=konumx+300,y=konumy+120)

                    
                l56=Label(ekran3,text="Araç modelini giriniz :",font=(yazi))
                l56.place(x=konumx,y=konumy+160)
                e56=Entry(ekran3,text="model",font=(yazi1),width=22)
                e56.place(x=konumx+300,y=konumy+160)

                yakitt=StringVar(value="Seçilmedi")
                l57=Label(ekran3,text="Araç yakıt türünü seçiniz :",font=yazi)
                l57.place(x=konumx,y=konumy+200)
                r11=Radiobutton(ekran3,text="BENZİN",variable=yakitt,value="BENZİN",)
                r12=Radiobutton(ekran3,text="DİZEL",variable=yakitt,value="MAZOT",)
                r11.place(x=konumx+320,y=konumy+200)
                r12.place(x=konumx+400,y=konumy+200)

                vitess=StringVar(value="Seçilmedi")
                l58=Label(ekran3,text="Araç şanzıman tipini seçiniz :",font=yazi)
                l58.place(x=konumx,y=konumy+240)
                r13=Radiobutton(ekran3,text="MANUEL",variable=vitess,value="MAMNUEL")
                r14=Radiobutton(ekran3,text="OTOMATİK",variable=vitess,value="OTOMATİK")
                r13.place(x=konumx+320,y=konumy+240)
                r14.place(x=konumx+400,y=konumy+240)

                l58=Label(ekran3,text="Araç Üretim tarihini giriniz :",font=(yazi))
                l58.place(x=konumx,y=konumy+280)
                c11=Combobox(ekran3,width=4)
                c11['values'] = ("Gün", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", 
                "16", "17","18", "19","20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
                c11.current(0)
                c11.config(font=yazi1)
                c11.place(x=konumx+300,y=konumy+280)
                c12 = Combobox(ekran3,width=4)
                c12['values'] = ("Ay" , "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
                c12.current(0)
                c12.config(font=yazi1)
                c12.place(x=konumx+361,y=konumy+280)
                c13 = Combobox(ekran3,width=6)
                c13['values'] = ("Yıl","2020","2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007")
                c13.current(0)
                c13.config(font=yazi1)
                c13.place(x=konumx+422,y=konumy+280)
                #tarih birleştirme
                #ut_tarih=(c3.get()+"/"+c2.get()+"/"+c1.get())

                l59=Label(ekran3,text="Araç kilometre giriniz :",font=(yazi))
                l59.place(x=konumx,y=konumy+320)
                e59=Entry(ekran3,text="km",font=(yazi1),width=22)
                e59.place(x=konumx+300,y=konumy+320)
                durumm=StringVar(value="Seçilmedi")  
                l60=Label(ekran3,text="Araç durumunu seçiniz",font=yazi)
                l60.place(x=konumx,y=konumy+360)
                r5=Radiobutton(ekran3,text="AKTİF",variable=durumm,value="HAZIR")
                r6=Radiobutton(ekran3,text="PASİF",variable=durumm,value="SERVİSDE")
                r5.place(x=konumx+320,y=konumy+360)
                r6.place(x=konumx+400,y=konumy+360)
                l61=Label(ekran3,text="*Değiştirmek istediğiniz kısımları doldurunuzu !!!",fg="brown",font=yazi)
                l61.place(x=konumx+10,y=konumy+400)
                def kayıt5():
                    mycursor=vt.cursor()
                    sorgu30="select arac_id from tum_araclar where arac_plaka=%s"
                    deger30=(degerbes.get(),)
                    mycursor.execute(sorgu30,deger30)
                    sonuc30=mycursor.fetchone()
                    ut_tarihh=(c13.get()+"/"+c12.get()+"/"+c11.get())
                    if(e52.get()!=""):
                        sorgu31="update tum_araclar set arac_plaka=%s where arac_id=%s"
                        deger31=(e52.get(),sonuc30[0])
                        mycursor.execute(sorgu31,deger31)
                        e52.delete(0,END)
                    if(e53.get()!=""):
                        sorgu32="update tum_araclar set arac_tur=%s where arac_id=%s"
                        deger32=(e53.get(),sonuc30[0])
                        mycursor.execute(sorgu32,deger32)
                    if(e54.get()!=""):
                        sorgu33="update tum_araclar set arac_sase=%s where arac_id=%s"
                        deger33=(e54.get(),sonuc30[0])
                        mycursor.execute(sorgu33,deger33)
                        e54.delete(0,END)
                    if(e55.get()!=""):
                        sorgu34="update tum_araclar set arac_marka=%s where arac_id=%s"
                        deger34=(e55.get(),sonuc30[0])
                        mycursor.execute(sorgu34,deger34)
                        e55.delete(0,END)
                    if(e56.get()!=""):
                        sorgu35="update tum_araclar set arac_model=%s where arac_id=%s"
                        deger35=(e56.get(),sonuc30[0])
                        mycursor.execute(sorgu35,deger35)
                        e56.delete(0,END)
                    if(yakitt.get()!="Seçilmedi"):
                        sorgu36="update tum_araclar set arac_yakit=%s where arac_id=%s"
                        deger36=(yakitt.get(),sonuc30[0])
                        mycursor.execute(sorgu36,deger36)
                    if(vitess.get()!="Seçilmedi"):
                        sorgu37="update tum_araclar set arac_vites=%s where arac_id=%s"
                        deger37=(vitess.get(),sonuc30[0])
                        mycursor.execute(sorgu37,deger37)
                    if(c11.get()!="Gün" and c12.get()!="Ay" and c13.get()!="Yıl"):
                        sorgu38="update tum_araclar set arac_uretim=%s where arac_id=%s"
                        deger38=(ut_tarihh,sonuc30[0])
                        mycursor.execute(sorgu38,deger38)
                    if(e59.get()!=""):
                        sorgu39="update tum_araclar set arac_km=%s where arac_id=%s"
                        deger39=(e59.get(),sonuc30[0])
                        mycursor.execute(sorgu39,deger39)
                        e59.delete(0,END)
                    if(durumm.get()!="Seçilmedi"):
                        sorgu40="update tum_araclar set arac_durum=%s where arac_id=%s"
                        deger40=(durumm.get(),sonuc30[0])
                        mycursor.execute(sorgu40,deger40)
                    vt.commit()
                    messagebox.showinfo("BİLGİLENDİRME","GÜNCELLEME BAŞARILI BİR ŞEKİLDE GERÇEKLEŞTİRİLDİ")
                    ekran3.destroy()
                b11=Button(ekran3,text="KAYDET",bg="grey",fg="white",font=yazi2,command=kayıt5)
                b11.place(x=konumx+150,y=konumy+450,width=200,height=40)

        def sil():
            ekran1=Toplevel(ekran)
            ekran1.title("ARAÇ KAYIT SİLME")
            ekran1.geometry("600x600+250+0")
            l53=Label(ekran1,text="ARAÇ KAYIT SİLME",font=("arial",16,"italic"),fg="grey")
            l53.place(x=150,y=10)
            rastgele=str(degerbes.get())+"\n Plakalı aracınızı veritabanından silmek istiyorsanız.\n Lütfen plakayı tekrar giriniz"
            l54=Label(ekran1,text=rastgele,font=yazi,fg="black")
            l54.place(x=80,y=90)
            e55=Entry(ekran1,font=yazi,fg="black")
            e55.place(x=150,y=210)
            def sil2():
                print()
                if(e55.get()==degerbes.get()):
                    mycursor=vt.cursor()
                    sorgu41="delete from tum_araclar where arac_plaka=%s"
                    deger41=(e55.get(),)
                    mycursor.execute(sorgu41,deger41)
                    messagebox.showinfo("Bilgilendirme","İŞLEM BAŞARILI ARAC SİLİNDİ")
                else:
                    messagebox.showinfo("UYARI","Plakayı yanlış girdiniz")
            b11=Button(ekran1,text="KAYDI SİL",bg="grey",fg="red",font=yazi2,command=sil2)
            b11.place(x=180,y=240,width=200,height=40)
            
        b9=Button(ekran1,text="KAYDI GÜNCELLE",bg="grey",fg="white",font=yazi2,command=güncelle)
        b9.place(x=160,y=650,width=340,height=40)
        b10=Button(ekran1,text="KAYDI SİL",bg="grey",fg="white",font=yazi2,command=sil)
        b10.place(x=540,y=650,width=340,height=40)
    def kira_kayitlari():
        ekran1=Toplevel(ekran)
        ekran1.title("KİRALAMA KAYITLARI")
        ekran1.geometry("735x650+260+10")
        tablo4=Treeview(ekran1)
        tablo4.config(height=25)
        scrol4=ttk.Scrollbar(ekran1,orient="vertical",command=tablo4.yview)
        scrol4.place(x=694,y=11,height=525)
        tablo4.configure(yscrollcommand=scrol4.set)

        tablo4["columns"] = ("Plaka","TC","Ad", "Soyad", "Kiralama tarihi", "Teslim tarihi")
        tablo4.column("#0",width=0,anchor='sw',stretch=tk.NO)
        tablo4.column("Plaka",width=100,anchor='sw')
        tablo4.column("TC",width=100,anchor='sw')
        tablo4.column("Ad",width=100,anchor='sw')
        tablo4.column("Soyad",width=100,anchor='sw')
        tablo4.column("Kiralama tarihi",width=140,anchor='sw')
        tablo4.column("Teslim tarihi",width=150,anchor='sw')

        tablo4.heading("Plaka", text="Plaka",anchor='sw')
        tablo4.heading("TC", text="TC Kimlik no",anchor='sw')
        tablo4.heading("Ad", text="Ad",anchor='sw')
        tablo4.heading("Soyad", text="Soyad",anchor='sw')
        tablo4.heading("Kiralama tarihi", text="Kiralama tarihi",anchor='sw')
        tablo4.heading("Teslim tarihi", text="Teslim tarihi",anchor='sw')
        tablo4.place(x=20,y=10)
        def tabloveri3():
            mycursor=vt.cursor()
            sorgu42="SELECT arac_plaka,uye_tc,uye_ad,uye_soyad,arac_alim_tar,teslim_alınan_tar from kiralama_kayitlari inner join musteriler on musteriler.uye_tc=kiralama_kayitlari.üye_tc"
            mycursor.execute(sorgu42)
            sonuc42=mycursor.fetchall()
            for satir in range(len(sonuc42)):
                for sutun in range(1):
                    tablo4.insert("", 0,values=(sonuc42[satir]))
            vt.commit()
        tabloveri3()
        def kapat():
            ekran1.destroy()
        b13=Button(ekran1,text="GERİ DÖN",bg="grey",fg="white",font=yazi2,command=kapat)
        b13.place(x=270,y=580,width=200,height=40)
    def yenile2():
        mycursor=vt.cursor()
        sorgu16="select count(arac_durum) from tum_araclar where arac_durum='HAZIR'"
        mycursor.execute(sorgu16)
        aktif=mycursor.fetchone()
        sorgu17="select count(arac_durum) from tum_araclar where arac_durum='KİRADA'"
        mycursor.execute(sorgu17)
        kira=mycursor.fetchone()
        sorgu18="select count(arac_durum) from tum_araclar where arac_durum='SERVİSDE'"
        mycursor.execute(sorgu18)
        servis=mycursor.fetchone()
        sorgu19="select count(arac_plaka) from tum_araclar"
        mycursor.execute(sorgu19)
        toplam=mycursor.fetchone()
        vt.commit()
        l4=Label(ekran,text=aktif[0],font=("impact",12),bg="grey",fg="red")
        l5=Label(ekran,text=kira[0],font=("impact",12),bg="grey",fg="red")
        l6=Label(ekran,text=servis[0],font=("impact",12),bg="grey",fg="red")
        l7=Label(ekran,text=toplam[0],font=("impact",12),bg="grey",fg="red")
        l4.place(x=625,y=110)
        l5.place(x=625,y=140)
        l6.place(x=625,y=170)
        l7.place(x=625,y=200)
        l4.after(1000,yenile2)
    yenile2()
        
    yazi2=("georgia",12)
    kutu=Canvas(ekran,width=220,height=150)
    kutu.config(bg="grey")
    kutu.place(x=450,y=100)
    l1=Label(ekran,text="Hazır araçlar :",font=yazi2,bg="grey",fg="white")
    l2=Label(ekran,text="Kiradaki araçlar :",font=yazi2,bg="grey",fg="white")
    l3=Label(ekran,text="Servisdeki araçlar :",font=yazi2,bg="grey",fg="white")
    l4=Label(ekran,text="Toplam araç sayısı :",font=yazi2,bg="grey",fg="white")
    l1.place(x=465,y=110)
    l2.place(x=465,y=140)
    l3.place(x=465,y=170)
    l4.place(x=465,y=200)

    def zaman():
        saniyeder=0
        dakikader=0
        saatder=0
        tarih=time.strftime("%Y/%m/%d")
        l7=Label(ekran,text=tarih,font=yazi2,fg="white",bg="grey")
        l7.place(x=260,y=250)

        w=Canvas(ekran,width=150,height=150)
        w.place(x=230,y=100)
        w.create_oval(5,5,150,150,fill="red",width=2)
        w.create_oval(22,30,117,125,fill="white",width=2,outline="red")
        w.create_oval(46,40,118,115,fill="red",width=2,outline="red")
        w.create_polygon([110,55,139,91,91,79,139,63,110,100],fill="white",outline="white")
        w.create_oval(77,76,77,76,fill="black",width=6,outline="black")
        a=w.create_arc(10,10,145,145,start=saniyeder,extent=0,style="pieslice",width=2,outline="black")
        b=w.create_arc(30,30,125,125,start=dakikader,extent=0,style="pieslice",width=3,outline="black")
        c=w.create_arc(50,50,105,105,start=saatder,extent=0,style="pieslice",width=5,outline="black")
        def saatt():
            zaman1=""
            global saniyeder,dakikader,saatder
            saniye=int(time.strftime('%S'))
            dakika=int(time.strftime('%M'))
            saat=int(time.strftime('%H'))
            if(saniye!=zaman1):
                    zaman1=saniye
                    saniyeder=(saniye*(-6))+90
                    dakikader=(dakika*(-6))+90
                    saatder=(saat*(-30))+90
                    w.itemconfig(a,start=saniyeder)
                    w.itemconfig(b,start=dakikader)
                    w.itemconfig(c,start=saatder)
            w.after(50,saatt)
        saatt()
    zaman()

    b1=Button(ekran,text="YENİ ARAÇ EKLEME",bd="0",bg="grey",fg="white",command=ekleme,font=yazi2)
    b1.place(x=200,y=300,width=220,height=60)

    b2=Button(ekran,text="ARAÇ KİRALAMA",bd="0",bg="grey",fg="white", command=kiralama,font=yazi2)
    b2.place(x=450,y=300,width=220,height=60)

    b3=Button(ekran,text="ARAÇ TESLİM ALMA",bd="0",bg="grey",fg="white",command=teslim,font=yazi2)
    b3.place(x=200,y=400,width=220,height=60)

    b4=Button(ekran,text="SERVİS",bd="0",bg="grey",fg="white", command=servis,font=yazi2)
    b4.place(x=450,y=400,width=220,height=60)

    b5=Button(ekran,text="ARAÇ DURUM KONTROL",bd="0",bg="grey",fg="white", command=arac_durum,font=yazi2)
    b5.place(x=200,y=500,width=220,height=60)

    b6=Button(ekran,text="KİRA ÜCRETLERİ DÜZENLEME",bd="0",bg="grey",fg="white", command=ucretler,font=("georgia",10))
    b6.place(x=450,y=500,width=220,height=60)

    b7=Button(ekran,text="TÜM ARAÇLAR",bd="0",bg="grey",fg="white", command=tum_araclar,font=yazi2)
    b7.place(x=200,y=600,width=220,height=60)

    b8=Button(ekran,text="KİRALAMA KAYITLARI",bd="0",bg="grey",fg="white", command=kira_kayitlari,font=yazi2)
    b8.place(x=450,y=600,width=220,height=60)
ekran.title("GİRİŞ YAP")
ekran.geometry("600x400+400+100")
resim0 = Image.open("logo1.png")
re_resim=resim0.resize((300,70))
yukle = ImageTk.PhotoImage(re_resim)
goruntu1 = Label(ekran, image=yukle)
goruntu1.image = yukle
goruntu1.place(x=140, y=0)
konumx=200
konumy=110
la1=Label(ekran,text="KULLANICI ADI :",font=(yazi))
la1.place(x=konumx,y=konumy)
en1=Entry(ekran,text="kadi",font=(yazi1),width=22)
en1.place(x=konumx,y=konumy+30)
la2=Label(ekran,text="ŞİFRE :",font=(yazi))
la2.place(x=konumx,y=konumy+60)
en2=Entry(ekran,show="*",font=(yazi1),width=22)
en2.place(x=konumx,y=konumy+90)
def kontrol():
    mycursor=vt.cursor()
    sorgu0 = "select k_ad,k_sifre from kullanıcı where k_ad=%s and k_sifre=%s"
    deger0 = (en1.get(),en2.get())
    mycursor.execute(sorgu0, deger0)
    sutun=mycursor.fetchone()
    vt.commit()
    if(mycursor.rowcount==1):
        if(sutun[0]==en1.get() and sutun[1]==en2.get()):
            temizleme()
        else:
            messagebox.showwarning("GİRİŞ BAŞARISIZ","KULLANICI ADI VEYA ŞİFRE YANLIŞ")
    else:
        messagebox.showwarning("GİRİŞ BAŞARISIZ","KULLANICI VERİTABANINDA BULUNAMADI")
def temizleme():
    for widget in ekran.winfo_children(): 
        widget.destroy()
    giris()
but1=Button(ekran,text="Giriş Yap",font=(yazi),bg="grey",fg="white",bd="1",command=kontrol)
but1.place(x=konumx+50,y=konumy+140,width=100,height=30)

ekran.mainloop()
