#rozwiazuje rownanie kwadratowe
import sys
import math

def solve(a, b, c):
    delta=b**2-4*a*c
    if delta > 0:
        result = [(-b-math.sqrt(delta))/2*a]
        result.append((-b+math.sqrt(delta))/2*a)
        return result
    if delta == 0:
        result = [-b/2*a]
        return result
    if delta < 0:
        return


try:
    a = (float)(sys.argv[1])
except ValueError:
    print ("Ojej, a przeciez to nie jest float...")
    exit()
try:
    b = (float)(sys.argv[2])
except ValueError:
    print ("Ojej, a przeciez to nie jest float...")
    exit()
try:
   c = (float)(sys.argv[3])
except ValueError:
    print ("Ojej, a przeciez to nie jest float...")
    exit()

print(solve(a,b,c))
