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
       |HAPPY BIRTHDAY JAELANI|
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

mengetik(HAPPY BIRTHDAY TO ME! ✨", 0.08)
mengetik("cieee 20 thn nih,for my self Semoga panjang umur, sehat selalu,semoga target nya tercapai, dan makin sukses.", 0.05)
mengetik("Tetap jadi orang baik dan bahagia terus! 🥳🎉", 0.05)
