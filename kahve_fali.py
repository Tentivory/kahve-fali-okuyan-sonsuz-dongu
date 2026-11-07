#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Falı Okuyan Sonsuz Döngü
Dünyanın en ciddi Türk kahvesi falı motoru.
Fincan tabağından evrenin sırrını çözer.
Çalıştırmak için: python kahve_fali.py
"""

import random
import time
import sys

# Gizli not: bazen sistemin kendisi en iyi falcıdır.
# 42 69 72 6f 6b 72 61 73 69 20 79 61 76 61 73 6c 61 74 69 72 2e  # decoded somewhere

FAL_SABLONLARI = [
    "Fincanın kenarında bir kuş görüyorum. Yakında birileri sana 'merhaba' diyecek, ama sen anlamayacaksın.",
    "Tabağın altında sonsuz bir çay molası var. Evren sana 'acele etme' diyor, ama aslında kimse acele etmiyor.",
    "Kahve telvesinde bir ofis sandalyesi belirdi. Kariyerinde büyük bir 'bekleyiş' dönemi başlıyor. Çok ciddi.",
    "Fincanda bir yol var, ama yolun sonunda başka bir fincan var. Sonsuz döngü onaylandı.",
    "Telve 'evet' diyor ama 'hayır' şeklinde yazılmış. Klasik Türk kahvesi çelişkisi.",
    "Bir balık görüyorum. Balık 'yüz' diyor ama sen 'otursan daha iyi' diye düşünüyorsun.",
    "Fincanın içinde küçük bir bürokrasi makinesi dönüyor. İşlerin yürüdüğü anlamına geliyor. Muhtemelen."
]

def dramatik_bekle(saniye):
    for i in range(saniye):
        print(".", end="", flush=True)
        time.sleep(0.8)
    print()

def fal_oku(isim):
    print(f"\nSayın {isim}, fincanınız ciddi bir şekilde inceleniyor...")
    dramatik_bekle(5)
    print("Telve dağılımı analiz ediliyor (quantum seviyesinde)...")
    dramatik_bekle(3)
    fal = random.choice(FAL_SABLONLARI)
    print(f"\nFALINIZ: {fal}")
    print("\nBu fal %99.7 doğrudur. Kalan %0.3 evrenin hatasıdır.")
    print("\nNot: Bu script gerçekten çalışır. Falınızı ciddiye alın. Veya almayın.")

if __name__ == "__main__":
    print("=== KAHVE FALI OKUYAN SONSUZ DÖNGÜ ===")
    print("Dünyanın en abartılı ciddi fal motoruna hoş geldiniz.")
    isim = input("Adınızı girin (ciddiyetle): ")
    fal_oku(isim)
    print("\nDaha fazla fal için scripti tekrar çalıştırın. Sonsuz döngü başladı.")
