from sympy import*
from sympy.abc import x,y,z,a,b,c
def divergence(f1,f2,f3):
    return(f1.diff(x)+f2.diff(y)+f3.diff(z))

def GDT(D):
    I = simplify(integrate(D,(x,0,a),(y,0,b),(z,0,c)))
    print("The Answer using Gauss Divergence Theorem is ",I)
    return I
                 
def Surface_Integral(f1,f2,f3):
    I1 = simplify(integrate(f1.subs(x,a),(y,0,b),(z,0,c)))
    I2 = simplify(integrate(-f1.subs(x,0),(y,0,b),(z,0,c)))
    I3 = simplify(integrate(f2.subs(y,b),(x,0,a),(z,0,c)))
    I4 = simplify(integrate(-f2.subs(y,0),(x,0,a),(z,0,c)))
    I5 = simplify(integrate(f3.subs(z,c),(x,0,a),(y,0,b)))
    I6 = simplify(integrate(-f3.subs(z,0),(x,0,a),(y,0,b)))
    sum = simplify(I1+I2+I3+I4+I5+I6)
    print("The Answer using Surface Integral is ", sum)
    return sum
                 
f1 = x**2 - y*z
f2 = y**2 - z*x
f3 = z**2 - x*y
D = divergence(f1,f2,f3) 
S1 = GDT(D)
S2 = Surface_Integral(f1,f2,f3)
if(S1==S2):
    print("Gauss Divergence Theorem is verified")
else:
    print("Gauss Divergence Theorem is not verified")
     
