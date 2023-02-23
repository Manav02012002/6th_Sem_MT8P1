from sympy import*
from sympy.abc import x,y,z,a,b,c
def divergence(f1,f2,f3):
    return(f1.diff(x)+f2.diff(y)+f3.diff(z))

def GDT(D):
    I = simplify(integrate(D,(x,0,1),(y,0,2),(z,0,3)))
    print("The Answer using Gauss Divergence Theorem is ",I)
    return I
                 
def Surface_Integral(f1,f2,f3):
    I1 = simplify(integrate(f1.subs(x,1),(y,0,2),(z,0,3)))
    I2 = simplify(integrate(-f1.subs(x,0),(y,0,2),(z,0,3)))
    I3 = simplify(integrate(f2.subs(y,2),(x,0,1),(z,0,3)))
    I4 = simplify(integrate(-f2.subs(y,0),(x,0,1),(z,0,3)))
    I5 = simplify(integrate(f3.subs(z,3),(x,0,1),(y,0,2)))
    I6 = simplify(integrate(-f3.subs(z,0),(x,0,1),(y,0,2)))
    sum = simplify(I1+I2+I3+I4+I5+I6)
    print("The Answer using Surface Integral is ", sum)
    return sum
                 
f1 = 2*x*y
f2 = y*z**2
f3 = x*z
D = divergence(f1,f2,f3) 
S1 = GDT(D)
S2 = Surface_Integral(f1,f2,f3)
if(S1==S2):
    print("Gauss Divergence Theorem is verified")
else:
    print("Gauss Divergence Theorem is not verified")
