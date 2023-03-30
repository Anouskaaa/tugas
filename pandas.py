import pandas

namaLengkap = ["Risdianto", "Emi Marliatun", "Effi", "Ani Sophia", "Heni Purwati", "Irfan", "Etika", "Nana", "Iyop", "Ade"]
noInduk = ["2004001", "2004002", "2004003", "2004004", "2004005", "2004006", "2004007", "2004008", "2004009", "20040010"]
pengenalanKomputer = ["90", "80", "70", "80", "85", "85", "87", "90", "95", "97"]
bahasaPemrograman = ["70", "90", "85", "90", "60", "75", "70", "80", "78", "95"]
programAplikasi = ["70", "90", "90", "80", "80", "85", "70", "65", "90", "50"]

n = pandas.DataFrame({
  
  "No.": ["1","2","3","4","5","6","7","8","9","10"],
  "Nama Lengkap": namaLengkap,
  "No. Induk": noInduk,
  "Pengenalan Komputer": pengenalanKomputer,
  "Bahasa Pemrograman": bahasaPemrograman,
  "Program Aplikasi": programAplikasi
})
n
