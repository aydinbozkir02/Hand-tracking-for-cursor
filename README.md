# El Takibi ile Fare Kontrol Projesi

Bu proje, Python, OpenCV, MediaPipe ve PyAutoGUI kullanılarak el hareketlerini takip eden ve belirli el hareketlerine göre fare kontrolü sağlayan bir uygulamadır. Proje ile el hareketlerini kullanarak:
- Ekran imlecini kontrol edebilirsiniz.
- Sol tıklama, sağ tıklama yapabilirsiniz.
- Belirli bir el hareketi (yumruk kapatma) algılandığında 'q' tuşuna basılarak (örneğin ekran kapatma) aksiyon tetiklenebilir.

## Özellikler
- **Gerçek Zamanlı El Takibi:**  
  Web kamerasından alınan görüntü üzerinde MediaPipe ile el tespiti yapılır.
- **İmleç Hareket Kontrolü:**  
  İşaret parmağı ucuna göre ekran imleci, yumuşatma filtresi ile akıcı bir şekilde hareket eder.
- **Fare Tıklama İşlevleri:**  
  - **Sol Tıklama:** İşaret parmak ile başparmak arasındaki mesafe belirli bir eşik altına düştüğünde.
  - **Sağ Tıklama:** İşaret parmak ile orta parmak arasındaki mesafe belirli bir eşik altına düştüğünde.
- **Ekran Kapatma (Tuşa Basma):**  
  Belirli bir el hareketi (örneğin, elin iç kısmındaki mesafe belirli bir değerin altına düştüğünde) 'q' tuşuna basma aksiyonu tetiklenir.
- **Görsel Geri Bildirim:**  
  Yapılan aksiyonlar (örneğin "Sol Tik", "Sag Tik", "q") ekrana metin olarak yazdırılır.

## Gereksinimler
- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)
- [MediaPipe](https://pypi.org/project/mediapipe/)
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)

## Kurulum
Öncelikle gerekli kütüphaneleri yüklemek için terminalde aşağıdaki komutu çalıştırın:

```bash
pip install opencv-python mediapipe pyautogui
