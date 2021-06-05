import math

def fa(r,n,aa):
    a = ((1 + r) ** n) - 1
    b = r
    return ((a / b) * aa)

def fp(r,n,aa):
    return aa*(1+r)**n


def pf(r,n,f):
    return f*((1+r)**-n)

def pa(r,n,aa):
    a = ((1+r)**n) - 1
    b = r*(1+r)**n
    return ((a/b)*aa)

def af(r,n,aa):
    a= r
    b = ((1+r)**n) -1
    return (aa*(a/b))

def ap(r,n,aa):
    a= r*(1+r)**n
    b = ((1+r)**n) -1
    return (aa*(a/b))


#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################


# The calculation of present worth:
def pw(capital, MARR, n, annual, future):

    answer = capital + pa(MARR,n,annual) + pf(MARR,n,future)

    return (answer)

def fw(capital, MARR, n, annual, future):

    a = pw(capital, MARR, n, annual, future)

    return fp(MARR,n,a)

def aw(capital, future, annualRevenue, annualExpenses, MARR, n):

    return (annualRevenue) - (annualExpenses) - (ap(MARR,n,capital) - af(MARR,n,future))




def bond(face, redemption, r, n, i):

    return pf(i,n,redemption) + pa(i,n, face*r)

def capatilized(capital, Annual, i, n, happensEveryNyears):

    return capital + Annual/i + af(i, n, happensEveryNyears)/i


#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################




#PW   MUST BE LARGER THAN 0
# print(f"The Present Worth Equals: { pw(capital= -50000,MARR= 0.16, n= 6, annual=28000, future= 0 ) }")

###############################################################################################################

#FW   MUST BE LARGER THAN 0 TO BE ACCEPTED
# print(f"The Future Worth Equals: { fw(capital= -5000,MARR= 0.1, n= 6, annual=1480, future= 0 ) }")

###############################################################################################################

#AW       Do not put any negative for any number.                 MUST BE LARGER THAN 0 TO BE ACCEPTED
# print(f"The Annual Worth Equals: { aw(capital = 14000, future = 2800, annualRevenue = 0, annualExpenses = 2400, MARR = 0.05, n = 18) }")

###############################################################################################################

#BOND   r = the normal rate of the bond (bond rate)      i = the desired rate of the bond (bond yield)
# print(f"The bond Equals: { bond(face= 5000, redemption= 5000, r = 0.08, n= 20, i = 0.089) }")

###############################################################################################################

#Capitalized Worth or Cost      n could be 0         happensEveryNyears could be 0
# print(f"The CW Equals: { capatilized(capital=-1900000, Annual= -25000, n= 8, i= 0.08, happensEveryNyears = -350000) }")

###############################################################################################################

#To find IRR set PW to 0 if MARR < IRR good investment .......







