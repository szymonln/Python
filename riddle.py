#odpytuje dwie liczby, zakres, pozniej zgadujemy
#random -> randint

import random

try:
    x = (int)(input("Podaj poczatek przedzialu do losowania: "))
except ValueError:
    print ("Ojej, a przeciez to nie jest liczba...")

try: 
    y=(int)(input("Podaj koniec przedzialu: "))
except ValueError:
    print ("Ojej, a przeciez to nie jest liczba...")

riddle=random.randint(x,y)

while True:
    try:
        z = (int)(input("Zgaduj: "))
        if z == riddle:
            print ("Braawo")
            break
    except ValueError:
        print ("Ojej, a przeciez to nie jest liczba...")


