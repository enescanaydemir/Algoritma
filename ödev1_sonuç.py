liste = []
for i in range (5):
    x = input("Bir sayı giriniz: ")
    liste.append(x)
liste.sort(reverse=True)
print(liste)

olustur=open ("221120181034_sonuc.txt","w")
for y in range (5):
    olustur.write(liste[y]+" ")