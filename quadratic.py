import cmath
a=int(input("enter the value:"))
b=int(input("enter the value of b is:"))
c=int(input("enter the value of c is:"))
d=(b**2) - (4*a*c)
x= (-b-cmath.sqrt(d))/(2*a)
y=(-b+cmath.sqrt(d))/(2*a)
print("the solution of {0} and{1}:".format(x,y))