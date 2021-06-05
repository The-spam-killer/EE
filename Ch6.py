import ch5


def lowerUsefulLifeCoter(capital, annual, future,MARR, usefullife, totalLife):

    return ch5.fp(MARR,totalLife - usefullife, 1)*(ch5.fp(MARR,usefullife,capital)+ ch5.fa(MARR,usefullife,annual)+ future)



############ Use when only useful life < total life
# print(f"The future worth: {lowerUsefulLifeCoter(capital = -3500, annual = 1255, future = 0 ,MARR = 0.1, usefullife = 4, totalLife= 6)}")

