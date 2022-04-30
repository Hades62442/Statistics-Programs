from math import sqrt

sumx2 = float(input("sum x2: "))
sumx = float(input("sum x: "))
sumy2 = float(input("sum y2: "))
sumy = float(input("sum y: "))
sumxy = float(input("sum xy: "))
avgx = float(input("avg x: "))
avgy = float(input("avg y: "))
n = int(input("n: "))
t = float(input("t: "))
xi = float(input("xi: "))

sxx = sumx2 - ((sumx**2)/n)
syy = sumy2 - ((sumy**2)/n)
sxy = sumxy - ((sumx*sumy)/n)

print(sxx, syy, sxy)

b = sxy / sxx
a = avgy - (b*avgx)

print(f"y = {a}+{b}x")

yhat = a + b*xi

ssr = syy - ((sxy**2)/sxx)
s2 = ssr / (n-2)
s = sqrt(s2)

print(ssr, s2, s)

final = t * s * sqrt((1/n)+(((xi-avgx)**2)/sxx))

print(f"{yhat} +- {final}")