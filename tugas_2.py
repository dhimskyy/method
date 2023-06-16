# function
def luas_lingkaran(jari_jari):
    luas = 3.14 * r * r
    return luas

def keliling_lingkaran(jari_jari):
    keliling = 2 * 3.14 * r
    return keliling

r = int(input("Masukkan jari jari: "))
print(f"Luas lingkaran: {luas_lingkaran(r)} ")
print(f"Keliling lingkaran: {keliling_lingkaran(r)} ")