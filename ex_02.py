def ters_cevir(liste):
    sol = 0
    sag = len(liste) - 1
    while sol < sag:
        liste[sol], liste[sag] = liste[sag], liste[sol]
        sol += 1
        sag -= 1
    return liste

# Test
liste = [1, 2, 3, 4, 5]
print(ters_cevir(liste))  # Çıktı: [5, 4, 3, 2, 1]

def metin_isle(metin):
    # Metni küçük harfe dönüştürme
    metin = metin.lower()
    # Boşlukları kaldırma
    metin = metin.replace(" ", "")
    # Metni tersine çevirme
    metin = metin[::-1]
    return metin

def alfanumerik_mi(metin):
    return metin.isalnum()

def main():
    while True:
        kullanici_girdisi = input("Metin girin: ")
        if alfanumerik_mi(kullanici_girdisi):
            islenmis_metin = metin_isle(kullanici_girdisi)
            print(f"İşlenen metin: {islenmis_metin}")
            break
        else:
            print("Hatalı giriş! Lütfen sadece harf ve rakam içeren bir metin girin.")

if __name__ == "__main__":
    main()
