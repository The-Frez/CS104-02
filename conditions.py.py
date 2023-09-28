# CS104

# Luca Bertinelli

# conditions.py

i = 0

while i < 5:
    temp = float(input("Please enter the current temperature: "))

    if temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay Inside")

    i += 1
            
