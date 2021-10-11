print("\n\n")

# Tampil Menu
print("GEROBAK FRIED CHICKEN")
print("==============================================")
print("| Kode       Jenis Potongan      Harga       |")
print("==============================================")
print("| D          Dada                Rp. 2500    |")
print("| P          Paha                Rp. 2000    |")
print("| S          Sayap               Rp. 1500    |")
print("==============================================")
print("\n")

# Input
banyakJenis = int(input("Banyak Jenis   : "))
print("")

for i in range(banyakJenis) :
    print("Jenis ke-" + str(i+1))
    kodePotong = input("Kode Potong [D/P/S] : ")
    banyakPotong = int(input("Banyak Potong     : "))

    # Proses
    if (kodePotong == "D" or kodePotong == "d") :
        jenisPotong = "Dada"
        hargaSatuan = 2500
        totalBayar = hargaSatuan * banyakPotong

    elif (kodePotong == "P" or kodePotong == "p") :
        jenisPotong = "Paha"
        hargaSatuan = 2000
        totalBayar = hargaSatuan * banyakPotong

    elif (kodePotong == "S" or kodePotong == "s") :
        jenisPotong = "Sayap"
        hargaSatuan = 1500
        totalBayar = hargaSatuan * banyakPotong

    else :
        jenisPotong = "Error"
        hargaSatuan = "Error"
        totalBayar = "Error"

# Proses


# Output
print("\n")
print("GEROBAK FRIED CHICKEN")
print("======================================================")
print("| No.    Jenis       Harga       Banyak      Jumlah  |")
print("|        Potong      Satuan      Beli        Harga   |")
print("======================================================")
print("| %i     %s          Rp. %i      %i      Rp. %i  |" % (i, jenisPotong, hargaSatuan, banyakPotong, totalBayar))


print("\n\n")
