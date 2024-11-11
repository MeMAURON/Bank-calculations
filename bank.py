customers = []
# Hafeze etelaat
while True:
   print("")
   print("Please select the desired option:  :")      
   print("1. Eftetahe hesab: ")
   print("2. Afzayeshe mojudi ")
   print("3. Exit ")
   
   choice = input()

   if choice == "1":
      
      national_code = input("Kode melli khod ra vared konid:...")
      name = input("Lotfan name and Family khod ra vared konid:... ")
      pull = float(input("Megdare pul Varizi ra vared konid:...."))

      if len(customers) >= 100:
            print("Hafeze account full ast!...")
      else:
            customers.append([national_code, name, pull])
            print("Hesab eftetah shod! ")
            print(customers)

      if choice == "2":
            
            national_code = input("Kode melli khod ra vared konid:...")
            
            found_customer = False
            for x in customers:
                  if x[0] == national_code:
                        found_customer = True                   
                        mablag_afzayesh = float(input("megdare Varizi ra vared konid:  "))
                        x[2] += mablag_afzayesh
                        print("Mojidi ba moafagiat afzayesh yaft! ")
                        print(f"Mojidi jadid shoma: {x[2]}")
                  else:
                        print("Kode melli eshtebah ast! ")





