from math import sqrt

sumx2 = float(input("sum x2: "))
sumx = float(input("sum x: "))
sumy2 = float(input("sum y2: "))
sumy = float(input("sum y: "))
sumxy = float(input("sum xy: "))
avgx = float(input("avg x: "))
avgy = float(input("avg y: "))
n = int(input("n: "))

sxx = sumx2 - ((sumx**2)/n)
syy = sumy2 - ((sumy**2)/n)
sxy = sumxy - ((sumx*sumy)/n)

r = sxy / (sqrt(sxx*syy))

print(f"Sxx: {sxx}\nSyy: {syy}\nSxy: {sxy}\nr: {r}")