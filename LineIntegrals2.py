from sympy import integrate, diff
from sympy.abc import x,y
y = x**2+1
dx = diff(x,x)
dy = diff(y,x)
Eq = (3*x+y)*dx + (2*y-x)*dy
I = integrate(Eq,(x,0,3))
print(I)
