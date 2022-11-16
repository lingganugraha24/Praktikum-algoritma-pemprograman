# NAMA  : Lingga Nugraha
# NIM   : 2270231079
# KELAS : P2K

print("= = = = = = = TOKO Handphone = = = = = = =")
print("\n")
handphone = {
    "Iphone 8 plus":5000000,
    "Iphone xr":7000000,
    "Iphone 11":8000000,
    "Iphone 11 pro":9000000,
    "Iphone 11 pro":10000000,
    "Iphone 12":11000000,
    "Iphone 12 pro":13000000
}
for i in handphone:
    print(i,"\t Harga: ",handphone[i])
print("+++Pembelian di atas Rp5.000.000 diskon 20%+++")
print("FORMAT PEMESANAN MOHON DI ISI BOS :)")
nama_pelanggan = input("Nama: ")
alamat = input("Alamat: ")
no = input("No Telfon: ")
beli = input("Nama Barang: ")
Jumlah = int(input("Jumlah Pembelian: "))
bayar = Jumlah*handphone[beli]
if bayar > 5000000:
    diskon = bayar * 20/100
    total = bayar - diskon
else:
    total = bayar
print("\n")

print("= = = = = = = RINCIAN PESANAN = = = = = = =")
print("Nama Pemesan                                 :",nama_pelanggan)
print("Alamat Pemesan                               :",alamat)
print("Nomer telpon                                 :",no)
print("Handphone yang dipilih                       :",beli)
print("Jumlah Barang                                :",Jumlah)
print("Total Pembayaran                             : Rp.",bayar)
print("Total Keseluruhan dengan diskon              : Rp.",total)
import datetime as dt
hari_ini = dt.date.today()
print("Tanggal Pembelian                            :",hari_ini)
print("\n")
print("PEMBAYARAN KE REK. PERMATA 1237592669")
print("A/N LINGGA NUGRAHA")
print("T E R I M A  K A S I H")