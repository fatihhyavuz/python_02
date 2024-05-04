import random as rd

sayi = rd.randint(1,100)

hak = 15

while hak > 0:
    tahmin = int(input("tahmininiz: "))
    hak -= 1
    if tahmin == sayi:
        print("tebrikler dogru bldiniz")
        break
    elif hak == 0 :
        print("hakkiniz  bitti dogru sayi:" + str(sayi))
        break 
    elif tahmin > sayi :
        print("assagi in ")
        continue
    elif tahmin < sayi :
        print("yukari cik ")

    
  