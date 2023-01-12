from sympy import integrate, diff, exp,cos,sin,pi
from sympy.abc import x,y,theta,a,b
a = 4
b = 3
x = a*cos(theta)
y = b*sin(theta)
dx = diff(x,theta)
dy = diff(y,theta)
Eq = (x+2*y)*dx + (4-2*x)*dy
I = integrate(Eq,(theta,0,2*pi))
print(I)
