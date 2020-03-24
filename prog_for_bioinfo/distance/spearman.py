def Spearman(l1,l2):
    x = list(p)
    y = list(q)
    SD = 0
    for i in range(len(p)):
        if x[i] != y[i]:
            a = (y.index(x[i])+1)-(x.index(x[i])+1)
            SD += abs(a)
    print("Spearman Distance is:",SD)
    return l1,l2

'''Input:
p = "cefdab"
q = "cfebad"
Spearman(p,q)
'''
