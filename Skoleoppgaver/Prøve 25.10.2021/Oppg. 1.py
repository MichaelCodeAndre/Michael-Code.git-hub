
#Spør som integer slik at man kan kunne regne dette ut.
lengde = int(input("skriv inn lengden på rektangelet: "))
bredde = int(input("Skriv inn bredden på rektangelet: "))

#Regner ut og gir svaret som string.
omkrets = str(lengde *2 + bredde * 2)
areal = str(lengde * bredde)

print("Omkretsen er: " + omkrets)
print("Arealet er: " + areal)


