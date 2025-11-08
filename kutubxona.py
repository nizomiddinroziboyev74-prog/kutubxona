# === KUTUBXONA TIZIMI ===
kutubxona = []

while True:
    print("""
    === KUTUBXONA TIZIMI ===
    1. Kitob qo‘shish
    2. Kitoblar ro‘yxatini ko‘rish
    3. Kitobni qidirish
    4. Kitobni o‘chirish
    5. Chiqish
    """)
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        nom = input("Kitob nomi: ")
        muallif = input("Muallif: ")
        yil = input("Yili: ")
        kutubxona.append({"nom": nom, "muallif": muallif, "yil": yil})
        print("Kitob qo‘shildi!")

    elif tanlov == "2":
        if kutubxona:
            print("\nKutubxonadagi kitoblar:")
            for i, k in enumerate(kutubxona, 1):
                print(f"{i}. {k['nom']} ({k['muallif']}, {k['yil']})")
        else:
            print("❗ Kutubxona bo‘sh.")

    elif tanlov == "3":
        qidiruv = input("Qaysi kitobni qidiryapsiz? ")
        topildi = False
        for k in kutubxona:
            if qidiruv.lower() in k["nom"].lower():
                print(f" Topildi: {k['nom']} ({k['muallif']}, {k['yil']})")
                topildi = True
        if not topildi:
            print(" Kitob topilmadi.")

    elif tanlov == "4":
        nom = input("O‘chiriladigan kitob nomi: ")
        for k in kutubxona:
            if nom.lower() == k["nom"].lower():
                kutubxona.remove(k)
                print(" Kitob o‘chirildi.")
                break
        else:
            print("Bunday kitob topilmadi.")

    elif tanlov == "5":
        print(" Dastur tugatildi.")
        break

    else:
        print("Noto‘g‘ri tanlov!")