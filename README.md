# Pyhton-Tkinter-Mysql-ornek-Proje
 Tkinter modülü ile araç kiralama filosu yönetim uygulaması projesi<br>
 Localhost'da çalıştığı için XAMMP uygulamasının APACHE SERVER ve MYSQL kısımlarını aktif etmelisiniz.Alternetif programlarda kullanabilirsiniz.<br>
 Daha sonra phpmyadmin sayfasından yeni veritabanı oluşturmalı ismi:"tasicom"<br>
 Daha sonra phpmyadmin sayfasından veritabanımızı içe aktarmalısınız.(Proje dosyalarının arasında "tasicom.sql") <br>
<br>
# import edilmesi gereken kütüphaneler

from tkinter.ttk import*<br>
from tkinter import *<br>
from tkinter import messagebox<br>
import tkinter as tk<br>
import tkinter.ttk as ttk<br>
import mysql.connector<br>
from PIL import Image, ImageTk<br>
import time<br>
import datetime<br><br>
import random<br>
NOT:PC'nizde olmayan kütüphaneleri pip ile kurmalısınız.
# Giriş yapma
Giriş yapabilmek için üyeler tablosu kullanılmaktadır.<br>
Phpmyadmin sayfasından manuel veri ekleyebilir yeni bi hesap oluşturabilirsiniz veya vereceğim kullanıcı adı ve şifre ile giriş yapabilirsiniz.<br>
<br>
kullanıcıadı:admin <br>
şifre:12345<br>
<br>
Programımız sorunsuz şekilde çalıçaktır.<br><br>
Yardımcı olmamı istediğiniz kısımlar için hakangvnc@mail.com.tr hesabına mesaj atarak bana ulaşabilirniz.<br>
