class jual_beli:
  #fungsi rumus harga kali banyak barang
  def harga_total(harga_satuan, jumlah_barang):
    return harga_satuan*jumlah_barang
  
 #fungsi tanpa kembalian berisi identitas kelompok 
  def Identitas_kelompok():
    print("Kelompok 35")
    print("Shift 2")
    print("Eng....")
    print("Muhammad Sulthon Auliya 21120120130047")
    print("Rafif ....")
  
#program main/untuk eksekusi
x="y"
  #perulangan berupa jumlah berapa kali transksi
while(x=="y"):
    #switch case pada python menggunakan array. sebagai datalist barang yang tersedia untuk pemilihan barang.
  list_barang:{
    1:"Buku tulis",
    2:"Pensil",
    3:"Bolpoin"
    } 
  pilihan=int(input("masukan pilihan anda"))
  print("Barang yang tersedia: %s"%list_barang.set.default(pilihan, "pilih (1-3)"))
  
  
  
  
    
  x=input("Beli barang lain?("y"=yes,selain itu dianggap no) ")   
  
  
#penjelasan
Program ini merupakan program sederhana yang berfungsi melakukan mekanisme perhitungan jual beli.
disini dalam class yang bernama jual_beli, terdapat 2 fungsi method yaitu yang pertama adalah
yang pertama adalah fungsi harga_total yang merupakan fungsi kembalian yang mengembalikan nilai dari parameternya
yaitu mengembalikan operasi perkalian variabel harga_satuan dan jumlah_barang. selanjutnya merupakan fungsi identitas_kelompok yang akan mengeluarkan beberapa output.




