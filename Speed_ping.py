# Testowanie predkosci przesylu

# wywolanie biblioteki do testowanie przesylu danych speedtest-cli
import time
import speedtest
import os
from ping3 import ping
tester = speedtest.Speedtest()
# wprowadzenie testera predkosci


# Wybieranie najlepszego serwera do sciagania/wysylania

# tester.get_best_server()

# zwracanie wartosci testow predkosci

print("""
      ##############################
      ## Testowanie predkosci ######
      ##############################
      
      ##############################
      Menu:
          1- Pingowanie do roznych punktow                  ##
          2- Sprawdzanie predkosci DOWNLOAD - szczegolowe   ##
          3- Sprawdzanie predkosci UPLOAD - szczegolowe     ##
          4- Ping, DOWNLOAD, UPLOAD - szybki test           ##
      ##############################
          
      """)
print("Ładowanie listy serwerów SpeedTest...")
tester.get_servers()
print("Wybieranie optymalnego...")
best = tester.get_best_server()
# rozne mechanizmy pingowania
ping_1 = os.system("ping wp.pl")
ping_2 = os.system("ping onet.pl")
ping_5 = round(ping("cnn.com"), 3)
ping_6 = round(ping("212.77.98.9"), 3)
ping_7 = round(ping("google.com"), 3)

print("Znaleziono ", best['host'], " Zlokalizowany: ", best['country'])
menu = input("Podaj wartosc z menu do realizacji: ")

if menu == "1":
    ## Pingowanie
    print("Ping do wp.pl: ", ping_1)
    print("Ping do onet.pl: ", ping_2)
    print("Ping do cnn.com: ", ping_5)
    print("Ping do wp.pl po IP /212.77.98.9/: \n", ping_6)
    print("""
          
          ##############################
          ## Koniec pingowania    ######
          ##############################
          
         
          """)
elif menu == "2":
    ## Download
    ping_1 = tester.results.ping
    print("Czas pingu w ramach Speedtest: ",ping_1," ms")
    tic1 = round(time.perf_counter())
    print("Rozpoczalem download o czasie: ", tic1)
    download_1 = (round(tester.download() / 1000 / 1000, 1))
    toc1 = time.perf_counter()
    czas_tic_toc1 = round(toc1 - tic1)
    print("Predkosc download: ", download_1," Mbit/s. Zajeło to: ", czas_tic_toc1, " sekund")
    tester.get_servers()
    print("Zmieniam serwer....")
    best = tester.get_best_server()
    print("Znaleziono ", best['host'], " Zlokalizowany: ", best['country'])
    tic2 = time.perf_counter()
    download_2 = (round(tester.download() / 1000 / 1000, 1))
    toc2 = time.perf_counter()
    czas_tic_toc2 = round(toc2 - tic2)
    print("Predkosc download: ", download_2, " Mbit/s. Zajeło to: ", czas_tic_toc2, " sekund")
    srednia_dl = (round((download_1 + download_2)/2))
    print("Srednia predkosc DOWNLOAD: ", srednia_dl, " Mbit/s")
    print("""
          
          ##############################
          ## Koniec Download      ######
          ##############################
          
         
          """)
elif menu == "3":
    ## Upload
   ping_1 = tester.results.ping
   print("Czas pingu w ramach Speedtest: ", ping_1, " ms")
   tic3 = round(time.perf_counter())
   print("Rozpoczalem upload o czasie: ", tic3)
   upload_1 = (round(tester.upload() / 1000 / 1000, 1))
   toc3 = time.perf_counter()
   czas_tic_toc3 = round(toc3 - tic3)
   print("Predkosc upload: ", upload_1, " Mbit/s. Zajeło to: ", czas_tic_toc3, " sekund")
   tester.get_servers()
   print("Zmieniam serwer....")
   best = tester.get_best_server()
   print("Znaleziono ", best['host'], " Zlokalizowany: ", best['country'])
   tic4 = time.perf_counter()
   upload_2 = (round(tester.upload() / 1000 / 1000, 1))
   toc4 = time.perf_counter()
   czas_tic_toc4 = round(toc4 - tic4)
   print("Predkosc upload: ", upload_2, " Mbit/s. Zajeło to: ", czas_tic_toc4, " sekund")
   srednia_up = (round((upload_1 + upload_2)/2))
   print("Srednia predkosc UPLOAD: ", srednia_up, " Mbit/s")
   print("""
          
          ##############################
          ## Koniec Upload        ######
          ##############################
          
         
          """)
   
elif menu == "4":
    ## Wszystko
    print("Ping do wp.pl: ", ping_1)
    print("Ping do onet.pl: ", ping_2)
    print("Ping do cnn.com: ", ping_5)
    print("Ping do google.com: ", ping_7)
    print("Ping do wp.pl po IP /212.77.98.9/: \n", ping_6)
    ping_1 = tester.results.ping
    print("Czas pingu w ramach Speedtest: \n",ping_1," ms")
    download = (round(tester.download() / 1000 / 1000, 1))
    print("Predkosc download: \n", download," Mbit/s")
    upload = (round(tester.upload() / 1000 / 1000, 1))
    print("Predkosc upload: \n",upload," Mbit/s")
    
    print("""
          
          ##############################
          ## Koniec Wszystkiego   ######
          ##############################
                   
          """)
else:
    print("Warunki nie zadziałały")
input("Nacisnij Enter by zakonczyc...")