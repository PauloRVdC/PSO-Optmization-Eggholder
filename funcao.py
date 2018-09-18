import math

def eggHolder(x):
    term1 = -(x[1]+47) * math.sin(math.sqrt(math.fabs(x[1]+x[0]/2+47)))
    term2 = -x[0] * math.sin(math.sqrt(math.fabs(x[0]-(x[1]+47))))
    result = term1 + term2
    return result