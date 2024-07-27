def areac(r):
 res=3.14*r*r
 return res
def arear(l,b):
  res=l*b
  return res
def areas(s):
  res=s*s
  return res
def areat(b,h):
  res=0.5*b*h
  return res
radius=10
length=4
breadth=5
side=2
base=4
height=5
print("area of circle: ",areac(radius))
print("area of rectangle: ",arear(length,breadth))
print("area of square: ",areas(side))
print("area of triangle: ",areat(base,height))
