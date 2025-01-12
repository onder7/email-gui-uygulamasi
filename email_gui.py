import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox, simpledialog
import configparser
import os

# Config dosyasını oku
def read_config():
    config = configparser.ConfigParser()
    if not os.path.exists("config.ini"):
        # Config dosyası yoksa varsayılan değerlerle oluştur
        config["SMTP"] = {
            "server": "smtp.gmail.com",
            "port": "587",
            "sender_email": "",
            "sender_password": "",
        }
        with open("config.ini", "w") as configfile:
            config.write(configfile)
    config.read("config.ini")
    return config

# Config dosyasını güncelle
def update_config(server, port, sender_email, sender_password):
    config = configparser.ConfigParser()
    config["SMTP"] = {
        "server": server,
        "port": port,
        "sender_email": sender_email,
        "sender_password": sender_password,
    }
    with open("config.ini", "w") as configfile:
        config.write(configfile)

# SMTP ayarlarını gösteren bir pencere
def show_settings():
    server = simpledialog.askstring("SMTP Ayarları", "SMTP Sunucusu:", initialvalue=config["SMTP"]["server"])
    port = simpledialog.askstring("SMTP Ayarları", "SMTP Portu:", initialvalue=config["SMTP"]["port"])
    sender_email = simpledialog.askstring("SMTP Ayarları", "Gönderici E-posta:", initialvalue=config["SMTP"]["sender_email"])
    sender_password = simpledialog.askstring("SMTP Ayarları", "Gönderici Şifre:", initialvalue=config["SMTP"]["sender_password"], show="*")

    if server and port and sender_email and sender_password:
        update_config(server, port, sender_email, sender_password)
        messagebox.showinfo("Başarılı", "SMTP ayarları güncellendi!")

# Hakkında penceresi
def show_about():
    about_text = """
    E-posta Gönderme Aracı

    Yazar: Önder Aköz
    E-posta: onder7@gmail.com
    GitHub: github.com/onder7

    Bu uygulama, Python ile SMTP kullanarak e-posta göndermeyi sağlar.
    """
    messagebox.showinfo("Hakkında", about_text)

# E-posta gönderme fonksiyonu
def send_email():
    try:
        # Kullanıcıdan alınan bilgiler
        receiver_email = entry_receiver.get()
        subject = entry_subject.get()
        body = text_body.get("1.0", tk.END)  # Text widget'ından gövdeyi al

        # E-posta mesajını oluştur
        message = MIMEMultipart()
        message["From"] = config["SMTP"]["sender_email"]
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # SMTP sunucusuna bağlan
        with smtplib.SMTP(config["SMTP"]["server"], int(config["SMTP"]["port"])) as server:
            server.starttls()  # TLS şifrelemesi başlat
            server.login(config["SMTP"]["sender_email"], config["SMTP"]["sender_password"])  # Giriş yap
            server.sendmail(config["SMTP"]["sender_email"], receiver_email, message.as_string())  # E-postayı gönder

        # Başarılı mesajı göster
        messagebox.showinfo("Başarılı", "E-posta başarıyla gönderildi!")

    except Exception as e:
        error_message = f"E-posta gönderilirken bir hata oluştu: {e}"
        print(error_message)
        messagebox.showerror("Hata", error_message)

# Config dosyasını oku
config = read_config()

# GUI oluştur
root = tk.Tk()
root.title("E-posta Gönderme Aracı")
root.geometry("500x400")

# Menü çubuğu oluştur
menu_bar = tk.Menu(root)

# Ayarlar menüsü
settings_menu = tk.Menu(menu_bar, tearoff=0)
settings_menu.add_command(label="SMTP Ayarları", command=show_settings)
menu_bar.add_cascade(label="Ayarlar", menu=settings_menu)

# Yardım menüsü
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Hakkında", command=show_about)
menu_bar.add_cascade(label="Yardım", menu=help_menu)

# Menü çubuğunu pencereye ekle
root.config(menu=menu_bar)

# Etiketler ve Giriş Alanları
label_receiver = tk.Label(root, text="Alıcı E-posta:")
label_receiver.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_receiver = tk.Entry(root, width=40)
entry_receiver.grid(row=0, column=1, padx=10, pady=5)

label_subject = tk.Label(root, text="Konu:")
label_subject.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_subject = tk.Entry(root, width=40)
entry_subject.grid(row=1, column=1, padx=10, pady=5)

label_body = tk.Label(root, text="E-posta Gövdesi:")
label_body.grid(row=2, column=0, padx=10, pady=5, sticky="w")
text_body = tk.Text(root, width=40, height=10)
text_body.grid(row=2, column=1, padx=10, pady=5)

# Gönder Butonu
button_send = tk.Button(root, text="E-postayı Gönder", command=send_email)
button_send.grid(row=3, column=1, padx=10, pady=10, sticky="e")

# Uygulamayı çalıştır
root.mainloop()