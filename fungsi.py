while True:
  print("Pilihan:")
  print("1. Hitung luas persegi panjang")
  print("2. Hitung luas lingkaran")
  print("3. Hitung nilai fungsi")
  print("4. selesai?")
  pilihan=int(input("Masukkan pilihan anda tuan: "))
  if pilihan == 1:
    panjang = float(input("Masukkan nilai panjang: "))
    lebar = float(input("Masukkan nilai lebar: "))
    luas = panjang * lebar
    print("Luas persegi panjang adalah:", luas)
  elif pilihan == 2:
    jari_jari = float(input("Masukkan jari-jari: "))
    luas = 3.14 * jari_jari * jari_jari
    print("Luasnya adalah:", luas)
  elif pilihan == 3:
    x = float(input("Masukkan nilai x: "))
    hasil = 2*x*x + 3*x - 10
    print("Hasilnya adalah:", hasil)
  elif pilihan == 4:
    break
  else:
      print("pilihan tidaj valid,silahkan pilih 1,2 dan 3")
