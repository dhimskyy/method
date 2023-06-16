#fungsi penjumlahan
def penjumlahan(x, y):
    hasil = x + y
    return hasil

#fungsi pengurangan
def pengurangan(x, y):
    hasil = x - y
    return hasil

#fungsi perkalian
def perkalian(x, y):
    hasil = x * y
    return hasil

#fungsi pembagian
def pembagian(x, y):
    hasil = x / y
    return hasil

#fungsi pangkat
def pangkat(x, y):
    hasil = x ** y
    return hasil

#menu
print("Kalkulator")
print("1. penjumlahan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")
print("5. pangkat")

pilih = (input("Masukkan pilihan: "))
angka1 = int(input("Masukkan bilangan pertama: "))
angka2 = int(input("Masukkan bilangan kedua: "))

if pilih == '1':
    print(f"Hasil penjumlahan: {penjumlahan(angka1, angka2)}")
elif pilih == '2':
    print(f"Hasil pengurangan: {pengurangan(angka1, angka2)}")
elif pilih == '3':
    print(f"Hasil perkalian: {perkalian(angka1, angka2)}")
elif pilih == '4':
    print(f"Hasil pembagian: {pembagian(angka1, angka2)}")
elif pilih == '5':
    print(f"Hasil pangkat: {pangkat(angka1, angka2)}")
else:
    print("Pilihan anda tidak valid")