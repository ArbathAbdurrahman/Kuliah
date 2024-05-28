import os
os.system("cls")
while True:
  print("Pilih Salah Satu\n 1. Celcius ke Fahrenheit\n 2. Fahrenheit ke Celcius\n 3. Kelvin ke Celcius\n 4. Celcius ke Kelvin \n 5. Kelvin ke Fahrenheit\n 6. Fahrenheit ke Kelvin")
  pilihan = int(input("Masukkan Pilihan Anda : "))
  if pilihan == 1:
    celcius = float(input("Masukkan Suhu Celcius : "))
    fahrenheit = (celcius * 9/5) + 32
    print("Suhu Fahrenheit adalah", fahrenheit)
  elif pilihan == 2:
    fahrenheit = float(input("Masukkan Suhu Fahrenheit : "))
    celcius = (fahrenheit - 32) * 5/9
    print("Suhu Celcius adalah", celcius)
  elif pilihan == 3:
    kelvin = float(input("Masukkan Suhu Kelvin : "))
    celcius = kelvin - 273.15
    print("Suhu Celcius adalah", celcius)
  elif pilihan == 4:
    celcius = float(input("Masukkan Suhu Celcius"))
    kelvins = celcius + 273.15
    print("Suhu Kelvin adalah", kelvins)
  elif pilihan == 5:
    kelvin = float(input("Masukkan Suhu Kelvin : "))
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print("Suhu Fahrenheit adalah", fahrenheit)
  elif pilihan == 6 :
    fahrenheit = float(input("Masukkan Suhu Fahrenheit : "))
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print("Suhu Kelfin adalah", kelvin)
  else :
    print("Input yang anda masukan Salah")
