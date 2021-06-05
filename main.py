import math

def Breakeven1(Cv,Cf,p):
    print(f"Breakeven: {math.ceil(Cf/(p-Cv))}")


def Breakeven2(a,Cv,b,Cf):

    D1 = -(a-Cv) + math.sqrt((a-Cv)**2 - (4*-b*-Cf))
    D2 = -(a-Cv) - math.sqrt((a-Cv)**2 - (4*-b*-Cf))
    base = 2*(-b)

    print(f"Break even 1: {math.ceil(D1 / base)}\nBreak even 2: {math.floor(D2 / base)}")

def uniformGradient1(g,i,n):
    print(f"First part : {g*((1/i)*( ((((1+i)**n)-1)/(i*((1+i)**n))) - (n/((1+i)**n)) ))}")

def uniformGradient2(g,i,n):
    print({f"First part : {g*( (1/i) - ((n)/(((1+i)**n)-1)) )}"})

def uniformGradient3(g,i,n):
    a = ( (((1+i)**n) -1) /  (i) )
    print(f"First part : {(g / i) * (a) - ((n*g)/(i))}")

def geometricSeequence1(i, f, n,A):
    pf = (1+i)**-n
    fp = (1+f)**n
    a = A*(1 - (pf*fp)) / (i-f)

    print(f"Present value : {a}")

def geometricSeequence2(i, n,A):
    pf = (1 + i) ** -1
    print(f"Present value : {A*n*pf}")




# Breakeven2(a= 228000,Cv=180513.57,b=1400,Cf=350000)
# Breakeven1(Cv=450,Cf=180000,p=700)

# Present Value
# uniformGradient1(g= 1000, i=0.15, n=4)

# Annuaty Value
# uniformGradient2(g= 1, i=0.06, n=10)

# Future Value
uniformGradient3(g= 1, i=0.032, n=9)

# When f != i
# geometricSeequence1(i= 0.045, f= 0.02, n=32, A=1000)

# f == i
# geometricSeequence2(i=0.25, n=4,A=1000)