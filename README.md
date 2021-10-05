# Pyhton-Tkinter-Mysql-ornek-Proje
 Tkinter modülü ile araç kiralama filosu yönetim uygulaması projesi<br>
 Localhost'da çalıştığı için XAMMP uygulamasının APACHE SERVER ve MYSQL kısımlarını aktif etmelisiniz.Alternetif programlarda kullanabilirsiniz.
 Daha sonra phpmyadmin sayfasından yeni veritabanı oluşturmalı ismi:"tasicom"
 Daha sonra phpmyadmin sayfasından veritabanımızı içe aktarmalısınız.(Proje dosyalarının arasında "tasicom.sql") 

# import edilmesi gereken kütüphaneler

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

#NOT:PC'nizde olmayan kütüphaneleri pip ile kurlmalısınız.

# Programımız sorunsuz şekilde çalıçaktır.
# Giriş yapabilmek için üyeler tablosu kullanılmaktadır.
# Phpmyadmin sayfasından manuel veri ekleyebilir yeni bi hesap oluşturabilirsiniz veya vereceğim kullanıcı adı ve şifre ile giriş yapabilirsiniz.

# kullanıcıadı:admin 
# şifre:12345

# Yardımcı olmamı istediğiniz kısımlar için hakangvnc@mail.com.tr hesabına mesaj atarak bana ulaşabilirniz.
