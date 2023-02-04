print("Kuis Pengetahuan Umum")

playing = input("Apakah kamu mau bermain?(yes/no) ")

if playing.lower() != "yes":
    quit()

print("Oke! Mari bermain :3")
nilai = 0

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
jawaban = input("Siapa menteri pendidikan sekarang? ")
if jawaban.lower() == "nadiem makarim":
    print('Jawaban kamu benar!')
    nilai += 1
else:
    print("Jawaban kamu salah!")
    
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
jawaban = input("Binatang yang bisa hidup di darat dan di air disebut? ")
if jawaban.lower() == "amfibi":
    print('Jawaban kamu benar!')
    nilai += 1
else:
    print("Jawaban kamu salah!")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
jawaban = input("Negara terluas keempat di Dunia adalah? ")
if jawaban.lower() == "china":
    print('Jawaban kamu benar!')
    nilai += 1
else:
    print("Jawaban kamu salah!")
    
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
jawaban = input("Gunung tertinggi di Dunia adalah? ")
if jawaban.lower() == "gunung everest":
    print('Jawaban kamu benar!')
    nilai += 1
else:
    print("Jawaban kamu salah!")
    
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")    
jawaban = input("Arah jam 9 itu sama dengan arah mata angin ke? ")
if jawaban.lower() == "barat":
    print('Jawaban kamu benar!')
    nilai += 1
else:
    print("Jawaban kamu salah!")

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Kamu berhasil menjawab " + str(nilai) + " pertanyaan dengan benar!")
print("Kamu mendapatkan nilai " + str((nilai / 5) * 100) + "%.")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")