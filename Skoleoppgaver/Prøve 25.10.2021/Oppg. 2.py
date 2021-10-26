
#Spør etter passord, gjør det om til string.
passord = str(input("skriv inn passord: "))

#Tar lengden av passordet som int og ganger det med ' * ' omgjort til en string
passordStjerne = str(len(passord) * str("*"))

#Tar lengden av passordet som int og omgjør til string.
passordString = str(len(passord))

print("Passordet er " + passordStjerne)
print("Passordet er " + passordString + " bokstaver langt.")



