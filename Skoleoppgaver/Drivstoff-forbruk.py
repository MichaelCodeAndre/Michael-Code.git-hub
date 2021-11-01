# This program figures out your fuel consumption, tank size, petrol price and will end with telling the consumer how much they will need to pay.
#I'm also using this as a chance to learn more about python and get used to writing to make it easy to see what's going on in my code.


#------------------------------------------ VARIABLES ------------------------------------------

carModel = int(0)

#------------------------------------------ /VARIABLES ------------------------------------------

#------------------------------------------ TANK SIZE ------------------------------------------

tankSize = input("How many litres can your tank hold? (Type 'help' if you don't know.) ")

if (tankSize == 'help') :
    print("Here are your options for cars:")
    print("If 'Prosche 911 Carerra 4S' type 1")
    print("If 'Skoda Fabia' type 2")
    print("If 'Rolls Royce Wraith' type 3")
    print("If 'Bugatti Chiron' type 4")
    carModel = int(input("What number is your car? "))

if (carModel == 1) :
    tankSize = 67
    print("You picked Porsche 911 Carrera 4S with tank size of 67 litres.")

if (carModel == 2) :
    tankSize = 45
    print("You picked Skoda Fabia with a tank size of 45 litres.")

if (carModel == 3) :
    tankSize = 83
    print("You picked Rolls Royce Wraith with a tank size of 83 litres.")    

if (carModel == 4) :
    tankSize = 100
    print("You picked Bugatti Chiron with a tank size of 100 litres.")

#------------------------------------------ /TANK SIZE ------------------------------------------

#------------------------------------------ FUEL CONSUMPTION ------------------------------------------

fuelConsume = input("What is your fuel consumption like in litres per kilometer? (Type 'help' if you don't know.) ")

if (fuelConsume == 'help') : 
    print("Here are your options for cars:")
    print("If 'Prosche 911 Carerra 4S' type 1")
    print("If 'Skoda Fabia' type 2")
    print("If 'Rolls Royce Wraith' type 3")
    print("If 'Bugatti Chiron' type 4")
    carModel = int(input("What number is your car? "))

if (carModel == 1) :
    fuelConsume = 0.11

if (carModel == 2) :
    fuelConsume = 0.059

if (carModel == 3) :
    fuelConsume = 0.16

if (carModel == 4) :
    fuelConsume = 0.225

#------------------------------------------ / FUEL CONSUMPTION ------------------------------------------

#------------------------------------------ PETROL PRICE ------------------------------------------

petrolPrice = float(input("What is the price per litre at your petrol station like in NOK? "))
#------------------------------------------ /PETROL PRICE ------------------------------------------

#------------------------------------------ RESULTS ------------------------------------------

print(fuelConsume)
print(tankSize)
#------------------------------------------ /RESULTS ------------------------------------------