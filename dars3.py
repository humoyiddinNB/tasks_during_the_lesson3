import os
os.system("cls")


# ######      35 -masala
def printer():
    try:
        b = 1
        c = int(input("Nechta to'plam yaratmoqchisiz? "))
        big_toplam = []
        while b <= c:
            litlle_toplam = []
            a = 1
            while True:
                d = int(input(f"{a} - sonni kiriting"))
                if d == 0:
                    break
                litlle_toplam.append(d)
                a += 1
            big_toplam.append(litlle_toplam)
            print(f"{b} - toplam yaratildi, elementlar soni: {len(litlle_toplam)}")
            b += 1
        return f"Umumiy toplam: {big_toplam}"
    except:
        return f"nimadir xato ketti, faqat sonlar kiriting"
    
print(printer())
   


