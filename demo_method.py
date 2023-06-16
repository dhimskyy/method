#function
def hitung_luas_persegi(sisi):
    hasil = sisi * sisi
    return hasil

print("Luas persegi: %d" % hitung_luas_persegi(10))

#prosedur
def hitung_luas_segiiga(alas, tinggi):
    hasil = (alas * tinggi) / 2
    print("Luas Setiga: %d" % hasil)
    
hitung_luas_segiiga(10, 5)

#parameter
def salam(ucapan):
    print(ucapan)

salam("Hallo, selamat pagi")