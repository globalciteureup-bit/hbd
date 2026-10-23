import time
import sys

def mengetik(teks, kecepatan=0.05):
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(kecepatan)
    print()

def tampilkan_kue():
    kue = """
         (  )   (  )   (  )
          ||     ||     ||
        .______.______.______.
       |(  o  )  (  o  )  (  o )|
       |                      |
       |______________________|
       |                      |
       |HAPPY BIRTHDAY DINI   |
       |______________________|
    """
    print(kue)

# Jalankan Animasi
mengetik("Initializing surprise protocol...", 0.03)
time.sleep(1)
mengetik("3... 2... 1...", 0.3)
print("\n")

tampilkan_kue()
time.sleep(1)

mengetik(HAPPY BIRTHDAY TO YOUUU MY DINONG!🥳✨", 0.08)
mengetik(" CIE CIE NAMBAH TUA AJA NIEE ,TERUNTUK PEREMPUAN YANG BERNAMA "DINI" SEMOGA PANJANG UMUR,TARGET"NYA TERCAPAI,SEHAT CERIA SELALU.", 0.05)
mengetik("TETAPLAH JADI ORANG YANG BAIK DAN RAMAH SENYUM YEE!! 🥳🎉", 0.05)
