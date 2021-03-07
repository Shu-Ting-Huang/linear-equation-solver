def frac2latex(x):
    if x.q == 1:
        return str(x.p)
    elif x.p > 0:
        return '\\frac{' + str(x.p) + "}{" + str(x.q) + "}"
    else:
        return '-\\frac{' + str(-x.p) + "}{" + str(x.q) + "}"

def frac2latex_omit1(x):
    if x == 1:
        return ""
    elif x == -1:
        return "-"
    elif x.q == 1:
        return str(x.p)
    elif x.p>0:
        return '\\frac{' + str(x.p) + "}{" + str(x.q) + "}"
    else:
        return '-\\frac{' + str(-x.p) + "}{" + str(x.q) + "}"