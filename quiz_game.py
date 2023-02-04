print("Kuis Pengetahuan Umum")

playing = input("Apakah kamu mau bermain?(yes/no) ")

if playing.lower() != "yes":
    quit()

print("Oke! Mari bermain :3")
score = 0

print("====================")
answer = input("Siapa menteri pendidikan sekarang? ")
if answer.lower() == "nadiem makarim":
    print('Jawaban kamu benar!')
    score += 1
else:
    print("Jawaban kamu salah!")

print("====================")
answer = input("Binatang yang bisa hidup di darat dan di air disebut? ")
if answer.lower() == "amfibi":
    print('Jawaban kamu benar!')
    score += 1
else:
    print("Jawaban kamu salah!")

print("====================")
answer = input("Negara terluas keempat di Dunia adalah? ")
if answer.lower() == "china":
    print('Jawaban kamu benar!')
    score += 1
else:
    print("Jawaban kamu salah!")

print("====================")
answer = input("Gunung tertinggi di Dunia adalah? ")
if answer.lower() == "gunung everest":
    print('Jawaban kamu benar!')
    score += 1
else:
    print("Jawaban kamu salah!")
    
print("====================")    
answer = input("Arah jam 9 itu sama dengan arah mata angin ke? ")
if answer.lower() == "barat":
    print('Jawaban kamu benar!')
    score += 1
else:
    print("Jawaban kamu salah!")

print("===================")
print("Kamu berhasil menjawab " + str(score) + " pertanyaan dengan benar!")
print("Kamu mendapatkan nilai " + str((score / 5) * 100) + "%.")
print("===================")