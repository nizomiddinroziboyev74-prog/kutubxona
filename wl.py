# === VALYUTA KONVERTORI ===
kurslar = {"usd": 12800, "eur": 13800, "rub": 140}

while True:
    print("\n=== VALYUTA KONVERTORI ===")
    print("1. So‘mni valyutaga aylantirish")
    print("2. Valyutani so‘mga aylantirish")
    print("3. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        summa = float(input("So‘mda summa: "))
        tur = input("Qaysi valyutaga (usd/eur/rub): ").lower()
        if tur in kurslar:
            natija = round(summa / kurslar[tur], 2)
            print(f" {natija} {tur.upper()}")
        else:
            print("Bunday valyuta mavjud emas.")

    elif tanlov == "2":
        tur = input("Valyuta turi (usd/eur/rub): ").lower()
        if tur in kurslar:
            miqdor = float(input(f"{tur.upper()} miqdori: "))
            natija = miqdor * kurslar[tur]
            print(f" {natija} so‘m")
        else:
            print("Bunday valyuta mavjud emas.")

    elif tanlov == "3":
        print(" Dastur tugatildi.")
        break

    else:
        print(" Noto‘g‘ri tanlov!")