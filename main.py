import telebot
import random
import json
import telegram
import requests
from bs4 import BeautifulSoup
import time 
bot = telebot.TeleBot("") # Tokeni buraya girin

@bot.message_handler(commands=['start'])
def send_welcome(message):

    # Diğer işlemler devam etirir
    
   
    
    bot.reply_to(message, "══════════════════\nMerhaba, bu bir fiyat takip botudur! komutlar listelenmiştir...\n\n"
                        
                          "/trendyol <ilan-url> <ilan-fiyat>  (Aktif)\n"
                          "örnek kod biçimi : <ilan-url> 58.14\n"
                          "══════════════════   \n"
                          
                          " Developer: Eray Özkan")

print("BOT ÇALIŞIYOR")

@bot.message_handler(commands=['trendyol'])
def handle_Trendyol(message):
    TRENDYOL_URL = message.text.split()[1]
    
    
    bot.reply_to(message, ("Ürünün fiyatı düşünce veya düşmediğinde haber alıcaksınız👍👍"))
    # Trendyol ürün linki


    # Takip edilecek fiyat


    
    def fiyat_takibi(message):
        
        
        
        
    
    # Kullanıcıdan takip edilecek fiyatı al
        
        
        
        
        takip_edilen_fiyat = float(message.text.split()[2   ])
   
        
        
        while True:
            try:
                # Trendyol sayfasını getir ve içeriğini çözümle
                response = requests.get(TRENDYOL_URL)
                soup = BeautifulSoup(response.content, "html.parser")

                # Ürün fiyatını al
                fiyat = float(soup.find("span", {"class": "prc-dsc"}).text.strip().replace("TL", "").replace(",", "."))

                # Fiyat değişikliklerini kontrol et ve Telegram'a bildir
                if fiyat < takip_edilen_fiyat:
                    bot.reply_to(message, (TRENDYOL_URL+"Ürünün fiyatı düştü👍👍"))
                
                # 5 dakika bekle ve tekrar kontrol et
                time.sleep(300)
            except Exception as e:
                print("Hata:", e)
                time.sleep(300)

    fiyat_takibi(message)
    
           

bot.polling()
