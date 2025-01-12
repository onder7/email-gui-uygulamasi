# E-posta Gönderme GUI Uygulaması

Bu uygulama, Python ve `tkinter` kütüphanesi kullanılarak geliştirilmiş bir grafik kullanıcı arayüzü (GUI) ile e-posta göndermeyi sağlar. Uygulama, SMTP protokolünü kullanarak e-posta gönderir ve kullanıcı dostu bir arayüz sunar. Ayrıca, SMTP ayarlarını bir `config.ini` dosyasından okuyarak esneklik sağlar.

---

## Özellikler

- **Kullanıcı Dostu Arayüz**: Basit ve anlaşılır bir GUI ile e-posta gönderme işlemi.
- **SMTP Ayarları Yönetimi**: SMTP sunucusu, port, gönderici e-posta ve şifre bilgilerini `config.ini` dosyasından okur.
- **Hata Yönetimi**: E-posta gönderimi sırasında oluşabilecek hatalar kullanıcıya bildirilir.
- **Hakkında ve Ayarlar Menüsü**: Uygulama hakkında bilgi ve SMTP ayarlarını düzenleme imkanı.

---

## Kurulum

### Gereksinimler

- Python 3.x
- `tkinter` (Python ile birlikte gelir, ek kurulum gerekmez)
- `configparser` (Python ile birlikte gelir, ek kurulum gerekmez)

### Adımlar

1. **Projeyi İndirin**:
   - Proje dosyalarını bilgisayarınıza indirin veya kopyalayın.

2. **Config Dosyasını Oluşturun**:
   - Proje dizininde `config.ini` adında bir dosya oluşturun ve aşağıdaki içeriği ekleyin:
     ```ini
     [SMTP]
     server = smtp.gmail.com
     port = 587
     sender_email = gönderici@gmail.com
     sender_password = şifreniz
     ```
   - Gmail kullanıyorsanız ve iki faktörlü kimlik doğrulama (2FA) etkinse, [Google Hesap Ayarları](https://myaccount.google.com/) üzerinden bir "Uygulama Şifresi" oluşturun ve bu şifreyi `sender_password` alanına girin.

3. **Uygulamayı Çalıştırın**:
   - Terminal veya komut istemcisinde proje dizinine gidin.
   - Aşağıdaki komutu çalıştırarak uygulamayı başlatın:
     ```bash
     python email_gui.py
     ```

---

## Kullanım

1. **Ana Pencere**:
   - Uygulama başladığında, alıcı e-posta adresi, konu ve e-posta gövdesi için giriş alanları görüntülenecektir.

2. **E-posta Gönderme**:
   - Alıcı e-posta adresini, konuyu ve e-posta gövdesini girin.
   - "E-postayı Gönder" butonuna tıklayarak e-postayı gönderin.

3. **SMTP Ayarları**:
   - "Ayarlar > SMTP Ayarları" menüsünden SMTP sunucusu, port, gönderici e-posta ve şifre bilgilerini güncelleyebilirsiniz.

4. **Hakkında Menüsü**:
   - "Yardım > Hakkında" menüsünden uygulama hakkında bilgi alabilirsiniz.

---

## Ekran Görüntüleri

### Ana Pencere
![Ana Pencere](https://i.imgur.com/0hKEzG1.jpg)

### SMTP Ayarları Penceresi
![SMTP Ayarları](https://i.imgur.com/2hscGMy.png)

### Hakkında Penceresi
![Hakkında](https://i.imgur.com/jwOa6o5.png)

---

## Yazar Bilgileri

- **Yazar**: Önder Aköz
- **E-posta**: onder7@gmail.com
- **GitHub**: [github.com/onder7](https://github.com/onder7)

---

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

---

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:
1. Bu depoyu forklayın.
2. Yeni bir branch oluşturun (`git checkout -b yeni-ozellik`).
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`).
4. Branch'inizi pushlayın (`git push origin yeni-ozellik`).
5. Bir Pull Request oluşturun.

---

## Teşekkürler

- Python ve `tkinter` ekibine bu harika araçları sağladıkları için teşekkürler!
- Tüm kullanıcılara ve katkıda bulunanlara teşekkürler!

---

