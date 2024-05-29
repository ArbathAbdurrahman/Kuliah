import os
import celtofah
import fahtocel
import keltocel
import celtokel
import keltofah
import fahtokel
import retocel
import retokel
import retofah
import celtore
import keltore
import fahtore
os.system("cls")
while True:
  print(f"\nPilih Salah Satu\n{'-'*40}\n1. Celcius ke Fahrenheit\n2. Fahrenheit ke Celcius\n3. Kelvin ke Celcius\n4. Celcius ke Kelvin \n5. Kelvin ke Fahrenheit\n6. Fahrenheit ke Kelvin\n7. Celcius ke Reamur\n8. Fahrenheit ke Reamur\n9. Kelvin ke Reamur\n10. Reamur ke Celcius\n11. Reamur ke Fahrenheit\n12. Reamur ke Kelvin\n{'-'*40}")
  pilihan = int(input("Masukkan Pilihan Anda : "))
  if pilihan == 1:
    celcius = float(input("Masukkan Suhu Celcius : "))
    celtofah.ctf(celcius)
  elif pilihan == 2:
    fahrenheit = float(input("Masukkan Suhu Fahrenheit : "))
    fahtocel.ftc(fahrenheit)
  elif pilihan == 3:
    kelvin = float(input("Masukkan Suhu Kelvin : "))
    keltocel.ktc(kelvin)
  elif pilihan == 4:
    celcius = float(input("Masukkan Suhu Celcius : "))
    celtokel.ctk(celcius)
  elif pilihan == 5:
    kelvin = float(input("Masukkan Suhu Kelvin : "))
    keltofah.ktf(kelvin)
  elif pilihan == 6:
    fahrenheit = float(input("Masukkan Suhu Fahrenheit : "))
    fahtokel.ftk(fahrenheit)
  elif pilihan == 7:
    celcius = float(input("Masukkan Suhu Celcius : "))
    celtore.ctr(celcius)
  elif pilihan == 8:
    fahrenheit = float(input("Masukkan Suhu Fahrenheit : "))
    fahtore.ftr(fahrenheit)
  elif pilihan == 9:
    kelvin = float(input("Masukkan Suhu Kelvin : "))
    keltore.ktr(kelvin)
  elif pilihan == 10:
    reamur = float(input("Masukkan Suhu Reamur : "))
    retocel.rtc(reamur)
  elif pilihan == 11:
    reamur = float(input("Masukkan Suhu Reamur : "))
    retofah.rtf(reamur)
  elif pilihan == 12:
    reamur = float(input("Masukkan Suhu Reamur : "))
    retokel.rtk(reamur)
  else :
    print("Pilihan yang anda masukan Salah!")
  input("Tekan Enter Untuk Lanjut...")
  os.system("cls")