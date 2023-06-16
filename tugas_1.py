def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

bilangan = int(input("Masukkan bilangan: "))
hasil = cek_ganjil_genap(bilangan)
print("Bilangan yang anda masukkan adalah", hasil)