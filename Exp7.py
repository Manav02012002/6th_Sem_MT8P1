from sympy import*
from sympy.abc import s,t
def Inverse_Laplace(f):
    il = inverse_laplace_transform(f, s, t)
    pprint(il)
f = s/(s-3)**5
Inverse_Laplace(f)
