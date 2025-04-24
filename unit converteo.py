print("hello world this is a unit convertor.\n Enter respective number to convert.")
while True:
    print("""1. Celsius to Fahrenheit
    2. Fahrenheit to Celsius
    3. Meters to Kilometers
    4. Kilometers to Meters
    5. Grams to Kilograms
    6. Kilograms to Grams
    7. Exit""")
    choic = int(input("Choose one:>> "))
    if choic == 1:
        f = int(input("Temp in Fahrenheit: "))
        c = 5*(f-32)/9
        print("Temp in Celsius is ",c," °C")
    elif choic == 2:
        c = int(input("Temp in Celsius: "))
        f = 9*(c)/5+32
        print("Temp in Fahrenheit is ",f," °F")
    elif choic == 3:
        m = int(input("Length in Meter: "))
        km = m/1000
        print("Length in Kilometer ",km," km")
    elif choic == 4:
        km = int(input("Length in Kilometer: "))
        m = km*1000
        print("Length in Meter ",m,"m")    
    elif choic == 5:
        g = int(input("Mass in Gram: "))
        kg = g/1000
        print("Mass in Kilogram ",kg,"kg")
    elif choic == 6:
        kg = int(input("Mass in Kilogram: "))
        g = kg*1000
        print("Mass in Gram ",g,"g")    
    else:
        break