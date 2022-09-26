travelbag = ["Tröja", "Badbyxor", "Mobil", "Bok"]

while True:
       menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program")

       if menyval == "1":
              print(travelbag)

       elif menyval == "2":
             Penna = input("vad vill du lägga i väskan?")
             travelbag.append(Penna)
             print(travelbag)
             

       elif menyval == "3":
              Mobil = input("vad vill ta bort från väskan?")
              travelbag.remove(Mobil)
              print(travelbag)
              

       elif menyval == "4":
              break
       