import math
def f(y):
    Q_target=5.0
    B=20.0
    S=0.0002
    n=0.03
    numerator=math.sqrt(S)*((B*y)**(5/3))
    denominator=n*((B+2*y)**(2/3))
    return (numerator/denominator)-Q_target

def df(y):
    B=20.0
    S=0.0002
    n=0.03
    c=math.sqrt(S)/n
    term1=c*(B**(5/3))*(y**(2/3))*((B+2*y)**(-5/3))
    term2=(5.0/3.0)*B+2*y
    return term1*term2

def newton_raphson(func,dfunc,y0,tol=1e-6,max_iter=100):
    y=y0
    for i in range(max_iter):
        fy=func(y)
        dfy=dfunc(y)
        if dfy==0:
            return None
        y_new=y-(fy/dfy)
        if abs(y_new-y)<tol:
            return y_new
        y=y_new
    return y

root_y=newton_raphson(f,df,1.0)
print(f"The flow depth for Q = 5 m^3/s is: {root_y:.4f} m")