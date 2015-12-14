import math
a = input()
c = input()
d = float(a/c)
if d>0:
	dr = round(d)
if d<0:
	dr = math.trunc(d)
print(d)
