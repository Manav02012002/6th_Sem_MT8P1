from sympy import integrate, diff, exp
from sympy.abc import x,y,t
x = exp(t)
y = exp(-t)
z = t**2
dx = diff(x,t)
dy = diff(y,t)
dz = diff(z,t)
Eq = (x*y)*dx+(x**2*z)*dy+(x*y*z)*dz
I = integrate(Eq,(t,0,1))
print(I)
