import json


with open("input..json", "r") as fp:
    soru_cevaplar = json.load(fp)

input_soru = input("soruyu yazar misin ? : ")
while not (input_soru == "q"):
    if (soru_cevaplar.get(input_soru)):
        print(soru_cevaplar.get(input_soru))
    else:
        print("boyle bir soru yok...")
    input_soru = input("soruyu yazar misin ? :")
