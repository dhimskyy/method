#function
def keliling_persegi(sisi):
    return 4 * sisi
def luas_persegi(sisi):
    return sisi * sisi

panjang = int(input("Masukkan panjang sisi: "))
print("Keliling persegi: ", keliling_persegi(panjang))
print("Luas persegi: ", luas_persegi(panjang))


#prosedur
def keliling_luas_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    print("Keliling persegi: %d" % keliling)
    print("Luas Persegi: %d" % luas)
panjang = int(input("Masukkan panjang sisi: "))
keliling_luas_persegi(panjang)