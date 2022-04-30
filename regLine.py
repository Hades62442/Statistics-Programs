sumx2 = float(input("sum x2: "))
sumx = float(input("sum x: "))
sumy = float(input("sum y: "))
sumxy = float(input("sum xy: "))
avgx = float(input("avg x: "))
avgy = float(input("avg y: "))
n = int(input("n: "))

sxx = sumx2 - ((sumx**2)/n)
sxy = sumxy - ((sumx*sumy)/n)

b = sxy / sxx
a = avgy - (b*avgx)

print(f"Sxx: {sxx}\nSxy: {sxy}\ny = {a}+{b}x")