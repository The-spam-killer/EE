import math

def effective(r):
    print(f"The effective is: {(math.exp(r)-1).__round__(5)}")

def pf(r,n,f):
    print(f"The Present value is: {(math.exp(-r*n))*f}")

def fp(r,n,p):
    print(f"The Future value is: {(math.exp(r*n))*p}")

def fa(r,n,aa):
    a = math.exp(r*n) - 1
    b = math.exp(r) - 1
    print(f"The Future value is: {(a/b)*aa}")

def af(r,n,f):
    a = math.exp(r*n) - 1
    b = math.exp(r) - 1
    print(f"The Annuaty value is: {(b/a)*f}")

def pa(r,n,aa):
    a = math.exp(r*n) - 1
    b = math.exp(r*n) * (math.exp(r) - 1)
    print(f"The Present value is: {(a/b)*aa}")

def ap(r,n,p):
    a = math.exp(r*n) - 1
    b = math.exp(r*n) * (math.exp(r) - 1)
    print(f"The Annuaty value is: {(b/a)*p}")

# entebah r la2aish year wela semi wela .....
effective(r = 0.145)
# fp(r= 0.19,n=5,p=37894.33)
# af(r=0.08,n=10,f=8000)
# pa(r=0.19 ,n= 3, aa=5000)
# fa(r=0.04,n= 12,aa=243)