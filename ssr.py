from math import sqrt

sumx2 = float(input("sum x2: "))
sumx = float(input("sum x: "))
sumy2 = float(input("sum y2: "))
sumy = float(input("sum y: "))
sumxy = float(input("sum xy: "))
n = int(input("n: "))

sxx = sumx2 - ((sumx**2)/n)
syy = sumy2 - ((sumy**2)/n)
sxy = sumxy - ((sumx*sumy)/n)

ssr = syy - ((sxy**2)/sxx)
s2 = ssr / (n-2)
s = sqrt(s2)

print(f"Sxx: {sxx}\nSyy: {syy}\nSxy: {sxy}\nSSR: {ssr}\ns2: {s2}\ns: {s}")